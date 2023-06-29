import questionary
import iaas.questions as iaasQuestions
import iaas.consts as iaasConsts
import networking.questions as networkingQuestions

if __name__ == '__main__':
    result = {}
    try:
        response = iaasQuestions.AskIaasQuestions()
        result['cloud'] = response
        response = networkingQuestions.AskNetworkingQuestions(response[iaasConsts.IaaS])
        result['networking'] = response
    except KeyboardInterrupt:
        # your chance to handle the keyboard interrupt
        print("Cancelled by user")
    finally:
        print(result)
