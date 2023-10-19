import iaas.consts as consts
import questionary
from  utils import state_or_defaults, update_and_persist, state_section


def IaasQuestions(iaas_state):
    # Question regarding the deployment environment
    questions = [
        {
            'type': 'print',
            'message': consts.iaasText
        },
        {
            'type': 'select',
            'name': consts.IaaS,
            'message': consts.iaasPrompt,
            'choices': consts.iaasOptions
        },
        {
            'type': 'confirm',
            'name' : consts.IsProvisioned,
            'message': consts.isProvisionedPrompt
        },
    ]
    questions = state_or_defaults(iaas_state, [], questions)
    return questionary.unsafe_prompt(questions)


def AWSIaaSQuestions(iaas_state):
    questions = [
        {
            'type': 'print',
            'message': consts.awsProvisionerText,
            'when': lambda x: (not iaas_state.get(consts.IsProvisioned, False)) and iaas_state[consts.IaaS] == consts.AWS
        },
        {
            'type': 'select',
            'name': consts.Provisioner,
            'message': consts.awsProvisionedPrompt,
            'choices': consts.awsProvisioners,
            'when': lambda x: (not iaas_state.get(consts.IsProvisioned, False)) and iaas_state[consts.IaaS] == consts.AWS
        },
    ]
    questions = state_or_defaults(iaas_state, [], questions)
    return questionary.unsafe_prompt(questions)

def AzureIaaSQuestions(iaas_state):
    questions = [
        { 
            'type': 'print',
            'message': consts.azureProvisionerText,
            'when': lambda x: (not iaas_state.get(consts.IsProvisioned, False)) and iaas_state[consts.IaaS] == consts.Azure
        },
        {
            'type': 'select',
            'name': consts.Provisioner,
            'message': consts.azureProvisionedPrompt,
            'choices': consts.azureProvisioners,
            'when': lambda x: (not iaas_state.get(consts.IsProvisioned, False)) and iaas_state[consts.IaaS] == consts.Azure
        },
    ]

    questions = state_or_defaults(iaas_state, [], questions)
    return questionary.unsafe_prompt(questions)


def GCPIaaSQuestions(iaas_state):
    questions = [
        { 
            'type': 'print',
            'message': consts.gcpProvisionerText,
            'when': lambda x: (not iaas_state.get(consts.IsProvisioned, False)) and iaas_state[consts.IaaS] == consts.GCP
        },
        {
            'type': 'select',
            'name': consts.Provisioner,
            'message': consts.gcpProvisionedPrompt,
            'choices': consts.gcpProvisioners,
            'when': lambda x: (not iaas_state.get(consts.IsProvisioned, False)) and iaas_state[consts.IaaS] == consts.GCP
        },
    ]


    questions = state_or_defaults(iaas_state, [], questions)
    return questionary.unsafe_prompt(questions)


def AskIaasQuestions(global_state):
    iaas_state = state_section(global_state, consts.section_name)
    iaas_state.update(IaasQuestions(iaas_state))
    iaas_state.update(AWSIaaSQuestions(iaas_state))
    iaas_state.update(AzureIaaSQuestions(iaas_state))
    iaas_state.update(GCPIaaSQuestions(iaas_state))
    update_and_persist(global_state, consts.section_name, iaas_state)


