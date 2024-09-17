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
    name="v4lefmr06ujx04v2hu68mhyreae4gnbvwp2w52",
    display_name="JtVGrm",
    description="ipsum sunt Duis cillum quis"
)

result = sdk.queues.create_queue(
    request_body=request_body,
    organization_name="cmzshp5r2321xyb8mgby4oaz0nnednrzwspo5e2iqcz1p0g5ye",
    project_name="x57abcm33wd-ap53y"
)

print(result)

```
