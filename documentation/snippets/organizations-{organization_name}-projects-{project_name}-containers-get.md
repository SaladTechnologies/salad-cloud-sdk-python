```python
from salad_cloud_sdk import SaladCloudSdk, Environment

sdk = SaladCloudSdk(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

result = sdk.container_groups.list_container_groups(
    organization_name="apihl1d8o144-mf49qtwmztxy5e3c9v5qfb4l0g8j1lcj9-nh4i6dz2e7jf3",
    project_name="vjbveijqip5mysgje2g39crv0td0zupa8uxmseld79zsgkh7je6z"
)

print(result)

```
