import sys, string
import customer.consts as consts
import questionary
from  utils import state_or_defaults, update_and_persist, state_section

def CustomerQuestions(cust_state):
    # Question regarding the deployment environment
    questions = [
        {
            'type': 'text',
            'name': consts.customerName,
            'message': consts.CustomerNamePrompt,
            'filter': lambda x: x.lower().replace(string.punctuation, "_").replace(string.whitespace, "_")
        },
    ]

    questions = state_or_defaults(cust_state, [], questions)
    return questionary.prompt(questions)


def AskCustomerQuestions(global_state):
    customer_state = state_section(global_state, consts.section_name)
    
    response = CustomerQuestions(customer_state)
    update_and_persist(global_state, consts.section_name, response) 


def GetFlagsFromResponse(global_state):
    return "--set global.customer.name=" + global_state[consts.section_name][consts.customerName]
