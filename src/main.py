import kopf
import azure.identity
import azure.mgmt.network

network_client = NetworkManagementClient(
        credential=DefaultAzureCredential(),
        subscription_id=SUBSCRIPTION_ID
    )