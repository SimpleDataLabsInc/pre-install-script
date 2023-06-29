import networking.consts as consts
import questionary


def IngressQuestions(ask=True):
    result = {}
    questions = [
        {
            'type': 'confirm',
            'name': consts.internetIngress,
            'message': consts.ingressnetworkingPromt
        },
    ]

    print(consts.ingressText)
    r = questionary.prompt(questions)
    result.update(r)

    if result[consts.internetIngress]:
        questions = [
            {
                'type': 'confirm',
                'name': consts.prophecyManagedDNSandCert,
                'message': consts.prophecyManagedDNSAndCertPromt
            },
        ]
        r = questionary.prompt(questions)
        result.update(r)
    return result


def EgressQuestions(ask=True):
    result = {}
    questions = [
        {
            'type': 'confirm',
            'name': consts.internetEgress,
            'message': consts.egressnetworkingPromt
        },
    ]

    print(consts.egressText)
    r = questionary.prompt(questions)
    result.update(r)
    return result


def AskNetworkingQuestions(cloud=None):
    result = {}
    print(consts.networkingText)

    ingResult = IngressQuestions()
    result['ingress'] = ingResult

    egResult = EgressQuestions()
    result['egress'] = egResult

    # use cloud to create questions pertaining to the cloud provider.

    return result
