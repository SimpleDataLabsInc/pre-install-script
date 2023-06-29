import iaas.consts as consts
import questionary

def IaasQuestions(ask=False):
    # Question regarding the deployment environment
    questions = [
        {
            'type': 'select',
            'name': consts.IaaS,
            'message': consts.iaasPrompt,
            'choices': consts.iaasOptions
        },
    ]
    if ask:
        print(consts.iaasText)
        return questions, consts.iaasText, questionary.prompt(questions)
    return questions, consts.iaasText, {}

def AWSIaaSQuestions(ask=False):
    questions = [
        {
            'type': 'select',
            'name': consts.Provisioner,
            'message': consts.awsProvisionerPromt,
            'choices': consts.awsProvisioners
        },
    ]
    if ask:
        print(consts.awsProvisionerText)
        return questions, consts.awsProvisionerText, questionary.prompt(questions)
    return questions, consts.awsProvisionerText, {}

def AzureIaaSQuestions(ask=False):
    questions = [
        {
            'type': 'select',
            'name': consts.Provisioner,
            'message': consts.azureProvisionerPromt,
            'choices': consts.azureProvisioners
        },
    ]
    if ask:
        print(consts.azureProvisionerText)
        return questions, consts.azureProvisionerText, questionary.prompt(questions)
    return questions, consts.azureProvisionerText, {}

def GCPIaaSQuestions(ask=False):
    questions = [
        {
            'type': 'select',
            'name': consts.Provisioner,
            'message': consts.gcpProvisionerPromt,
            'choices': consts.gcpProvisioners
        },
    ]
    if ask:
        print(consts.gcpProvisionerText)
        return questions, consts.gcpProvisionerText, questionary.prompt(questions)
    return questions, consts.gcpProvisionerText, {}

def AskIaasQuestions(ask=True):
    iaasQuestions = []
    (questions, promt, response) = IaasQuestions(ask)
    iaasQuestions.append((questions, promt, response))
    if response[consts.IaaS] == consts.AWS:
        q, p, r = AWSIaaSQuestions(ask)
        iaasQuestions.append((q, p, r))
        response[consts.AWS] = r
    elif response[consts.IaaS] == consts.Azure:
        q, p, r = AzureIaaSQuestions(ask)
        iaasQuestions.append((q, p, r))
        response[consts.Azure] = r
    elif response[consts.IaaS] == consts.GCP:
        q, p, r = GCPIaaSQuestions(ask)
        iaasQuestions.append((q, p, r))
        response[consts.GCP] = r
    else:
        None
    return response, iaasQuestions


