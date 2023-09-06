import questionary
import ingress_controller.consts as consts
import iaas.consts as iaasConsts

def IngressControllerInstallQuestions(cloud=None):
    result = {}
    if cloud == iaasConsts.AWS:
        questions = [
            {
                'type': 'confirm',
                'name': consts.IsTLSLBTermination,
                'message': consts.IsTLSLBTerminationPromt
            }
        ]
        r = questionary.prompt(questions)
        result.update(r)

        if r[consts.IsTLSLBTermination]:
            questions = [
                {
                    'type': 'text',
                    'name': consts.TLSCertificateARN,
                    'message': consts.TLSCertificateARNPrompt
                }
            ]
            r = questionary.prompt(questions)
            result.update(r)
    return result

def AskIngressControllerQuestions(cloud=None):
    result = {}
    questions = [
        {
            'type': 'confirm',
            'name': consts.IsIngressControllerPresent,
            'message': consts.IngressControllerPromt
        },
    ]

    print(consts.IngressControllerText)
    r = questionary.prompt(questions)
    result.update(r)

    if r[consts.IsIngressControllerPresent]:
        questions = [
            {
                'type': 'select',
                'name': consts.IngressControllerType,
                'message': consts.IngressControllerTypePromt,
                'choices': consts.IngressControllerTypeOptions
            }
        ]
        r = questionary.prompt(questions)
        result.update(r)
        if r[consts.IngressControllerType] == consts.Nginx or \
            r[consts.IngressControllerType] == consts.Multiple:
            questions = [
                {
                    'type': 'text',
                    'name': consts.IngressControllerClass,
                    'message': consts.IngressControllerClassPrompt,
                }
            ]
            r = questionary.prompt(questions)
            result.update(r)
        return result

    result.update(IngressControllerInstallQuestions(cloud))
    return result

def GetFlagsFromResponse(ingressResponse):
    flags = ""

    if ingressResponse[consts.IsIngressControllerPresent]:
        flags = flags + " " + "--set platform.ingressNginx.enabled=false"
        if ingressResponse[consts.IngressControllerType] == consts.Nginx or \
                ingressResponse[consts.IngressControllerType] == consts.Multiple:
            flags = flags + " " + "--set global.ingressController.class="+ingressResponse[consts.IngressControllerClass]
            flags = flags + " " + "--set global.ingressController.type="+consts.Nginx
        else:
            flags = flags + " " + "--set global.ingressController.type="+consts.Istio
    else:
        if (consts.IsTLSLBTermination in ingressResponse.keys()) and (ingressResponse[consts.IsTLSLBTermination]):
            flags = flags + " " + "--set platform.ingressNginx.enabled=true"
            flags = flags + " " + "--set platform.\"ingress-nginx\".controller.service.certificateARN="+ingressResponse[consts.TLSCertificateARN]
    return flags
