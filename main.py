import questionary
import iaas.questions as iaasQuestions
import iaas.consts as iaasConsts
import ingress_controller.questions as ingressControllerQuestions
import image_repository.questions as imgRegistryQuestions
import networking.questions as networkingQuestions
import certificate.questions as certQuestions
import lognmonitoring.questions as logMonQuestions

if __name__ == '__main__':
    result = {}
    try:
        iaasResponse = iaasQuestions.AskIaasQuestions()
        result['cloud'] = iaasResponse
        networkingResponse = networkingQuestions.AskNetworkingQuestions(iaasResponse[iaasConsts.IaaS])
        result['networking'] = networkingResponse
        ingressControllerResponse = ingressControllerQuestions.AskIngressControllerQuestions(iaasResponse[iaasConsts.IaaS])
        result['ingressController'] = ingressControllerResponse
        imageRegistryResponse = imgRegistryQuestions.AskImageRegistryQuestions()
        result['imageRegistry'] = imageRegistryResponse
        certResponse = certQuestions.AskCertificateQuestions()
        result['certificate'] = certResponse
        logMonitoringResponse = logMonQuestions.AskLoggingAndMonitoringQuestions()
        result['platform'] = logMonitoringResponse
    except KeyboardInterrupt:
        # your chance to handle the keyboard interrupt
        print("Cancelled by user")
    finally:
        print(result)
