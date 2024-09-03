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
    display_name="UtDi9VD ZS",
    container={
        "image": "culpa nulla eu non",
        "resources": {
            "cpu": 11,
            "memory": 1557,
            "gpu_classes": [
                "gpu_classes"
            ],
            "storage_amount": 40250176413
        },
        "command": [
            "command"
        ],
        "priority": "high",
        "environment_variables": {},
        "logging": {
            "axiom": {
                "host": "nisi et veniam",
                "api_token": "Lorem esse dolor",
                "dataset": "et commodo Duis"
            },
            "datadog": {
                "host": "veniam deserunt sunt dolore",
                "api_key": "ullamco occaecat nostrud irure",
                "tags": [
                    {
                        "name": "name",
                        "value": "value"
                    }
                ]
            },
            "new_relic": {
                "host": "dolor adipisicing eu dolore incididunt",
                "ingestion_key": "aliqua"
            },
            "splunk": {
                "host": "enim incididunt",
                "token": "Lorem Duis ipsum et"
            },
            "tcp": {
                "host": "qui in cupidatat deserunt cillum",
                "port": 39897
            },
            "http": {
                "host": "nostrud ea dolore",
                "port": 52587,
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
    replicas=183,
    country_codes=[
        "af"
    ],
    networking={
        "port": 60033
    },
    liveness_probe={
        "tcp": {
            "port": 23269
        },
        "http": {
            "path": "path",
            "port": 61900,
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
            "port": 58759
        },
        "exec_": {
            "command": [
                "command"
            ]
        },
        "initial_delay_seconds": 5,
        "period_seconds": 10,
        "timeout_seconds": 30,
        "success_threshold": 1,
        "failure_threshold": 3
    },
    readiness_probe={
        "tcp": {
            "port": 23269
        },
        "http": {
            "path": "path",
            "port": 61900,
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
            "port": 58759
        },
        "exec_": {
            "command": [
                "command"
            ]
        },
        "initial_delay_seconds": 6,
        "period_seconds": 1,
        "timeout_seconds": 1,
        "success_threshold": 1,
        "failure_threshold": 3
    },
    startup_probe={
        "tcp": {
            "port": 23269
        },
        "http": {
            "path": "path",
            "port": 61900,
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
            "port": 58759
        },
        "exec_": {
            "command": [
                "command"
            ]
        },
        "initial_delay_seconds": 4,
        "period_seconds": 3,
        "timeout_seconds": 10,
        "success_threshold": 2,
        "failure_threshold": 1200
    }
)

result = sdk.container_groups.update_container_group(
    request_body=request_body,
    organization_name="ob3ca5hduqlb1uzytbhhukf1u0-ahl0b9oqfjj0q",
    project_name="x7dvdopv2czgde1zrufxgiv5tp-kncd4gfzda9ik-lx71",
    container_group_name="cif9b1yvozs9trd4v0bll7qwslfehyhnfadnjp2w52gwrm0urjjj5b9hbe2fr6f"
)

print(result)

```
