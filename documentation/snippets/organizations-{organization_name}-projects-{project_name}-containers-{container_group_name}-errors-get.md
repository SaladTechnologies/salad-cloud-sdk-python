```python
from salad_cloud_sdk import SaladCloudSdk, Environment

sdk = SaladCloudSdk(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

result = sdk.workload_errors.get_workload_errors(
    organization_name="x4hd7xmy53wgq8mpuy5k2wfbbzlhws5edt3sje",
    project_name="hug6abtk-ewjq1594j27m6u1whmqikj9f18pd",
    container_group_name="lq52i317o2r8pje-v4-ccp8q-329szw31h4fee236"
)

print(result)

```
