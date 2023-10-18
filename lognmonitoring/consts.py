# Constants
section_name = "platform"
LoggingRequired = "loggingRequired"
MonitoringRequired = "monitoringRequired"
ClusterRole = "clusterrole"

# Documentation
LoggingText = '''
Optional installation features include the monitoring and logging sub-system. If you have a log aggregation service 
already installed in the cluster, you can proceed to not install the logging sub-system. If you choose to install the 
logging sub-system, Prophecy will install loki and (promtail/fluentbit) to pull logs from the containers in the namespace. 
You can then choose to install promtail as a daemonset(requires HostPath) or fluentbit as a sidecar to the services.
'''

MonitoringText = '''
Prometheus takes care of monitoring and collecting metrics. Grafana is used to display the dashboards. Promethues can be 
deployed using an operator which requires a cluster role or can be deployed in the namespace without a cluster role. The 
latter will have limited resources as metrics related to the Kubernetess cluster and node utilization are not pulled into 
Prometheus. Just the memory and CPU utilization from metric server is pulled in this case.
'''

# Promts
IsClusterRolePromt = "Is Prophecy and platform deployed using a cluster role?"
LoggingRequiredPrompt = "Should logging components be deployed?"
MonitoringRequiredPrompt = "Should monitoring components be deployed?"



