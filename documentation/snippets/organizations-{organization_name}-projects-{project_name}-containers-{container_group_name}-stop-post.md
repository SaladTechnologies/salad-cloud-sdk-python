```python
from salad_cloud_sdk import SaladCloudSdk

sdk = SaladCloudSdk(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    timeout=10000
)

result = sdk.container_groups.stop_container_group(
    organization_name="q4wd2h8lvferfwvgjb47jpkwvr5-fbn",
    project_name="q-ie00beo1z3udfmoy56",
    container_group_name="lu5x4bztq-9mobin7qc1t3yiqpbz9g"
)

print(result)

```
