import questionary
from utils import ask_load_state, get_prophecy_version
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

    try:
        state = ask_load_state()
        
        customerQuestions.AskCustomerQuestions(state)
        iaasQuestions.AskIaasQuestions(state)
        networkingQuestions.AskNetworkingQuestions(state)
        ingressControllerQuestions.AskIngressControllerQuestions(state)
        imgRegistryQuestions.AskImageRegistryQuestions(state)
        certQuestions.AskCertificateQuestions(state)
        logMonQuestions.AskLoggingAndMonitoringQuestions(state)

        print("*" * 20)
        prophecy_version = get_prophecy_version()
        if prophecy_version is None:
            questionary.print("Unable to load the current release version of Prophecy. Please contact the Prophecy engineer for the current version.", style="bold italic fg:darkred")
            prophecy_version = "<prophecy_version>"

        helmCommand = f"helm upgrade -i -n prophecy prophecy/prophecy-installer --version {prophecy_version}"

        helmCommand = helmCommand + " " + customerQuestions.GetFlagsFromResponse(state)
        helmCommand = helmCommand + " " + networkingQuestions.GetFlagsFromResponse(state)
        helmCommand = helmCommand + " " + ingressControllerQuestions.GetFlagsFromResponse(state)
        helmCommand = helmCommand + " " + imgRegistryQuestions.GetFlagsFromResponse(state)
        helmCommand = helmCommand + " " + certQuestions.GetFlagsFromResponse(state)
        helmCommand = helmCommand + " " + logMonQuestions.GetFlagsFromResponse(state)
        
        questionary.print("Please run this command to add the helm chart to your repository:")
        questionary.print("helm repo add prophecy https://prophecy-chart.s3.amazonaws.com", style="bold italic fg:ansigreen")
        questionary.print("\n\nHelm command to run to install Prophecy (cluster role required to run this command):")
        questionary.print(helmCommand, style="bold italic fg:ansigreen")


    except KeyboardInterrupt:
        # your chance to handle the keyboard interrupt
        print("Script cancelled by user")