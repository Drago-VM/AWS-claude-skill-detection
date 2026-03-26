import json
import os
from typing import List, Dict
import anthropic

# ==============================
# CONFIG
# ==============================

API_KEY = os.getenv("ANTHROPIC_API_KEY")
MODEL = "claude-sonnet-4-20250514"

client = anthropic.Anthropic(api_key=API_KEY)

# ✅ FIX: DEFINE BASE DIR
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# ==============================
# LOAD EVENTS
# ==============================

def load_events(file_path: str) -> List[Dict]:
    full_path = os.path.join(BASE_DIR, file_path)

    print("📂 Loading from:", full_path)  # debug

    with open(full_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    if isinstance(data, list):
        return data
    else:
        return [data]


# ==============================
# LOAD PROMPTS
# ==============================

def load_prompt(mode="triage"):
    prompt_path = os.path.join(BASE_DIR, "PROMPTS.md")

    print("📂 Loading prompt from:", prompt_path)  # debug

    with open(prompt_path, "r", encoding="utf-8") as f:
        content = f.read()

    if mode == "siem":
        return content.split("## 🔹 Advanced SIEM Analysis Prompt")[1]
    else:
        return content.split("## 🔹 Triage Prompt")[1]


# ==============================
# PROMPT BUILDER
# ==============================

def build_full_context(event, mode="triage"):
    prompt_template = load_prompt(mode)

    return f"""
{prompt_template}

Event:
{json.dumps(event, indent=2)}
"""


# ==============================
# CLAUDE CALL
# ==============================

def analyze_event(event, mode="triage"):
    prompt = build_full_context(event, mode)

    response = client.messages.create(
        model=MODEL,
        max_tokens=700,
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return response.content[0].text


# ==============================
# MAIN PIPELINE
# ==============================

def run(file_path: str):
    events = load_events(file_path)

    print(f"\n🔍 Loaded {len(events)} event(s)\n")

    for idx, event in enumerate(events, start=1):
        print(f"==============================")
        print(f"Event #{idx}")
        print(f"==============================")

        try:
            result = analyze_event(event, mode="siem")  # 🔥 use SIEM mode
            print(result)

        except Exception as e:
            print(f"❌ Error processing event: {e}")

        print("\n")


# ==============================
# ENTRY POINT
# ==============================

if __name__ == "__main__":
    run("data/sample_event.json")