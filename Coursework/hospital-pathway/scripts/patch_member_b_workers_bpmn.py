# -*- coding: utf-8 -*-
"""Insert member-B service tasks only into hospital pathway BPMN."""
from __future__ import annotations

import re
import shutil
from pathlib import Path

COURSEWORK = Path(
    r"d:\OneDrive\MyProjects\HW_AISD\Coursework\hospital-pathway\bpmn"
    r"\W02_Hospital_All_Processes_Clean_Lines_Camunda8.bpmn"
)
ZH = Path(
    r"d:\OneDrive\MyProjects\HW_AISD\Ruby\hospital-pathway-zh-learn\bpmn"
    r"\W02_Hospital_All_Processes_Clean_Lines_Camunda8.bpmn"
)

TASKS = [
    (
        "CheckVisitSlot",
        "P3&#10;Check / reserve&#10;outpatient slot",
        "check-slot",
        "Member B worker type check-slot. After BookVisit form: mock external scheduling, write booking_slot; then VisitOutcome gateway.",
        1180,
        280,
    ),
    (
        "ReserveTreatmentSlot",
        "P6&#10;Reserve treatment&#10;slot / resources",
        "reserve-appointment",
        "Member B worker type reserve-appointment. After resources-ready gateway, before send-booking-confirmation; writes booking_slot confirmed.",
        2140,
        280,
    ),
    (
        "FlagResourceUnavailable",
        "P6&#10;Flag resource&#10;unavailable",
        "flag-resource-unavailable",
        "Member B worker type flag-resource-unavailable. Pending/retry path: write booking_slot pending + retry, then back to BookTreatment.",
        1980,
        400,
    ),
]


def service_task_xml(task_id: str, name: str, type_name: str, docs: str, incoming: str, outgoing: str) -> str:
    return f"""    <bpmn:serviceTask id="{task_id}" name="{name}">
      <bpmn:documentation>{docs}</bpmn:documentation>
      <bpmn:extensionElements>
        <zeebe:taskDefinition type="{type_name}" />
      </bpmn:extensionElements>
      <bpmn:incoming>{incoming}</bpmn:incoming>
      <bpmn:outgoing>{outgoing}</bpmn:outgoing>
    </bpmn:serviceTask>
"""


def shape_xml(task_id: str, x: float, y: float) -> str:
    return f"""      <bpmndi:BPMNShape id="{task_id}_di" bpmnElement="{task_id}" bioc:stroke="#263746" bioc:fill="#e8f5e9">
        <dc:Bounds x="{x}" y="{y}" width="100" height="80" />
      </bpmndi:BPMNShape>
"""


def edge_xml(flow_id: str) -> str:
    return f"""      <bpmndi:BPMNEdge id="{flow_id}_di" bpmnElement="{flow_id}" bioc:stroke="#2e7d32">
        <di:waypoint x="0" y="0" />
        <di:waypoint x="0" y="0" />
      </bpmndi:BPMNEdge>
"""


def patch(text: str) -> str:
    if 'id="CheckVisitSlot"' in text:
        print("Already patched; skip")
        return text

    replacements = [
        (
            '<bpmn:sequenceFlow id="Flow_06" sourceRef="BookVisit" targetRef="VisitOutcome" />',
            '<bpmn:sequenceFlow id="Flow_06" sourceRef="BookVisit" targetRef="CheckVisitSlot" />\n'
            '    <bpmn:sequenceFlow id="Flow_06b" sourceRef="CheckVisitSlot" targetRef="VisitOutcome" />',
        ),
        (
            '<bpmn:sequenceFlow id="Flow_16" name="Resources ready" sourceRef="TreatmentOutcome" targetRef="SendBookingConfirmation">',
            '<bpmn:sequenceFlow id="Flow_16" name="Resources ready" sourceRef="TreatmentOutcome" targetRef="ReserveTreatmentSlot">',
        ),
        (
            '<bpmn:sequenceFlow id="Flow_50" name="Pending / retry" sourceRef="TreatmentOutcome" targetRef="BookTreatment" />',
            '<bpmn:sequenceFlow id="Flow_50" name="Pending / retry" sourceRef="TreatmentOutcome" targetRef="FlagResourceUnavailable" />\n'
            '    <bpmn:sequenceFlow id="Flow_50b" sourceRef="FlagResourceUnavailable" targetRef="BookTreatment" />',
        ),
    ]
    for old, new in replacements:
        if old not in text:
            raise SystemExit(f"Missing fragment:\n{old}")
        text = text.replace(old, new, 1)

    m = re.search(
        r'(<bpmn:sequenceFlow id="Flow_16"[^>]*>[\s\S]*?</bpmn:sequenceFlow>)',
        text,
    )
    if not m:
        raise SystemExit("Flow_16 block not found")
    text = text.replace(
        m.group(1),
        m.group(1)
        + '\n    <bpmn:sequenceFlow id="Flow_16b" sourceRef="ReserveTreatmentSlot" targetRef="SendBookingConfirmation" />',
        1,
    )

    node_io = [
        (
            '<bpmn:exclusiveGateway id="VisitOutcome" name="Visit&#10;outcome?" default="Flow_35">\n'
            '      <bpmn:incoming>Flow_06</bpmn:incoming>',
            '<bpmn:exclusiveGateway id="VisitOutcome" name="Visit&#10;outcome?" default="Flow_35">\n'
            '      <bpmn:incoming>Flow_06b</bpmn:incoming>',
        ),
        (
            '      <bpmn:incoming>Flow_16</bpmn:incoming>\n'
            '      <bpmn:outgoing>Flow_66</bpmn:outgoing>\n'
            '    </bpmn:sendTask>',
            '      <bpmn:incoming>Flow_16b</bpmn:incoming>\n'
            '      <bpmn:outgoing>Flow_66</bpmn:outgoing>\n'
            '    </bpmn:sendTask>',
        ),
        (
            '      <bpmn:incoming>Flow_50</bpmn:incoming>\n'
            '      <bpmn:outgoing>Flow_15</bpmn:outgoing>\n'
            '    </bpmn:userTask>\n'
            '    <bpmn:exclusiveGateway id="TreatmentOutcome"',
            '      <bpmn:incoming>Flow_50b</bpmn:incoming>\n'
            '      <bpmn:outgoing>Flow_15</bpmn:outgoing>\n'
            '    </bpmn:userTask>\n'
            '    <bpmn:exclusiveGateway id="TreatmentOutcome"',
        ),
    ]
    for old, new in node_io:
        if old not in text:
            raise SystemExit(f"Missing node IO:\n{old[:160]}")
        text = text.replace(old, new, 1)

    task_defs = {
        "CheckVisitSlot": ("Flow_06", "Flow_06b"),
        "ReserveTreatmentSlot": ("Flow_16", "Flow_16b"),
        "FlagResourceUnavailable": ("Flow_50", "Flow_50b"),
    }
    blocks = []
    for task_id, name, type_name, docs, x, y in TASKS:
        inc, out = task_defs[task_id]
        blocks.append(service_task_xml(task_id, name, type_name, docs, inc, out))
    text = text.replace("  </bpmn:process>", "\n".join(blocks) + "  </bpmn:process>", 1)

    m = re.search(r'(<bpmn:lane id="Admin"[^>]*>)([\s\S]*?)(</bpmn:lane>)', text)
    if not m:
        raise SystemExit("Admin lane not found")
    refs = "".join(
        f"\n        <bpmn:flowNodeRef>{i}</bpmn:flowNodeRef>"
        for i, *_ in TASKS
    )
    text = text[: m.start(3)] + refs + "\n      " + text[m.start(3) :]

    shapes = [shape_xml(t[0], t[4], t[5]) for t in TASKS]
    edges = [edge_xml(f) for f in ("Flow_06b", "Flow_16b", "Flow_50b")]
    text = text.replace(
        "</bpmndi:BPMNPlane>",
        "\n".join(shapes + edges) + "\n    </bpmndi:BPMNPlane>",
        1,
    )

    old_guide = (
        "Payment uses a send task + payment-result message catch (Est pattern); "
        "booking confirmation uses a send task worker. Other external services / elapsed time stay simulated."
    )
    new_guide = (
        "Payment uses a send task + payment-result message catch (Est pattern); "
        "booking confirmation uses a send task worker. "
        "Member B added check-slot, reserve-appointment, flag-resource-unavailable service tasks. "
        "Other members' workers are not in this diagram yet."
    )
    if old_guide in text:
        text = text.replace(old_guide, new_guide, 1)

    return text


def main() -> None:
    patched = patch(COURSEWORK.read_text(encoding="utf-8"))
    COURSEWORK.write_text(patched, encoding="utf-8", newline="\n")
    print(f"Wrote {COURSEWORK}")
    if ZH.exists():
        shutil.copy2(COURSEWORK, ZH)
        print(f"Synced {ZH}")


if __name__ == "__main__":
    main()
