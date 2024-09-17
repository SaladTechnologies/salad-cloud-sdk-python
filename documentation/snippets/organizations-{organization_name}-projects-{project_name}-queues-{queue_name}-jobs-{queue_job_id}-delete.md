```python
from salad_cloud_sdk import SaladCloudSdk, Environment

sdk = SaladCloudSdk(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

result = sdk.queues.delete_queue_job(
    organization_name="v8az1xa5dcxhbrhwkxlx3lw0pdkr3o6osknzh2tjfasx0nsa3dsbwz4m6an8",
    project_name="qi5",
    queue_name="vxffyxrcpjz02o68mnowwsycakrj2ndjibysiw7xvw8v11op7e4dq1ckmwu5v27",
    queue_job_id="queue_job_id"
)

print(result)

```
