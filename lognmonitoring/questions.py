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
