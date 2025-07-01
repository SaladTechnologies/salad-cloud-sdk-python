```python
from salad_cloud_sdk import SaladCloudSdk
from salad_cloud_sdk.models import LogEntryQuery

sdk = SaladCloudSdk(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    timeout=10000
)

request_body = LogEntryQuery(
    end_time="end_time",
    page_size=1,
    query="query",
    sort_order="desc",
    start_time="start_time"
)

result = sdk.logs.query_log_entries(
    request_body=request_body,
    organization_name="acme-corp"
)

print(result)

```
