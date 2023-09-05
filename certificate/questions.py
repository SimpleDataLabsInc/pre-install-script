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

def GetFlagsFromResponse(certResponse):
    flags = ""

    if certResponse[consts.CertificateProvider] == consts.CertSecretVal:
        flags = flags + " " + "--set global.prophecy.wildcardCert.name=" + certResponse[consts.CertificateSecret]
        flags = flags + " " + "--set global.prophecy.wildcardCert.useExternal=false"
    elif certResponse[consts.CertificateProvider] == consts.CertManagerVal:
        flags = flags + " " + "--set global.prophecy.wildcardCert.name=" + certResponse[consts.CertificateSecret]
        flags = flags + " " + "--set global.prophecy.wildcardCert.useExternal=false"
    elif certResponse[consts.CertificateProvider] == consts.ProphecyManagedVal:
        flags = flags + " " + "--set global.prophecy.wildcardCert.useExternal=true"

    return flags
