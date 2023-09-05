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

    # if result[consts.internetIngress]:
    #     questions = [
    #         {
    #             'type': 'confirm',
    #             'name': consts.prophecyManagedDNSandCert,
    #             'message': consts.prophecyManagedDNSAndCertPromt
    #         },
    #     ]
    #     r = questionary.prompt(questions)
    #     result.update(r)
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


def GetFlagsFromResponse(networkingResponse):
    flags = ""

    if networkingResponse['ingress'][consts.internetIngress]:
        # if networkingResponse['ingress'][consts.prophecyManagedDNSandCert]:
        #     flags = "--set global.prophecy.wildcardCert.useExternal=false"
        # else:
        #     flags = "--set global.prophecy.wildcardCert.useExternal=true"
        flags = flags + " " + "--set athena.isDarkCluster=false"
    else:
        flags = flags + " " + "--set athena.isDarkCluster=true"

    if networkingResponse['egress'][consts.internetEgress]:
        flags = flags + " " + "--set athena.controlcenter.disabled=false"
    else:
        flags = flags + " " + "--set athena.controlcenter.disabled=true"

    return flags
