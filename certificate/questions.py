import certificate.consts as consts
import questionary


def AskCertificateQuestions(cloud=None):
    result = {}
    questions = [
        {
            'type': 'select',
            'name': consts.CertificateProvider,
            'message': consts.CertificatePrompt,
            'choices': consts.CertificateOptions
        },
    ]
    print(consts.CertificateText)
    r = questionary.prompt(questions)
    result.update(r)

    if r[consts.CertificateProvider] == consts.CertSecretVal:
        questions = [
            {
                'type': 'text',
                'name': consts.CertificateSecret,
                'message': consts.CertificateSecretPrompt
            }
        ]
        r = questionary.prompt(questions)
        result.update(r)

    elif r[consts.CertificateProvider] == consts.CertManagerVal:
        questions = [
            {
                'type': 'text',
                'name': consts.CertificateIssuer,
                'message': consts.CertificateIssuerPrompt
            }
        ]
        r = questionary.prompt(questions)
        result.update(r)

    return result

