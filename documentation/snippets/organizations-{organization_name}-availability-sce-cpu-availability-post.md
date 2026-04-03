```python
from salad_cloud_sdk import SaladCloudSdk
from salad_cloud_sdk.models import CpuAvailabilityPrototype

sdk = SaladCloudSdk(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    timeout=10000
)

request_body = CpuAvailabilityPrototype(
    country_codes=[
        "af"
    ],
    cpu=4,
    memory=8192,
    storage_amount=1000000000
)

result = sdk.organizations.get_cpu_availability(
    request_body=request_body,
    organization_name="acme-corp"
)

print(result)

```
