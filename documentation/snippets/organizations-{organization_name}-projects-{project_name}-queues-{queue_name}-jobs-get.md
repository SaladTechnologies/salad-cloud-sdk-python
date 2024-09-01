```python
from salad_cloud_sdk import SaladCloudSdk, Environment

sdk = SaladCloudSdk(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

result = sdk.queues.list_queue_jobs(
    organization_name="s3artniqzrtb3xp",
    project_name="ghu49za-gk-63eofvgj1t0umc64usbu",
    queue_name="tz9a-29ellqfizdwuu79xr4e598",
    page=1660039363,
    page_size=20
)

print(result)

```
