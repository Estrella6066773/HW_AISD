"""Check D's actual executable diagram, not only the patch script."""
from pathlib import Path
import unittest
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
NS = {'b': 'http://www.omg.org/spec/BPMN/20100524/MODEL',
      'z': 'http://camunda.org/schema/zeebe/1.0',
      'di': 'http://www.omg.org/spec/BPMN/20100524/DI',
      'w': 'http://www.omg.org/spec/DD/20100524/DI'}

class MemberDBpmnTest(unittest.TestCase):
    def setUp(self):
        self.root = ET.parse(ROOT / 'bpmn/W02_Hospital_All_Processes_Clean_Lines_Camunda8.bpmn').getroot()
        self.nodes = {n.get('id'): n for n in self.root.iter() if n.get('id')}

    def test_one_d_worker_in_change_path(self):
        task = self.nodes['NotifyCareChange']
        definition = task.find('b:extensionElements/z:taskDefinition', NS)
        self.assertEqual(definition.get('type'), 'notify-care-change')
        self.assertEqual(self.nodes['Flow_51'].get('sourceRef'), 'ClinicalChange')
        self.assertEqual(self.nodes['Flow_51'].get('targetRef'), 'NotifyCareChange')
        self.assertEqual(self.nodes['Flow_51_D'].get('targetRef'), 'ChangeValid')
        refs = [n.text for n in self.root.findall('.//b:lane/b:flowNodeRef', NS)]
        self.assertEqual(refs.count('NotifyCareChange'), 1)

    def test_sequence_flow_references_agree(self):
        for flow in self.root.findall('.//b:sequenceFlow', NS):
            source, target = self.nodes[flow.get('sourceRef')], self.nodes[flow.get('targetRef')]
            self.assertIn(flow.get('id'), [n.text for n in source.findall('b:outgoing', NS)])
            self.assertIn(flow.get('id'), [n.text for n in target.findall('b:incoming', NS)])

    def test_enquiries_end_after_human_response(self):
        for flow, source, target in [('Flow_25', 'AdminEnquiry', 'EndAdminEnquiry'),
                ('Flow_26', 'ClinicalEnquiry', 'EndClinicalEnquiry'),
                ('Flow_27', 'FinanceEnquiry', 'EndFinanceEnquiry')]:
            self.assertEqual(self.nodes[flow].get('sourceRef'), source)
            self.assertEqual(self.nodes[flow].get('targetRef'), target)
        self.assertFalse(any(t.get('type') == 'ack-enquiry-routed'
                             for t in self.root.findall('.//z:taskDefinition', NS)))

    def test_job_types_have_java_workers(self):
        import re
        java = '\n'.join(p.read_text(encoding='utf-8') for p in (ROOT/'src/main/java').rglob('*.java'))
        registered = set(re.findall(r'@JobWorker\(type\s*=\s*"([^"]+)"', java))
        for task in self.root.findall('.//z:taskDefinition', NS):
            self.assertIn(task.get('type'), registered)

if __name__ == '__main__':
    unittest.main()
