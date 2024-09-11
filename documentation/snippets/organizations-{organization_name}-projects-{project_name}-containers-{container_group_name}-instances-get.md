```python
from salad_cloud_sdk import SaladCloudSdk, Environment

sdk = SaladCloudSdk(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

result = sdk.container_groups.list_container_group_instances(
    organization_name="x9apf4t0-uai3sdl150pq-zx5u-9-j",
    project_name="bz4mp1vscg2wjxeuemfxcv-ue7tm-bp-8n1hvh8fnv7mx285iuup332rpaf",
    container_group_name="shaiuchf2q8kkg3dsgwkty0ap7uq2b1ex4akekgljza8i9375vs22d352n"
)

print(result)

```
