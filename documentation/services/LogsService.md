# LogsService

A list of all methods in the `LogsService` service. Click on the method name to view detailed information about that method.

| Methods                                 | Description                                                                                                               |
| :-------------------------------------- | :------------------------------------------------------------------------------------------------------------------------ |
| [query_log_entries](#query_log_entries) | Retrieve a collection of _log entries_ for the _organization_ identified by `{organization_name}` matching the log query. |

## query_log_entries

Retrieve a collection of _log entries_ for the _organization_ identified by `{organization_name}` matching the log query.

- HTTP Method: `POST`
- Endpoint: `/organizations/{organization_name}/log-entries`

**Parameters**

| Name              | Type                                        | Required | Description                                                                                                                                                                                                                                         |
| :---------------- | :------------------------------------------ | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| request_body      | [LogEntryQuery](../models/LogEntryQuery.md) | ✅       | The request body.                                                                                                                                                                                                                                   |
| organization_name | str                                         | ✅       | Your organization name. This identifies the billing context for the API operation and represents a security boundary for SaladCloud resources. The organization must be created before using the API, and you must be a member of the organization. |

**Return Type**

`LogEntryCollection`

**Example Usage Code Snippet**

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
