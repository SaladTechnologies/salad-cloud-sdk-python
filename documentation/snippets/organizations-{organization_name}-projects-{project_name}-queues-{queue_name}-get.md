```python
from salad_cloud_sdk import SaladCloudSdk, Environment

sdk = SaladCloudSdk(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

result = sdk.queues.get_queue(
    organization_name="bb5wprcvb9628akhug9lnd2",
    project_name="bw-4bdb9jsi-f1xex70mdgjf5n-5ua-e28xyu9ujbls0vsy",
    queue_name="wilo12xl52y9c178cmdya6ykpby-hunb0b6s7s2l"
)

print(result)

```
