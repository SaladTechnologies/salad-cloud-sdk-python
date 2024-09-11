```python
from salad_cloud_sdk import SaladCloudSdk, Environment

sdk = SaladCloudSdk(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

result = sdk.organization_data.list_gpu_classes(organization_name="fxfk5b5evdjkgcjj9-97upvvnm6un-9x5riyyqnyl5q39cufb35o2nfpd3n8gv")

print(result)

```
