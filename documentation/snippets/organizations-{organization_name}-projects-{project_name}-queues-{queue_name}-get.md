```python
from salad_cloud_sdk import SaladCloudSdk, Environment

sdk = SaladCloudSdk(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

result = sdk.queues.get_queue(
    organization_name="s6o2b",
    project_name="z-hsy9-rgx52jml2un9bjy3nn4rykiwe0vex",
    queue_name="q77lymon4qqm4j2k111l74jgrz9lbr76iko0hba99bukkai1ci9jgia3pwf8f-v"
)

print(result)

```
