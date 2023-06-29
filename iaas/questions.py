import iaas.consts as consts
import questionary


def IaasQuestions():
    # Question regarding the deployment environment
    result = {}
    questions = [
        {
            'type': 'select',
            'name': consts.IaaS,
            'message': consts.iaasPrompt,
            'choices': consts.iaasOptions
        },
        {
            'type': 'confirm',
            'name' : consts.IsProvisioned,
            'message': consts.isProvisionerPromt
        },
    ]

    print(consts.iaasText)
    result.update(questionary.prompt(questions))
    return result


def AWSIaaSQuestions():
    result = {}
    questions = [
        {
            'type': 'select',
            'name': consts.Provisioner,
            'message': consts.awsProvisionerPromt,
            'choices': consts.awsProvisioners
        },
    ]

    print(consts.awsProvisionerText)
    result.update(questionary.prompt(questions))
    return result


def AzureIaaSQuestions():
    result = {}
    questions = [
        {
            'type': 'select',
            'name': consts.Provisioner,
            'message': consts.azureProvisionerPromt,
            'choices': consts.azureProvisioners
        },
    ]

    print(consts.azureProvisionerText)
    result.update(questionary.prompt(questions))
    return result


def GCPIaaSQuestions():
    result = {}
    questions = [
        {
            'type': 'select',
            'name': consts.Provisioner,
            'message': consts.gcpProvisionerPromt,
            'choices': consts.gcpProvisioners
        },
    ]

    print(consts.gcpProvisionerText)
    result.update(questionary.prompt(questions))
    return result


def AskIaasQuestions():
    result = {}
    response = IaasQuestions()
    result.update(response)
    if consts.IsProvisioned in response.keys() and not response[consts.IsProvisioned]:
        if consts.IaaS in response.keys() and response[consts.IaaS] == consts.AWS:
            r = AWSIaaSQuestions()
            result.update(r)
        elif consts.IaaS in response.keys() and response[consts.IaaS] == consts.Azure:
            r = AzureIaaSQuestions()
            result.update(r)
        elif consts.IaaS in response.keys() and response[consts.IaaS] == consts.GCP:
            q, p, r = GCPIaaSQuestions()
            result.update(r)
        else:
            None
    return result


