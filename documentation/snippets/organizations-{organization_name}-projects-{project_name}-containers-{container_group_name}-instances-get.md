```python
from salad_cloud_sdk import SaladCloudSdk

sdk = SaladCloudSdk(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    timeout=10000
)

result = sdk.container_groups.list_container_group_instances(
    organization_name="uc-y08qjw2plboeezjs7bj1g04wskczv4ux-1drauitzdwr9qeggqavmvwbn",
    project_name="ffvu3ece9yhhnzdc345revreliict4850bfesqznhccmp",
    container_group_name="v4osb2nms0izyhne-3b96ou31bnuzrpa533bnuvidlz4opbb766b"
)

print(result)

```
