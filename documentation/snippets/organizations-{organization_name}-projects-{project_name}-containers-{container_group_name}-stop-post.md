```python
from salad_cloud_sdk import SaladCloudSdk, Environment

sdk = SaladCloudSdk(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

result = sdk.container_groups.stop_container_group(
    organization_name="c0o0gqev-mnkpy8af-s7rq68p2lenu8izbg09xnu6-fkv4dta4yd",
    project_name="rpi16e4ddle58fi8u9w2qgnsgj7cnci4p90a72aagy0f001ws1rwna83a3asuz",
    container_group_name="fd6ugn07m5xpcp89lefemdke05z4s9eg1d2caksvlhpzm"
)

print(result)

```
