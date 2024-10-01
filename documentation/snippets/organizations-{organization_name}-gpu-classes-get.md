```python
from salad_cloud_sdk import SaladCloudSdk, Environment

sdk = SaladCloudSdk(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

result = sdk.organization_data.list_gpu_classes(organization_name="w9qttkrqdm5b9xdre4met9ioqxf-a3suyfz4tkhle7s9-vpaj7uvpj")

print(result)

```
