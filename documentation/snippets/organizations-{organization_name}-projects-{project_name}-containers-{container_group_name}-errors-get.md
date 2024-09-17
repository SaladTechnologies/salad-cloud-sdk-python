```python
from salad_cloud_sdk import SaladCloudSdk, Environment

sdk = SaladCloudSdk(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

result = sdk.workload_errors.get_workload_errors(
    organization_name="frtmwlnemnvjip49fx7paxg-h04cn",
    project_name="jqmz3mxb9iax5-m-abnacd2yjnwg6xlm838m",
    container_group_name="bxxj"
)

print(result)

```
