import questionary

# Constants
section_name = "certificate"
CertSecret = "Certificate secret in namespace"
CertSecretVal = "secret"
CertManager = "Certificate provided by cert-manager"
CertManagerVal = "certManager"
ProphecyManaged = "Prophecy-managed DNS and certificate. (ACME protocol backed by Lets-Encrypt)"
ProphecyManagedVal = "prophecyManaged"
CertificateProvider = "certificateProvider"
RootURL             = "rootURL"
CertificateSecret = "certificateSecret"
CertificateIssuer = "certificateIssuer"

# Documentation
CertificateText = '''
For certificate management, you can choose to use one of three options: Prophecy-managed certificate and domain, a provided
certificate or leverage cert-manager already installed in the cluster. If Cert-manager is already installed in the cluster it can 
generate the certificates on-demand from ingress resources requiring TLS.
'''

# Prompts
CertificatePrompt = 'How do you wish to provide the certificate?'
CertificateSecretPrompt = 'What is the secret that stores the certificate?'
CertificateIssuerPrompt = 'What is the (cluster)issuer associated with cert-manager?'
RootURLPrompt = 'What is the root URL to access Prophecy?'

# Options
CertificateOptions = [
    questionary.Choice(ProphecyManaged, value=ProphecyManagedVal),
    questionary.Choice(CertManager, value=CertManagerVal),
    questionary.Choice(CertSecret, value=CertSecretVal),
]
