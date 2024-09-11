```python
from salad_cloud_sdk import SaladCloudSdk, Environment

sdk = SaladCloudSdk(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

result = sdk.queues.list_queue_jobs(
    organization_name="caw0rzpy61pt90mpd37q4adxw-cgodal6rzqd6z1mw1si55p9gl6eb4zgl",
    project_name="d6wezcp8h3lm398az1xa5dcxhbrhwkxlx3lw0pdkr3o5",
    queue_name="jknzh2tjfasx0nsa3dsbwz4m6an9wbi5",
    page=1762690379,
    page_size=100
)

print(result)

```
