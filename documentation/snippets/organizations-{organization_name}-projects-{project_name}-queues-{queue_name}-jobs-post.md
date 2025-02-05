```python
from salad_cloud_sdk import SaladCloudSdk
from salad_cloud_sdk.models import CreateQueueJob

sdk = SaladCloudSdk(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    timeout=10000
)

request_body = CreateQueueJob(
    input="",
    metadata={},
    webhook="webhook"
)

result = sdk.queues.create_queue_job(
    request_body=request_body,
    organization_name="w4s9eg1d2caksvlhpzmfccbh2v7dcapp3enb9gd2f4k4",
    project_name="yviu53s67ckwwnxsd-gfjsmuxcljdg4t1zzyn",
    queue_name="gpl2kuh4c67m3ae7qwlwipkdye-ad90-cq0up7kyr7vabeivb96iw"
)

print(result)

```
