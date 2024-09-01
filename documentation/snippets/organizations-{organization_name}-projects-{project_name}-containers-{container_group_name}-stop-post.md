```python
from salad_cloud_sdk import SaladCloudSdk, Environment

sdk = SaladCloudSdk(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

result = sdk.container_groups.stop_container_group(
    organization_name="ohrlrstei115qknuq5qe4nwnj",
    project_name="mb04z87rwlzn3oww-l1t2vxu9r52mu126bs1owp2gdjes6jc5ch-ei3t5i",
    container_group_name="kda80pcf6aqiptmp19a40ofjecyop-nmf2k9mz2fveuxwp-0fo3gm2pxa"
)

print(result)

```
