# Constants
section_name = "ingress_controller"
IsIngressControllerPresent = "isIngressControllerPresent"
IsTLSLBTermination = "isTLSLBTermination"
TLSCertificateARN = "tlsCertificateARN"
IngressControllerType = "ingressControllerType"
IngressControllerClass = "ingressControllerClass"
Nginx = 'nginx'
Istio = 'istio'
Multiple  = 'multiple'

# Documentation
IngressControllerText = '''
The Nginx controller can be deployed to terminate TLS traffic at the controller or at the loadbalancer. The termination option 
and the certificate details can be selected using annotations. For AWS the loadbalancer can either be Classic or NLB. 
In the case of Azure,  we have to explicitly set the /healthz annotation for it to work correctly. We 
can also deploy Istio gateway and virtual service, though nginx is preferred by default. Nginx controller is deployed within 
a namespace with namespaced roles. If istio is deployed as service mesh then annotations need to be added to the ingress 
resources. 
'''

# Prompt
IngressControllerPromt = 'Is ingress controller installed in the cluster?'
IngressControllerTypePromt = 'What is the ingress controller installed? If istio is the deployed service mesh, please choose "multiple".'
IsTLSLBTerminationPromt = 'Is TLS terminated at the Loadbalancer?'
TLSCertificateARNPrompt = 'ARN of the TLS certificate to be terminated at the Loadbalancer?'
IngressControllerClassPrompt = 'What is the ingress controller class?'

# Options
IngressControllerTypeOptions = [
    Nginx,
    Istio,
    Multiple
]
