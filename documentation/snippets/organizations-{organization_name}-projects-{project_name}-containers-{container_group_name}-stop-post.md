```python
from salad_cloud_sdk import SaladCloudSdk, Environment

sdk = SaladCloudSdk(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

result = sdk.container_groups.stop_container_group(
    organization_name="akn0y-5uryou3umpp3jva-wgcda23a08440n-ew1-q",
    project_name="im",
    container_group_name="d9iq2qrkhhpqc1ii57w5xgt26suu70u1qechp"
)

print(result)

```
