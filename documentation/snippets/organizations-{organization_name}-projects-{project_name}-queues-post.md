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
    name="qezkr2369ic05v6gnnllg6fhb-84kitkca0jy309-oh27ro0i5p95v4le",
    display_name="IR",
    description="consequat nulla magna minim ad"
)

result = sdk.queues.create_queue(
    request_body=request_body,
    organization_name="v2321xyb8mgby4oaz0nnednrzwspo5e",
    project_name="uqcz1p0g5ye7j57a"
)

print(result)

```
