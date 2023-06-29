import questionary
import iaas.questions as iaasQuestions

if __name__ == '__main__':
    response, questions = iaasQuestions.AskIaasQuestions()
    print(response)
