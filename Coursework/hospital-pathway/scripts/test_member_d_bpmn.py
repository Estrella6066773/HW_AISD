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

    def test_four_connected_worker_tasks(self):
        for task, source, target, kind in [
            ('NotifyCareChange', 'ClinicalChange', 'ChangeValid', 'notify-care-change'),
            ('AckAdminEnquiry', 'AdminEnquiry', 'EndAdminEnquiry', 'ack-enquiry-routed'),
            ('AckClinicalEnquiry', 'ClinicalEnquiry', 'EndClinicalEnquiry', 'ack-enquiry-routed'),
            ('AckFinanceEnquiry', 'FinanceEnquiry', 'EndFinanceEnquiry', 'ack-enquiry-routed')]:
            with self.subTest(task=task):
                self.assertIn(task, self.nodes)
                definition = self.nodes[task].find('b:extensionElements/z:taskDefinition', NS)
                self.assertEqual(definition.get('type'), kind)
                incoming = self.nodes[task].find('b:incoming', NS).text
                outgoing = self.nodes[task].find('b:outgoing', NS).text
                self.assertEqual(self.nodes[incoming].get('sourceRef'), source)
                self.assertEqual(self.nodes[outgoing].get('targetRef'), target)
                refs = [n.text for n in self.root.findall('.//b:lane/b:flowNodeRef', NS)]
                self.assertEqual(refs.count(task), 1)

    def test_sequence_flow_references_agree(self):
        for flow in self.root.findall('.//b:sequenceFlow', NS):
            source, target = self.nodes[flow.get('sourceRef')], self.nodes[flow.get('targetRef')]
            self.assertIn(flow.get('id'), [n.text for n in source.findall('b:outgoing', NS)])
            self.assertIn(flow.get('id'), [n.text for n in target.findall('b:incoming', NS)])

    def test_d_edges_have_visible_coordinates(self):
        for flow in ['Flow_51_D', 'Flow_25_D', 'Flow_26_D', 'Flow_27_D']:
            self.assertIn(flow + '_di', self.nodes)
            points = self.nodes[flow + '_di'].findall('w:waypoint', NS)
            self.assertGreaterEqual(len(points), 2)
            self.assertTrue(all(float(p.get('x')) > 0 and float(p.get('y')) > 0 for p in points))

    def test_job_types_have_java_workers(self):
        import re
        java = '\n'.join(p.read_text(encoding='utf-8') for p in (ROOT/'src/main/java').rglob('*.java'))
        registered = set(re.findall(r'@JobWorker\(type\s*=\s*"([^"]+)"', java))
        for task in self.root.findall('.//z:taskDefinition', NS):
            self.assertIn(task.get('type'), registered)

if __name__ == '__main__':
    unittest.main()
