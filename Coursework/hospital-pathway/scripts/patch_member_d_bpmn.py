"""Add D's four visible tasks; preserve other members' process definitions."""
from pathlib import Path
import re
import xml.etree.ElementTree as ET

PATH = Path(__file__).resolve().parents[1] / 'bpmn/W02_Hospital_All_Processes_Clean_Lines_Camunda8.bpmn'

def patch(text):
    if 'id="NotifyCareChange"' in text:
        return text

    def replace(old, new):
        nonlocal text
        if text.count(old) != 1:
            raise ValueError(f'Expected one occurrence: {old}')
        text = text.replace(old, new, 1)

    def block(kind, identifier, transform):
        nonlocal text
        pattern = rf'<{kind}\b[^>]*\bid="{identifier}"[^>]*>[\s\S]*?</{kind}>'
        text, count = re.subn(pattern, lambda m: transform(m.group()), text)
        if count != 1:
            raise ValueError(f'Missing block {identifier}')

    def points(flow, coords, label=None):
        def update(old):
            start = old[:old.index('>')+1]
            waypoints = ''.join(f'\n        <di:waypoint x="{x}" y="{y}" />' for x,y in coords)
            labels = '' if label is None else (f'\n        <bpmndi:BPMNLabel><dc:Bounds x="{label[0]}" y="{label[1]}" width="90" height="28" /></bpmndi:BPMNLabel>')
            return start + waypoints + labels + '\n      </bpmndi:BPMNEdge>'
        block('bpmndi:BPMNEdge', flow+'_di', update)

    def bounds(node, x, y, w, h, label=None):
        def update(old):
            old = re.sub(r'<dc:Bounds[^>]*/>', f'<dc:Bounds x="{x}" y="{y}" width="{w}" height="{h}" />', old, count=1)
            if label:
                old = re.sub(r'<bpmndi:BPMNLabel>[\s\S]*?</bpmndi:BPMNLabel>',
                    f'<bpmndi:BPMNLabel><dc:Bounds x="{label[0]}" y="{label[1]}" width="90" height="28" /></bpmndi:BPMNLabel>', old)
            return old
        block('bpmndi:BPMNShape', node+'_di', update)

    specs = [
        ('NotifyCareChange','P11 / P12&#10;Notify care change','notify-care-change','Clinical','ClinicalChange','ChangeValid','Flow_51',1020,1060,140,100,'#eaf8f0'),
        ('AckAdminEnquiry','P10&#10;Send enquiry receipt','ack-enquiry-routed','Admin','AdminEnquiry','EndAdminEnquiry','Flow_25',310,630,220,60,'#edf5ff'),
        ('AckClinicalEnquiry','P10&#10;Send enquiry receipt','ack-enquiry-routed','Clinical','ClinicalEnquiry','EndClinicalEnquiry','Flow_26',310,1170,220,60,'#eaf8f0'),
        ('AckFinanceEnquiry','P10&#10;Send enquiry receipt','ack-enquiry-routed','Finance','FinanceEnquiry','EndFinanceEnquiry','Flow_27',310,1730,220,70,'#fff3e5'),
    ]
    for node,name,job,lane,source,target,flow,x,y,w,h,fill in specs:
        newflow = flow+'_D'
        replace(f'<bpmn:sequenceFlow id="{flow}" sourceRef="{source}" targetRef="{target}" />',
                f'<bpmn:sequenceFlow id="{flow}" sourceRef="{source}" targetRef="{node}" />\n'
                f'    <bpmn:sequenceFlow id="{newflow}" sourceRef="{node}" targetRef="{target}" />')
        target_kind = 'bpmn:exclusiveGateway' if target=='ChangeValid' else 'bpmn:endEvent'
        block(target_kind,target,lambda s:s.replace(f'<bpmn:incoming>{flow}</bpmn:incoming>',f'<bpmn:incoming>{newflow}</bpmn:incoming>'))
        docs = (f'Member D (Ryan), type {job}: mock external notification, append audit_event with a unique task receipt before completing. '
                'No real email/SMS. Care changes require formal authorisation; financial changes only read payment_ledger and request Finance review. '
                'Human forms and gateway decisions remain authoritative. No BPMN message catch is required for this synchronous mock job.')
        task = f'''    <bpmn:serviceTask id="{node}" name="{name}">
      <bpmn:documentation>{docs}</bpmn:documentation>
      <bpmn:extensionElements>
        <zeebe:taskDefinition type="{job}" retries="3" />
      </bpmn:extensionElements>
      <bpmn:incoming>{flow}</bpmn:incoming>
      <bpmn:outgoing>{newflow}</bpmn:outgoing>
    </bpmn:serviceTask>
'''
        replace('  </bpmn:process>',task+'  </bpmn:process>')
        block('bpmn:lane',lane,lambda s:s.replace('</bpmn:lane>',f'  <bpmn:flowNodeRef>{node}</bpmn:flowNodeRef>\n      </bpmn:lane>'))
        shape = f'''      <bpmndi:BPMNShape id="{node}_di" bpmnElement="{node}" bioc:stroke="#263746" bioc:fill="{fill}">
        <dc:Bounds x="{x}" y="{y}" width="{w}" height="{h}" />
      </bpmndi:BPMNShape>
'''
        if source == 'ClinicalChange':
            outgoing = [(1160,1110),(1180,1110)]
        else:
            cy = y+h//2
            bounds(target,590,cy-20,40,40,(560,cy+25))
            points(flow,[(420,y-10 if lane!='Finance' else 1700),(420,y)])
            outgoing = [(530,cy),(590,cy)]
        edge = f'      <bpmndi:BPMNEdge id="{newflow}_di" bpmnElement="{newflow}" bioc:stroke="#667481">\n'
        edge += ''.join(f'        <di:waypoint x="{px}" y="{py}" />\n' for px,py in outgoing)
        edge += '      </bpmndi:BPMNEdge>\n'
        replace('    </bpmndi:BPMNPlane>',shape+edge+'    </bpmndi:BPMNPlane>')

    # Make space for a readable, inline change Worker before the existing gateway.
    bounds('ClinicalChange',790,1060,190,100)
    points('Flow_51',[(980,1110),(1020,1110)])
    points('Flow_52',[(1200,1090),(1200,1000),(1130,1000),(1130,620)],(1140,975))
    for flow in ['Flow_22','Flow_36','Flow_62']:
        def move_endpoint(old):
            matches = list(re.finditer(r'<di:waypoint x="([^"]+)" y="([^"]+)" />',old))
            last=matches[-1]; ox,oy=map(float,last.groups())
            nx=790 if ox==880 else 885 if ox==1000 else ox
            old=old[:last.start()]+f'<di:waypoint x="{nx:g}" y="{oy:g}" />'+old[last.end():]
            if len(matches)>1:
                prev=matches[-2]; px,py=map(float,prev.groups())
                if px==ox:
                    old=old[:prev.start()]+f'<di:waypoint x="{nx:g}" y="{py:g}" />'+old[prev.end():]
            return old
        block('bpmndi:BPMNEdge',flow+'_di',move_endpoint)
    text=text.replace("Other members' workers are not in this diagram yet.",
            "Member D added notify-care-change and three ack-enquiry-routed service tasks with shared audit receipts.")
    ET.fromstring(text)
    return text

if __name__ == '__main__':
    PATH.write_text(patch(PATH.read_text(encoding='utf-8')), encoding='utf-8', newline='\n')
    print('Patched formal BPMN; optional learning package stays unmodified.')
