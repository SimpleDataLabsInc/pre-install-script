#Constants
section_name = "iaas"
IaaS = "iaas"
Provisioner = "provisioner"
IsProvisioned = "provisioned"

AWS = "aws"
Azure = "azure"
GCP = "gcp"
OnPrem = "on-premise"
Terraform = "terraform"
Cloudformation = "cloudformation"
Console = "console"

#Documentation
iaasText = '''
Prophecy deploys to a Kubernetes environment. This can include Kubernetes in Public Cloud offerings such as AWS, Azure or GCP for public 
cloud. You can also choose to run the Kubernetes cluster on-premise like Open-shift or Tanzu. We can offer support to 
create managed K8s clusters on Azure and AWS via infrastructure as code using Terraform or Cloud Formation scripts. For GKE clusters, 
you will need to provision the GKE cluster from GCP console. We don't provide deployment scripts for GKE at this time. The cluster
that is created is expected to have 6 nodes which are m4.2xlarge in case of AWS EKS or Standard_DS4 in case of Azure AKS or 
n2-standard-8 in case of GKE.
'''

#Documentation - AWS
awsProvisionerText = '''
AWS EKS cluster can be deployed using console or via infrastructure as code options, namely Cloudformation or Terraform. 
'''

#Documentation - Azure
azureProvisionerText = '''
Azure AKS cluster can be deployed using console or via infrastructure as code options, namely Terraform. 
'''

#Documentation - GCP
gcpProvisionerText = '''
Google Cloud GKE cluster can be deployed using console. We dont support Infrastructure as Code option currently. 
'''

#Prompts
iaasPrompt = 'Where is the Kubernetes cluster running/planned to be run?'
isProvisionedPrompt = 'Is the Kubernetes cluster already provisioned?'
awsProvisionedPrompt = 'How would you like to deploy EKS?'
azureProvisionedPrompt = 'How would you like to deploy AKS?'
gcpProvisionedPrompt = 'How would you like to deploy GKE?'

#Options
iaasOptions = [
        AWS,
        Azure,
        GCP,
        OnPrem
]

awsProvisioners = [
        Terraform,
        Cloudformation,
        Console
]

azureProvisioners = [
        Terraform,
        Console
]

gcpProvisioners = [
        Console
]



