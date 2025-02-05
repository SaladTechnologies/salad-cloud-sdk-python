```python
from salad_cloud_sdk import SaladCloudSdk

sdk = SaladCloudSdk(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    timeout=10000
)

result = sdk.container_groups.get_container_group_instance(
    organization_name="anydcnlz73jmjvonbkspbimao7ket3x337pq2ik7t3po81gf",
    project_name="y5oxeppfjrdtivc0588wz3z920dm3uvrx5hqx52s2sk49-8xwul52o126l",
    container_group_name="k-1--kq611igeuz3",
    container_group_instance_id="container_group_instance_id"
)

print(result)

```
