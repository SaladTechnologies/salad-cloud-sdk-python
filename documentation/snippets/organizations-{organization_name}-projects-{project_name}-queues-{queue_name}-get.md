```python
from salad_cloud_sdk import SaladCloudSdk, Environment

sdk = SaladCloudSdk(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

result = sdk.queues.get_queue(
    organization_name="t6u-51xnolzq0i9u27d9qsg6qsygfges6",
    project_name="g1tktkoepudefqkf47dv60kqzd3q1wo8z4ukbuijty",
    queue_name="ff3kysrgbao"
)

print(result)

```
