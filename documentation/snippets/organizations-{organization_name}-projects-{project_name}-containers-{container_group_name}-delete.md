```python
from salad_cloud_sdk import SaladCloudSdk

sdk = SaladCloudSdk(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    timeout=10000
)

result = sdk.container_groups.delete_container_group(
    organization_name="gv",
    project_name="mzx3s9b9-97wub7dm-r26ufpa46ncdw1l9j53dkso8adlnp",
    container_group_name="h1wsrgnjh8izdjsr6ircjk6xa1-pd"
)

print(result)

```
