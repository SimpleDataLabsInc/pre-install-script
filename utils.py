import json, sys, os
from pathlib import Path
from typing import List
import questionary

state_file = Path(__file__).parent / "state.json"

def ask_load_state():
    if state_file.exists():
        result = questionary.select("Load previously-used values as defaults?", choices=["Yes", "No"]).ask()
        if result:
            if result == "No":
                result = questionary.select("Overwrite previously saved choices/values?", choices=["Yes", "No"]).ask()
                if result == "No":
                    sys.exit(1)
                else:
                    os.remove(state_file)
                    return {}
            else:
                return json.loads(open(state_file).read())
    return {}

def state_section(state, section_name: str|List):
    if not isinstance(section_name, List):
        section_name = [section_name]
    section = state
    for sn in section_name:
        sn = sn.lower()
        if sn in section:
            section = section[sn]
        else:
            section[sn] = {}
            section = section[sn]
    return section
    
def state_or_defaults(state, section_name: str|List, questions):
    section = state
    if not isinstance(section_name, List):
        section_name = [section_name]
    for sn in section_name:
        sn = sn.lower()
        if sn in section:
            section = section[sn]
        else:
            return questions
    for q in questions:
        if q["type"] == "print":
            continue
        if q["name"].lower() in section:
            q["default"] = section[q["name"].lower()]
    return questions

def update_and_persist(state, section_name: str|List, results, merge=False):
    section_name = section_name.lower()

    if not isinstance(section_name, List):
        section_name = [section_name]
    section = state
    parent_section = state
    for sn in section_name:
        sn = sn.lower()
        parent_section = section
        if sn in section:
            section = section[sn]
        else:
            section[sn] = {}
            section = section[sn]
    if not merge:
        section = {}
    for (k, v) in results.items():
        section[k.lower()] = v
    parent_section[section_name[-1]] = section

    with open(state_file, "w") as file:
        file.write(json.dumps(state))

def check_result_none(results):
    for v in results.values():
        if v is None:
def get_prophecy_version() -> Optional[str]:
    try:
        resp = requests.get("https://app.prophecy.io/athena/api/v1/cluster").json()
        current_version:str = resp["current_version"]["controlplane_version"]
        version_segments = current_version.split(".")
        major_version = ".".join(version_segments[:-1])
        return major_version + "-" + version_segments[-1]
    except Exception as e:
        breakpoint()
        return None