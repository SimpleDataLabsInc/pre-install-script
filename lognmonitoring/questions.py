import questionary
import lognmonitoring.consts as consts
from  utils import state_or_defaults, update_and_persist, state_section

def AskLoggingAndMonitoringQuestions(global_state):
    log_state = state_section(global_state, consts.section_name)
    questions = [
        {
            'type': 'confirm',
            'name': consts.ClusterRole,
            'message': consts.IsClusterRolePromt
        },
        {
            'type': 'print',
            'message': consts.LoggingText
        },
        {
            'type': 'confirm',
            'name': consts.LoggingRequired,
            'message': consts.LoggingRequiredPrompt
        },
        {
            'type': 'print',
            'message': consts.MonitoringText
        },
        {
            'type': 'confirm',
            'name': consts.MonitoringRequired,
            'message': consts.MonitoringRequiredPrompt
        }
    ]
    questions = state_or_defaults(log_state, [], questions)
    r = questionary.unsafe_prompt(questions)
    update_and_persist(global_state, consts.section_name, r)

def GetFlagsFromResponse(global_state):
    flags = ""
    log_state = state_section(global_state, consts.section_name)
    if log_state[consts.LoggingRequired]:
        flags = flags + " " + "--set platform.loki.enabled=true"
        flags = flags + " " + "--set platform.promtail.enabled=true"
    else:
        flags = flags + " " + "--set platform.loki.enabled=false"
        flags = flags + " " + "--set platform.promtail.enabled=false"

    if log_state[consts.MonitoringRequired]:
        if not log_state[consts.ClusterRole]:
            flags = flags + " " + "--set platform.prometheusStandalone.enabled=true"
            flags = flags + " " + "--set platform.prometheusStack.enabled=false"
        else:
            flags = flags + " " + "--set platform.prometheusStandalone.enabled=false"
            flags = flags + " " + "--set platform.prometheusStack.enabled=true"
    else:
        flags = flags + " " + "--set platform.prometheusStandalone.enabled=false"
        flags = flags + " " + "--set platform.prometheusStack.enabled=false"

    return flags
