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
            },
            {
                'type': 'text',
                'name': consts.RootURL,
                'message': consts.RootURLPrompt
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
            },
            {
                'type': 'text',
                'name': consts.RootURL,
                'message': consts.RootURLPrompt
            }
        ]
        r = questionary.prompt(questions)
        result.update(r)

    return result

def GetFlagsFromResponse(certResponse):
    flags = ""

    if certResponse[consts.CertificateProvider] == consts.CertSecretVal:
        flags = flags + " " + "--set global.prophecy.wildcardCert.name=" + certResponse[consts.CertificateSecret]
        flags = flags + " " + "--set global.prophecy.wildcardCert.useExternal=true"
        flags = flags + " " + "--set global.prophecy.rootUrl=" + certResponse[consts.RootURL]
    elif certResponse[consts.CertificateProvider] == consts.CertManagerVal:
        flags = flags + " " + "--set certManager.issuerName=" + certResponse[consts.CertificateIssuer]
        flags = flags + " " + "--set global.prophecy.wildcardCert.useExternal=true"
        flags = flags + " " + "--set global.prophecy.rootUrl=" + certResponse[consts.RootURL]
    elif certResponse[consts.CertificateProvider] == consts.ProphecyManagedVal:
        flags = flags + " " + "--set global.prophecy.wildcardCert.useExternal=false"
        flags = flags + " " + "--set global.prophecy.rootUrl=cloud.prophecy.io"

    return flags
