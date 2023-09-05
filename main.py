import questionary
import iaas.questions as iaasQuestions
import customer.questions as customerQuestions
import iaas.consts as iaasConsts
import ingress_controller.questions as ingressControllerQuestions
import image_repository.questions as imgRegistryQuestions
import networking.questions as networkingQuestions
import certificate.questions as certQuestions
import lognmonitoring.questions as logMonQuestions

if __name__ == '__main__':
    result = {}

    helmCommand = "helm upgrade -i -n prophecy"

    try:
        customerResponse = customerQuestions.AskCustomerQuestions()
        result = customerResponse
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

        helmCommand = helmCommand + " " + customerQuestions.GetFlagsFromResponse(customerResponse)
        helmCommand = helmCommand + " " + networkingQuestions.GetFlagsFromResponse(networkingResponse)
        helmCommand = helmCommand + " " + ingressControllerQuestions.GetFlagsFromResponse(ingressControllerResponse)
        helmCommand = helmCommand + " " + imgRegistryQuestions.GetFlagsFromResponse(imageRegistryResponse)
        helmCommand = helmCommand + " " + certQuestions.GetFlagsFromResponse(certResponse)
        helmCommand = helmCommand + " " + logMonQuestions.GetFlagsFromResponse(logMonitoringResponse)
        print(helmCommand)

    except KeyboardInterrupt:
        # your chance to handle the keyboard interrupt
        print("Cancelled by user")
    finally:
        print(result)


