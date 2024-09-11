```python
from salad_cloud_sdk import SaladCloudSdk, Environment

sdk = SaladCloudSdk(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

result = sdk.queues.get_queue_job(
    organization_name="j-8sae7t0u7o0emyztq64o8ut710qtepjztx34mk6lruecseiyq06ab3ok5xr",
    project_name="eokxas9m7y892q4m5rifzmevenpg1vot8xgbal184sloim-c7555huym18dia9d",
    queue_name="zbvvpn2qgtohp",
    queue_job_id="queue_job_id"
)

print(result)

```
