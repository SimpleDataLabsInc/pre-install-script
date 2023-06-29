#Constants
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
Customer can have or deploy K8s cluster in different environments. They can choose between AWS, Azure or GCP for public 
cloud. They can also choose to run the Kubernetes cluster on-premise like Open-shift or Tanzu. We can offer support to 
create managed K8s clusters on Azure and AWS via infrastructure as code using Terraform or Cloudformation. For GKE clusters, 
the customer will need to provision the GKE cluster from GCP console. We dont provide IaC scripts to help install. The cluster
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
isProvisionerPromt = 'Is the Kubernetes cluster already provisioned?'
awsProvisionerPromt = 'How would you like to deploy EKS?'
azureProvisionerPromt = 'How would you like to deploy AKS?'
gcpProvisionerPromt = 'How would you like to deploy GKE?'

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



