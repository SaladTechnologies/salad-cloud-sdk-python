```python
from salad_cloud_sdk import SaladCloudSdk, Environment
from salad_cloud_sdk.models import CreateQueueJob

sdk = SaladCloudSdk(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

request_body = CreateQueueJob(
    input="",
    metadata={},
    webhook="webhook"
)

result = sdk.queues.create_queue_job(
    request_body=request_body,
    organization_name="jb7eyumc25lm4prwopvwr-1961g-m85nbqda3ufs",
    project_name="sn780t45z2tw4xt1b86w0clx6vkq-3",
    queue_name="sx811v32aty9s-ghx1hm2nw1mhgooidhvnhwadaqzuh19krhv62or5c"
)

print(result)

```
