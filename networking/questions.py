import networking.consts as consts
import questionary
from  utils import state_or_defaults, update_and_persist, state_section

def IngressQuestions(net_state):
    questions = [
        { 
            'type': 'print',
            'message': consts.ingressText,
        },
        { 
            'type': 'print',
            'message': consts.egressText,
        },
        {
            'type': 'confirm',
            'name': consts.internetIngress,
            'message': consts.ingressnetworkingPromt
        },
    ]

    state_or_defaults(net_state, "ingress", questions)
    return questionary.unsafe_prompt(questions)

    # if result[consts.internetIngress]:
    #     questions = [
    #         {
    #             'type': 'confirm',
    #             'name': consts.prophecyManagedDNSandCert,
    #             'message': consts.prophecyManagedDNSAndCertPromt
    #         },
    #     ]
    #     r = questionary.unsafe_prompt(questions)
    #     result.update(r)


"""def EgressQuestions(ask=True):
    result = {}
    questions = [
        {
            'type': 'confirm',
            'name': consts.internetEgress,
            'message': consts.egressnetworkingPromt
        },
    ]

    print(consts.egressText)
    r = questionary.unsafe_prompt(questions)
    result.update(r)
    return result
"""


def AskNetworkingQuestions(global_state):
    questionary.print(consts.networkingText)

    net_state = state_section(global_state, consts.section_name)
    net_state["ingress"] = IngressQuestions(net_state)
    update_and_persist(global_state, consts.section_name, net_state)

    # egResult = EgressQuestions()
    # result['egress'] = egResult

    # use cloud to create questions pertaining to the cloud provider.


def GetFlagsFromResponse(global_state):
    flags = ""
    net_state = state_section(global_state, consts.section_name)
    if net_state['ingress'][consts.internetIngress]:
        # if networkingResponse['ingress'][consts.prophecyManagedDNSandCert]:
        #     flags = "--set global.prophecy.wildcardCert.useExternal=false"
        # else:
        #     flags = "--set global.prophecy.wildcardCert.useExternal=true"
        flags = flags + " " + "--set athena.isDarkCluster=false"
        flags = flags + " " + "--set athena.controlcenter.disabled=false"
    else:
        flags = flags + " " + "--set athena.isDarkCluster=true"
        flags = flags + " " + "--set athena.controlcenter.disabled=true"

    return flags
