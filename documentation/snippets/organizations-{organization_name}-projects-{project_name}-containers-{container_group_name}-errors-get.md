```python
from salad_cloud_sdk import SaladCloudSdk, Environment

sdk = SaladCloudSdk(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

result = sdk.workload_errors.get_workload_errors(
    organization_name="u9szw31h4fee237cnffybnugpd7nbngs47jne2vq5j0d2m4f20",
    project_name="c5ozb1-4j-you0d7uftlpfgcaqa-2oc58y844m0ne",
    container_group_name="khlkkgda39h5upyur493wxwbxrj4x"
)

print(result)

```
