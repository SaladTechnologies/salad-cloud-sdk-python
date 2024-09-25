```python
from salad_cloud_sdk import SaladCloudSdk, Environment

sdk = SaladCloudSdk(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

result = sdk.container_groups.get_container_group(
    organization_name="gq7z7dvdopv2czgde1zrufxgiv5tp-kncd4gfzda9ik-lw",
    project_name="xd-if9b1yvozs9trd4v0bll7qwslfehyhnfadnjp2w52gwrmz",
    container_group_name="ojjj5b9hbe2fr6f5t7j1htjaws1zx3r"
)

print(result)

```
