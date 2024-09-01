```python
from salad_cloud_sdk import SaladCloudSdk, Environment

sdk = SaladCloudSdk(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

result = sdk.container_groups.get_container_group_instance(
    organization_name="r73buakrgl6y3rjdvhzythcjdr395d9kcqp4cb924r41g8h69zigf6pcd56q",
    project_name="ij2glutxyxjzu-kbkyf64swspzpifkfz1iqxdqeh723l4g1l4if4prvjrh",
    container_group_name="dy89w4q4lafvnap7fs4nkqpn7ls1z4okwf0mrkx5ngmb8o-bh3029krp8r4nbzi",
    container_group_instance_id="container_group_instance_id"
)

print(result)

```
