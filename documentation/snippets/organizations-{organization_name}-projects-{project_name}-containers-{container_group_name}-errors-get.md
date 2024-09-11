```python
from salad_cloud_sdk import SaladCloudSdk, Environment

sdk = SaladCloudSdk(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

result = sdk.workload_errors.get_workload_errors(
    organization_name="vfx7paxg-h04conuqmz3mxb9iax5-m-abnacd2yjnwg6xlm838mbbxxjo-h52",
    project_name="sonqyj90ubo8reysxpqq7xwg32lxlhjn2dh8g4ria4k5s",
    container_group_name="dzd-3pdeog5yu4egwx3g9mbcmuyxmxx"
)

print(result)

```
