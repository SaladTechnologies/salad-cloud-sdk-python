```python
from salad_cloud_sdk import SaladCloudSdk
from salad_cloud_sdk.models import CreateQueue

sdk = SaladCloudSdk(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    timeout=10000
)

request_body = CreateQueue(
    name="name",
    display_name=" 6zTtRPsvOk",
    description="description"
)

result = sdk.queues.create_queue(
    request_body=request_body,
    organization_name="j-8a4o7jhy3jn2rdf012fi7ouno3mk-ax3",
    project_name="cajj5ajjquzeg-z3kvqxtnoxnlzhjhjt-8nawc40o0gqev9"
)

print(result)

```
