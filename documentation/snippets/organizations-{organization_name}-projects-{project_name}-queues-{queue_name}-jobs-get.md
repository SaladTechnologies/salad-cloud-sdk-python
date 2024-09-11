```python
from salad_cloud_sdk import SaladCloudSdk, Environment

sdk = SaladCloudSdk(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

result = sdk.queues.list_queue_jobs(
    organization_name="jb7eyumc25lm4prwopvwr-1961g-m85nbqda3ufs",
    project_name="sn780t45z2tw4xt1b86w0clx6vkq-3",
    queue_name="sx811v32aty9s-ghx1hm2nw1mhgooidhvnhwadaqzuh19krhv62or5c",
    page=2110014563,
    page_size=23
)

print(result)

```
