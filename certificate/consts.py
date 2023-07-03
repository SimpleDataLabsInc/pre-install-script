import questionary

# Constants
CertSecret = "Certificate secret in namespace"
CertSecretVal = "secret"
CertManager = "Certificate provided by cert-manager"
CertManagerVal = "certManager"
ProphecyManaged = "Prophecy managed DNS and certificate.(ACME protocol backed by Lets-Encrypt)"
ProphecyManagedVal = "prophecyManaged"
CertificateProvider = "certificateProvider"
CertificateSecret = "certificateSecret"
CertificateIssuer = "certificateIssuer"

# Documentation
CertificateText = '''
For certificate management, the customer choose to use between prophecy managed certificate and domain, customer provided
certificate or leverage cert-manager already installed in the cluster. Cert-manager already installed in the cluster can 
generate the certificates on demand from ingress resources requiring TLS.
'''

# Prompts
CertificatePrompt = 'How do you wish to provide the certificate?'
CertificateSecretPrompt = 'What is the secret that stores the certificate?'
CertificateIssuerPrompt = 'What is the (cluster)issuer associated with cert-manager?'

# Options
CertificateOptions = [
    questionary.Choice(ProphecyManaged, value=ProphecyManagedVal),
    questionary.Choice(CertManager, value=CertManagerVal),
    questionary.Choice(CertSecret, value=CertSecretVal),
]
