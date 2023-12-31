import questionary
import ingress_controller.consts as consts
import iaas.consts as iaasConsts
from  utils import state_or_defaults, update_and_persist, state_section

def AskIngressControllerQuestions(global_state):
    ingress_state = state_section(global_state, consts.section_name)
    questions = [
        {
            'type': 'print',
            'message': consts.IngressControllerText
        },
        {
            'type': 'confirm',
            'name': consts.IsIngressControllerPresent,
            'message': consts.IngressControllerPromt
        },
        {
            'type': 'select',
            'name': consts.IngressControllerType,
            'message': consts.IngressControllerTypePromt,
            'choices': consts.IngressControllerTypeOptions,
            'when': lambda st: consts.IsIngressControllerPresent in st and st[consts.IsIngressControllerPresent] == True
        },
        {
            'type': 'text',
            'name': consts.IngressControllerClass,
            'message': consts.IngressControllerClassPrompt,
            'when': lambda st: consts.IngressControllerType in st and (st[consts.IngressControllerType] == consts.Nginx or st[consts.IngressControllerType] == consts.Multiple)
        },
        {
            'type': 'confirm',
            'name': consts.IsTLSLBTermination,
            'message': consts.IsTLSLBTerminationPromt,
            'when': lambda _st: state_section(global_state, iaasConsts.section_name)[iaasConsts.IaaS] == iaasConsts.AWS
        },
        {
            'type': 'text',
            'name': consts.TLSCertificateARN,
            'message': consts.TLSCertificateARNPrompt,
            'when': lambda st: consts.IsTLSLBTermination in st and st[consts.IsTLSLBTermination] == True
        }
    ]
    questions = state_or_defaults(ingress_state, [], questions)
    r = questionary.unsafe_prompt(questions)
    ingress_state.update(r)

    update_and_persist(global_state, consts.section_name, ingress_state)

def GetFlagsFromResponse(global_state):
    flags = ""
    ingress_state = state_section(global_state, consts.section_name)
    if ingress_state[consts.IsIngressControllerPresent]:
        flags = flags + " " + "--set platform.ingressNginx.enabled=false"
        if ingress_state[consts.IngressControllerType] == consts.Nginx or \
                ingress_state[consts.IngressControllerType] == consts.Multiple:
            flags = flags + " " + "--set global.ingressController.class="+ingress_state[consts.IngressControllerClass]
            flags = flags + " " + "--set global.ingressController.type="+consts.Nginx
        else:
            flags = flags + " " + "--set global.ingressController.type="+consts.Istio
    else:
        if (consts.IsTLSLBTermination in ingress_state.keys()) and (ingress_state[consts.IsTLSLBTermination]):
            flags = flags + " " + "--set platform.ingressNginx.enabled=true"
            flags = flags + " " + "--set platform.\"ingress-nginx\".controller.service.certificateARN="+ingress_state[consts.TLSCertificateARN]
    return flags
