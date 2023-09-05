import customer.consts as consts
import questionary


def CustomerQuestions():
    # Question regarding the deployment environment
    result = {}
    questions = [
        {
            'type': 'text',
            'name': consts.customerName,
            'message': consts.CustomerNamePrompt
        },
    ]

    result.update(questionary.prompt(questions))
    return result


def AskCustomerQuestions():
    result = {}
    response = CustomerQuestions()
    result.update(response)
    return result


def GetFlagsFromResponse(customerResponse):
    return "--set global.customer.name=" + customerResponse[consts.customerName]
