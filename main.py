import questionary
import iaas.questions as iaasQuestions
import iaas.consts as iaasConsts
import ingress_controller.questions as ingressControllerQuestions
import networking.questions as networkingQuestions

if __name__ == '__main__':
    result = {}
    try:
        iaasResponse = iaasQuestions.AskIaasQuestions()
        result['cloud'] = iaasResponse
        networkingResponse = networkingQuestions.AskNetworkingQuestions(iaasResponse[iaasConsts.IaaS])
        result['networking'] = networkingResponse
        ingressControllerResponse = ingressControllerQuestions.AskIngressControllerQuestions(iaasResponse[iaasConsts.IaaS])
        result['ingressController'] = ingressControllerResponse
    except KeyboardInterrupt:
        # your chance to handle the keyboard interrupt
        print("Cancelled by user")
    finally:
        print(result)
