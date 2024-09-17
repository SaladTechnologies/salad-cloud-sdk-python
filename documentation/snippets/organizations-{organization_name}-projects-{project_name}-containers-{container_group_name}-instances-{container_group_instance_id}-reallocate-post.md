```python
from salad_cloud_sdk import SaladCloudSdk, Environment

sdk = SaladCloudSdk(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

result = sdk.container_groups.reallocate_container_group_instance(
    organization_name="mmcbsf7w3wlau11f5g2zdmdpxhq",
    project_name="ehv7x3dhck87lv8-z-wg2fzk8ea2roe6yryt0-t1885d",
    container_group_name="k62ut0igkfak4jbmum3tb50owd1q7z43vbdm-ym2fjvtwvm3kubeomi0c0",
    container_group_instance_id="container_group_instance_id"
)

print(result)

```
