"""Exercise D through the real local Camunda API. Creates only labelled demo cases.

Start c8run and the formal Java application first. Run from hospital-pathway:
python scripts/smoke_member_d.py
Credentials can be overridden with CAMUNDA_USERNAME / CAMUNDA_PASSWORD.
"""
from pathlib import Path
import base64
import datetime as dt
import json
import os
import time
import urllib.error
import urllib.request

BASE = os.environ.get('CAMUNDA_REST_URL', 'http://localhost:8080').rstrip('/')
AUTH = base64.b64encode((os.environ.get('CAMUNDA_USERNAME','demo')+':'+os.environ.get('CAMUNDA_PASSWORD','demo')).encode()).decode()
PROCESS = 'Hospital_All_Processes_Simple_C8'
ROOT = Path(__file__).resolve().parents[1]
STAMP = dt.datetime.now().strftime('%Y%m%d-%H%M%S')
PREFIX = 'D-SIMPLE-'+STAMP
EVIDENCE = {'run':PREFIX,'method':'real local Camunda REST; actual forms bound, task completions submitted by API','instances':[]}

def api(method, path, body=None):
    data = None if body is None else json.dumps(body).encode()
    request = urllib.request.Request(BASE+'/v2'+path, data=data, method=method,
            headers={'Authorization':'Basic '+AUTH,'Content-Type':'application/json'})
    try:
        with urllib.request.urlopen(request,timeout=20) as response:
            raw=response.read()
            return json.loads(raw) if raw else {}
    except urllib.error.HTTPError as error:
        raise RuntimeError(f'{method} {path}: {error.code} {error.read().decode()}') from error

def wait_for(fn, description, timeout=45):
    deadline=time.monotonic()+timeout
    while time.monotonic()<deadline:
        value=fn()
        if value: return value
        time.sleep(.5)
    raise AssertionError('Timed out: '+description)

def task(instance, element):
    def find():
        tasks=api('POST','/user-tasks/search',{'filter':{'processInstanceKey':instance,'state':'CREATED'}})['items']
        return next((t for t in tasks if t['elementId']==element),None)
    return wait_for(find,element+' in '+instance)

def complete(record, element, **variables):
    item=task(record['processInstanceKey'],element)
    values={'patientId':record['case'],'staffRole':'D-DEMO / relevant team','clinicianId':'D-DEMO-CLINICIAN',
            'specialty':'Demo','priority':'routine','timeframe':'Demo agreed timeframe',
            'notes':'Synthetic classroom verification only','action':'recorded'}
    values.update(variables)
    api('POST',f"/user-tasks/{item['userTaskKey']}/completion",{'variables':values})
    record['tasks'].append({'element':element,'userTaskKey':item['userTaskKey'],'formKey':item.get('formKey'),'action':values['action']})

def start(definition, scenario):
    case=PREFIX+'-'+scenario
    instance=api('POST','/process-instances',{'processDefinitionKey':definition,
            'variables':{'patientId':case}})
    record={'scenario':scenario,'case':case,'processInstanceKey':instance['processInstanceKey'],'tasks':[]}
    EVIDENCE['instances'].append(record)
    return record

def finish(record, expected_variable, expected_value):
    key=record['processInstanceKey']
    state=wait_for(lambda:(p if (p:=api('GET','/process-instances/'+key))['state']=='COMPLETED' else None),'completed '+key)
    variables=api('POST','/variables/search',{'filter':{'processInstanceKey':key},'page':{'limit':100}})['items']
    decoded={v['name']:json.loads(v['value']) for v in variables if not v.get('isTruncated',False)}
    if expected_variable:
        assert decoded.get(expected_variable)==expected_value,(record['scenario'],decoded)
    else:
        assert 'enquiryAcknowledgementSent' not in decoded, 'Optional Worker still ran'
    incidents=api('POST','/incidents/search',{'filter':{'processInstanceKey':key,'state':'ACTIVE'}})['items']
    assert not incidents,incidents
    record.update(state=state['state'],notificationVariables={k:v for k,v in decoded.items()
                  if k.startswith(('careChangeNotification','enquiryAcknowledgement'))},activeIncidents=0)
    print(record['scenario'],key,'COMPLETED',record['notificationVariables'],flush=True)

def main():
    definitions=api('POST','/process-definitions/search',{'filter':{'processDefinitionId':PROCESS},'sort':[{'field':'version','order':'DESC'}]})['items']
    assert definitions,'Deploy the formal project first'
    definition=definitions[0]
    EVIDENCE['definition']=definition
    key=definition['processDefinitionKey']
    for kind,element in [('admin','AdminEnquiry'),('clinical','ClinicalEnquiry'),('finance','FinanceEnquiry')]:
        record=start(key,kind)
        complete(record,'Register',action='enquiry_'+kind)
        complete(record,element)
        finish(record,None,None)
    for scenario,decision in [('change','discharge_unpaid'),('financial-change','discharge_paid')]:
        record=start(key,scenario)
        complete(record,'Register',action='change')
        complete(record,'ClinicalChange',action=decision)
        if decision.endswith('_paid'): complete(record,'FinanceAdjustment',action='resolved')
        finish(record,'careChangeNotificationStatus','SENT_FINANCE_REVIEW_REQUIRED' if decision.endswith('_paid') else 'SENT')
    record=start(key,'unapproved-then-corrected')
    complete(record,'Register',action='change')
    complete(record,'ClinicalChange',action='invalid')
    task(record['processInstanceKey'],'GetDocuments')
    values=api('POST','/variables/search',{'filter':{'processInstanceKey':record['processInstanceKey'],'name':'careChangeNotificationSent'}})['items']
    assert values and all(json.loads(v['value']) is False for v in values)
    record['unapprovedNotificationSkipped']=True
    complete(record,'GetDocuments')
    complete(record,'Register',action='change')
    complete(record,'ClinicalChange',action='discharge_unpaid')
    finish(record,'careChangeNotificationSent',True)
    record=start(key,'cancel-visit-change')
    complete(record,'Register',action='referral')
    complete(record,'ReviewReferral',action='accept')
    complete(record,'BookVisit',action='cancelled')
    complete(record,'ClinicalChange',action='discharge_unpaid')
    finish(record,'careChangeNotificationSent',True)

if __name__=='__main__':
    try:
        main()
        EVIDENCE['result']='PASS'
    finally:
        path=ROOT/'target'/f'member-d-smoke-{STAMP}.json'
        path.parent.mkdir(exist_ok=True)
        path.write_text(json.dumps(EVIDENCE,ensure_ascii=False,indent=2),encoding='utf-8')
        print('Evidence:',path,flush=True)
