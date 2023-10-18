import questionary
from utils import ask_load_state
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

    helmCommand = "helm upgrade -i -n prophecy prophecy/prophecy-installer --version <prohecy-version>"

    try:
        state = ask_load_state()
        customerQuestions.AskCustomerQuestions(state)
        iaasQuestions.AskIaasQuestions(state)
        networkingQuestions.AskNetworkingQuestions(state)
        ingressControllerQuestions.AskIngressControllerQuestions(state)
        imgRegistryQuestions.AskImageRegistryQuestions(state)
        certQuestions.AskCertificateQuestions(state)
        logMonQuestions.AskLoggingAndMonitoringQuestions(state)

        helmCommand = helmCommand + " " + customerQuestions.GetFlagsFromResponse(state)
        helmCommand = helmCommand + " " + networkingQuestions.GetFlagsFromResponse(state)
        helmCommand = helmCommand + " " + ingressControllerQuestions.GetFlagsFromResponse(state)
        helmCommand = helmCommand + " " + imgRegistryQuestions.GetFlagsFromResponse(state)
        helmCommand = helmCommand + " " + certQuestions.GetFlagsFromResponse(state)
        helmCommand = helmCommand + " " + logMonQuestions.GetFlagsFromResponse(state)


    except KeyboardInterrupt:
        # your chance to handle the keyboard interrupt
        print("Cancelled by user")
    finally:
        #print(result)
        print("\nHelm command to run(cluster role required to run this command):")
        print(helmCommand)
