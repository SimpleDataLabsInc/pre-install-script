import questionary
import lognmonitoring.consts as consts


def AskLoggingAndMonitoringQuestions(cloud=None):
    result = {}
    questions = [
        {
            'type': 'confirm',
            'name': consts.Namespaced,
            'message': consts.IsNamespacedPromt
        },
        {
            'type': 'confirm',
            'name': consts.LoggingRequired,
            'message': consts.LoggingRequiredPrompt
        },
        {
            'type': 'confirm',
            'name': consts.MonitoringRequired,
            'message': consts.MonitoringRequiredPrompt
        }
    ]


    print(consts.LoggingText)
    print(consts.MonitoringText)
    r = questionary.prompt(questions)
    result.update(r)
    return result

def GetFlagsFromResponse(response):
    flags = ""
    if response[consts.LoggingRequired]:
        flags = flags + " " + "--set platform.loki.enabled=true"
        flags = flags + " " + "--set platform.promtail.enabled=true"
    else
        flags = flags + " " + "--set platform.loki.enabled=false"
        flags = flags + " " + "--set platform.promtail.enabled=false"

    if response[consts.MonitoringRequired]:
        if response[consts.Namespaced]:
            flags = flags + " " + "--set platform.prometheusStandalone.enabled=true"
            flags = flags + " " + "--set platform.prometheusStack.enabled=false"
        else:
            flags = flags + " " + "--set platform.prometheusStandalone.enabled=false"
            flags = flags + " " + "--set platform.prometheusStack.enabled=true"
    else
        flags = flags + " " + "--set platform.prometheusStandalone.enabled=false"
        flags = flags + " " + "--set platform.prometheusStack.enabled=false"
