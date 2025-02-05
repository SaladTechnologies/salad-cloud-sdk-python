```python
from salad_cloud_sdk import SaladCloudSdk

sdk = SaladCloudSdk(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    timeout=10000
)

result = sdk.queues.list_queue_jobs(
    organization_name="w4s9eg1d2caksvlhpzmfccbh2v7dcapp3enb9gd2f4k4",
    project_name="yviu53s67ckwwnxsd-gfjsmuxcljdg4t1zzyn",
    queue_name="gpl2kuh4c67m3ae7qwlwipkdye-ad90-cq0up7kyr7vabeivb96iw",
    page=124963738,
    page_size=59
)

print(result)

```
