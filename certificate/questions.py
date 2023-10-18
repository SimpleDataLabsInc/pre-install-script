import certificate.consts as consts
import questionary
from  utils import state_or_defaults, update_and_persist, state_section, check_result_none

def AskCertificateQuestions(global_state):
    cert_state = state_section(global_state, consts.section_name)
    questions = [
        {
            'type': 'print',
            'message': consts.CertificateText
        },
        {
            'type': 'select',
            'name': consts.CertificateProvider,
            'message': consts.CertificatePrompt,
            'choices': consts.CertificateOptions
        },
        {
            'type': 'text',
            'name': consts.CertificateSecret,
            'message': consts.CertificateSecretPrompt,
            'when': lambda st: st[consts.CertificateProvider] == consts.CertSecretVal
        },
        {
            'type': 'text',
            'name': consts.RootURL,
            'message': consts.RootURLPrompt,
            'when': lambda st: st[consts.CertificateProvider] == consts.CertSecretVal
        },
        {
            'type': 'text',
            'name': consts.CertificateIssuer,
            'message': consts.CertificateIssuerPrompt,
            'when': lambda st: st[consts.CertificateProvider] == consts.CertManagerVal
        },
        {
            'type': 'text',
            'name': consts.RootURL,
            'message': consts.RootURLPrompt,
            'when': lambda st: st[consts.CertificateProvider] == consts.CertManagerVal
        }
    ]
    questions = state_or_defaults(cert_state, [], questions)
    r = questionary.unsafe_prompt(questions)
    update_and_persist(global_state, consts.section_name, r)

def GetFlagsFromResponse(global_state):
    flags = ""
    cert_state = state_section(global_state, consts.section_name)
    if cert_state[consts.CertificateProvider] == consts.CertSecretVal:
        flags = flags + " " + "--set global.prophecy.wildcardCert.name=" + cert_state[consts.CertificateSecret]
        flags = flags + " " + "--set global.prophecy.wildcardCert.useExternal=true"
        flags = flags + " " + "--set global.prophecy.rootUrl=" + cert_state[consts.RootURL]
    elif cert_state[consts.CertificateProvider] == consts.CertManagerVal:
        flags = flags + " " + "--set certManager.issuerName=" + cert_state[consts.CertificateIssuer]
        flags = flags + " " + "--set global.prophecy.wildcardCert.useExternal=true"
        flags = flags + " " + "--set global.prophecy.rootUrl=" + cert_state[consts.RootURL]
    elif cert_state[consts.CertificateProvider] == consts.ProphecyManagedVal:
        flags = flags + " " + "--set global.prophecy.wildcardCert.useExternal=false"
        flags = flags + " " + "--set global.prophecy.rootUrl=cloud.prophecy.io"

    return flags
