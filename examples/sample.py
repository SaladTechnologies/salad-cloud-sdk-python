from salad_cloud_sdk import SaladCloudSdk, Environment

sdk = SaladCloudSdk(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    base_url=Environment.DEFAULT.value,
    timeout=10000,
)

result = sdk.quotas.get_quotas(organization_name="yp5d1ln00phm36ghf3imgjjp6z9mn")

print(result)
