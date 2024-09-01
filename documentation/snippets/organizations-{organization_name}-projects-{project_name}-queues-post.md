```python
from salad_cloud_sdk import SaladCloudSdk, Environment
from salad_cloud_sdk.models import CreateQueue

sdk = SaladCloudSdk(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

request_body = CreateQueue(
    name="mh7g70vophyeafe4lxl6gmt4hizzzamvy3j90uelmwdmv",
    display_name="gEiIPCAh",
    description="dolor aliquip"
)

result = sdk.queues.create_queue(
    request_body=request_body,
    organization_name="gcmqvx5-larlezt8ks00ar9f8kfq524njjzfmn5dis4gk",
    project_name="x9ql9z"
)

print(result)

```
