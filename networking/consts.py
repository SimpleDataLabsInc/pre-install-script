# Constants
internetIngress = "internetIngress"
internetEgress = 'internetEgress'
prophecyManagedDNSandCert = "prophecyManagedDNSandCertificate"

# Documentation
networkingText = '''
Prophecy expects ingress and egress to the K8s cluster enabled by default. This is to enable image pull from public image 
repositories, execution environment to push execution status and access to Prophecy UI from worksystem from outside the 
virtual network the Kubernetes cluster is deployed. Prophecy has a call back home endpoint used to push updates and upgrades 
which also requires access to the Internet.

Customers can choose to disable ingress and egress to the internet from the virtual network. This can be done by deploying
the Kubernetes cluster entirely in private subnets or adding restrictive access control.  In such scenarios, they have to ensure
that Prophecy images are available to the Kubernetes cluster. Prophecy should be 
accesible from the the workstations and the execution environment.
'''

ingressText = '''
Since Prophecy needs to be deployed using an nginx service backed by a domain, we require a loadbalancer for Ingress. The
loadbalancer IP/domain will need to be added to the DNS zone to enable DNS resolution. The customer is responsible to managing
the domain and DNS resolution. An option to leverage Prophecy managed domain and DNS resolution is available in case Internet
is accessible for DNS resolution. The customer can also choose to disable ingress from the Internet. For the same, the customer
can deploy an internal loadbalancer which will not have a public IP address. This can be deployed into private subnets and 
removes the requirement of having a public subnet. The customer is responsible to ensure connectivity to this loadbalancer 
from their workstation to access Prophecy UI and from the Spark environment to populate interims from pipeline execution.
'''

egressText = '''
To disable egress traffic to the internet for AWS EKS, they can choose to deploy the K8s clusters entirely in private subnets, 
without a public subnet with internet gateways. Azure VNets are connected to Internet by default. Internet egress needs to be 
disabled with network security rules associated with the subnet using the service tag Internet in the security rule. In case 
egress is disabled, Prophecy package will need to be explicitly provided to the Prophecy setup as it cannot pull from public 
maven repositories. This can be done by adding the packages explicitly to cloud bucket or hdfs and using that information in 
fabric.

Egress to the container registry is mandatory. If the image registry leveraged is Prophecy-managed public repository, then egress
to the Internet is mandatory. If the repository used is private and egress to Internet is disabled then the repository needs to 
be available within the private subnets via private endpoints. The customer has to ensure that the repository is reachable from 
instances deployed in the subnets. The authentication to the container registry can be using image pull secrets or instance roles.
'''

# Prompts
prophecyManagedDNSAndCertPromt = 'Do you want Prophecy to manage DNS and Certificate?'
ingressnetworkingPromt = 'Is traffic enabled from the Internet?'
egressnetworkingPromt = 'Is egress traffic disabled to the Internet?'

# Options
