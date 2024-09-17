```python
from salad_cloud_sdk import SaladCloudSdk, Environment
from salad_cloud_sdk.models import UpdateContainerGroup

sdk = SaladCloudSdk(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

request_body = UpdateContainerGroup(
    display_name="HD",
    container={
        "image": "sit Ut aliqua consequat sunt",
        "resources": {
            "cpu": 13,
            "memory": 25675,
            "gpu_classes": [
                "gpu_classes"
            ],
            "storage_amount": 46594236814
        },
        "command": [
            "command"
        ],
        "priority": "high",
        "environment_variables": {},
        "logging": {
            "axiom": {
                "host": "voluptate exercitation culpa commodo",
                "api_token": "do amet non id",
                "dataset": "nostrud irure enim cillum"
            },
            "datadog": {
                "host": "officia dolore ex",
                "api_key": "nostrud proident dolor laborum",
                "tags": [
                    {
                        "name": "name",
                        "value": "value"
                    }
                ]
            },
            "new_relic": {
                "host": "esse",
                "ingestion_key": "Duis exercitation aliquip consectetur dolore"
            },
            "splunk": {
                "host": "incididunt dolore tempor",
                "token": "dolore laboris non amet"
            },
            "tcp": {
                "host": "est cupidatat",
                "port": 49463
            },
            "http": {
                "host": "laborum",
                "port": 12450,
                "user": "user",
                "password": "password",
                "path": "path",
                "format": "json",
                "headers": [
                    {
                        "name": "name",
                        "value": "value"
                    }
                ],
                "compression": "none"
            }
        },
        "registry_authentication": {
            "basic": {
                "username": "username",
                "password": "password"
            },
            "gcp_gcr": {
                "service_key": "service_key"
            },
            "aws_ecr": {
                "access_key_id": "access_key_id",
                "secret_access_key": "secret_access_key"
            },
            "docker_hub": {
                "username": "username",
                "personal_access_token": "personal_access_token"
            },
            "gcp_gar": {
                "service_key": "service_key"
            }
        }
    },
    replicas=244,
    country_codes=[
        "af"
    ],
    networking={
        "port": 55659
    },
    liveness_probe={
        "tcp": {
            "port": 30306
        },
        "http": {
            "path": "path",
            "port": 53006,
            "scheme": "http",
            "headers": [
                {
                    "name": "name",
                    "value": "value"
                }
            ]
        },
        "grpc": {
            "service": "service",
            "port": 6425
        },
        "exec_": {
            "command": [
                "command"
            ]
        },
        "initial_delay_seconds": 10,
        "period_seconds": 10,
        "timeout_seconds": 30,
        "success_threshold": 1,
        "failure_threshold": 3
    },
    readiness_probe={
        "tcp": {
            "port": 30306
        },
        "http": {
            "path": "path",
            "port": 53006,
            "scheme": "http",
            "headers": [
                {
                    "name": "name",
                    "value": "value"
                }
            ]
        },
        "grpc": {
            "service": "service",
            "port": 6425
        },
        "exec_": {
            "command": [
                "command"
            ]
        },
        "initial_delay_seconds": 5,
        "period_seconds": 1,
        "timeout_seconds": 1,
        "success_threshold": 1,
        "failure_threshold": 3
    },
    startup_probe={
        "tcp": {
            "port": 30306
        },
        "http": {
            "path": "path",
            "port": 53006,
            "scheme": "http",
            "headers": [
                {
                    "name": "name",
                    "value": "value"
                }
            ]
        },
        "grpc": {
            "service": "service",
            "port": 6425
        },
        "exec_": {
            "command": [
                "command"
            ]
        },
        "initial_delay_seconds": 0,
        "period_seconds": 3,
        "timeout_seconds": 10,
        "success_threshold": 2,
        "failure_threshold": 1200
    }
)

result = sdk.container_groups.update_container_group(
    request_body=request_body,
    organization_name="bvf99pxxwtres8z9zwaod8ipjrui87jps52s0izl8d-g9wqh8bjg",
    project_name="d2tyh4q9ni9h81tilnlnf5i-r38a8vv5h3",
    container_group_name="it5rb91fzs3spaw4grzs1ulr7"
)

print(result)

```
