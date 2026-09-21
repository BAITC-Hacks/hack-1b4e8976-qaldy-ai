import json
from pathlib import Path


file_path = Path(__file__).with_name("events.json")
events = json.loads(file_path.read_text(encoding="utf-8"))

critical_events = []

for event in events:
    if event.get("level") == "critical":
        critical_events.append(event)
        print(f"critical: {event['event']}")

print(f"критичных {len(critical_events)}")
