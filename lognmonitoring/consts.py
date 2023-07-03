# Constants
LoggingRequired = "loggingRequired"
MonitoringRequired = "monitoringRequired"
Namespaced = "namespaced"

# Documentation
LoggingText = '''
Optional installation features include the monitoring and logging sub-system. If the customer has a log aggregation service 
already installed in the cluster, they can proceed to not install the logging sub-system. If they choose to install the 
logging sub-system, Prophecy will install loki and (promtail/fluentbit) to pull logs from the containers in the namespace. 
Customers can choose to install promtail as a daemonset(requires HostPath) or fluentbit as a sidecar to the services.
'''

MonitoringText = '''
Prometheus takes care of monitoring and collecting metrics. Grafana is used to display the dashboards. Promethues can be 
deployed using an operator which requires a cluster role or can be deployed in the namespace without a cluster role. The 
latter will have limited resources as metrics related to the Kubernetess cluster and node utilization are not pulled into 
Prometheus. Just the memory and cpu utilization from metric server is pulled in this case.
'''

# Promts
IsNamespacedPromt = "Is Prophecy and platform deployed with a namespaced role or cluster role?"
LoggingRequiredPrompt = "Should logging components be deployed?"
MonitoringRequiredPrompt = "Should monitoring components be deployed?"



