```python
from salad_cloud_sdk import SaladCloudSdk, Environment

sdk = SaladCloudSdk(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

result = sdk.container_groups.list_container_group_instances(
    organization_name="qaykn0y-5uryou3umpp3jva-wgcda23a08440n-ew1-qmamfu9iq2qrkhhpqc0",
    project_name="g57w5xgt26suu7z",
    container_group_name="oqechp8q9apf4t0-uai3sdl150pq-zx5u-9-kc8z4mp1vscg"
)

print(result)

```
