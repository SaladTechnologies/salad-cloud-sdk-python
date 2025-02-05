```python
from salad_cloud_sdk import SaladCloudSdk

sdk = SaladCloudSdk(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    timeout=10000
)

result = sdk.organization_data.list_gpu_classes(organization_name="ebg0vpngqc8hz5pxjwi7muqnmuuqsx3q3zm2hxkci5yv6khp3h5ljgqmbs")

print(result)

```
