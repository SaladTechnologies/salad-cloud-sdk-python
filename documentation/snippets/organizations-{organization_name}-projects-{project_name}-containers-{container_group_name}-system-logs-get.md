```python
from salad_cloud_sdk import SaladCloudSdk

sdk = SaladCloudSdk(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    timeout=10000
)

result = sdk.system_logs.get_system_logs(
    organization_name="v4jjl15umljlf7j3ipq777p3m4a5kvcr49scpbvkt8frzckadjfuwa2t",
    project_name="c89a2l4l-74ilyrrugrnir4d3p-nljpe2j7j0fvf",
    container_group_name="sz9np2a"
)

print(result)

```
