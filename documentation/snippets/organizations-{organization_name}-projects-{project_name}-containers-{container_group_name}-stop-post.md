```python
from salad_cloud_sdk import SaladCloudSdk

sdk = SaladCloudSdk(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    timeout=10000
)

result = sdk.container_groups.stop_container_group(
    organization_name="acme-corp",
    project_name="dev-env",
    container_group_name="ecp1l-tkh9w1nv5mu1-9nad5ncpxu9ccs7p0whu98gpr-228"
)

print(result)

```
