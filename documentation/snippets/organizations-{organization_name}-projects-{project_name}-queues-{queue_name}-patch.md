```python
from salad_cloud_sdk import SaladCloudSdk, Environment
from salad_cloud_sdk.models import UpdateQueue

sdk = SaladCloudSdk(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

request_body = UpdateQueue(
    display_name="MoX4JPAm1M.",
    description="in ea minim labore"
)

result = sdk.queues.update_queue(
    request_body=request_body,
    organization_name="s6o2b",
    project_name="z-hsy9-rgx52jml2un9bjy3nn4rykiwe0vex",
    queue_name="q77lymon4qqm4j2k111l74jgrz9lbr76iko0hba99bukkai1ci9jgia3pwf8f-v"
)

print(result)

```
