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
    display_name="GzGG5v3-Z",
    container={
        "image": "labore mollit tempor elit",
        "resources": {
            "cpu": 3,
            "memory": 2085,
            "gpu_classes": [
                "gpu_classes"
            ],
            "storage_amount": 27222255995
        },
        "command": [
            "command"
        ],
        "priority": "high",
        "environment_variables": {},
        "logging": {
            "axiom": {
                "host": "et in ipsum",
                "api_token": "in sit in velit mollit",
                "dataset": "in"
            },
            "datadog": {
                "host": "incididunt irure",
                "api_key": "ea ullamco",
                "tags": [
                    {
                        "name": "name",
                        "value": "value"
                    }
                ]
            },
            "new_relic": {
                "host": "labore irure enim consequat",
                "ingestion_key": "aliquip consequat"
            },
            "splunk": {
                "host": "ea fugiat",
                "token": "nulla pariatur"
            },
            "tcp": {
                "host": "reprehenderit magna Ut veniam do",
                "port": 37055
            },
            "http": {
                "host": "nisi laborum pariatur",
                "port": 15435,
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
    replicas=242,
    country_codes=[
        "af"
    ],
    networking={
        "port": 16926
    },
    liveness_probe={
        "tcp": {
            "port": 33909
        },
        "http": {
            "path": "path",
            "port": 58747,
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
            "port": 54101
        },
        "exec_": {
            "command": [
                "command"
            ]
        },
        "initial_delay_seconds": 1,
        "period_seconds": 10,
        "timeout_seconds": 30,
        "success_threshold": 1,
        "failure_threshold": 3
    },
    readiness_probe={
        "tcp": {
            "port": 33909
        },
        "http": {
            "path": "path",
            "port": 58747,
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
            "port": 54101
        },
        "exec_": {
            "command": [
                "command"
            ]
        },
        "initial_delay_seconds": 10,
        "period_seconds": 1,
        "timeout_seconds": 1,
        "success_threshold": 1,
        "failure_threshold": 3
    },
    startup_probe={
        "tcp": {
            "port": 33909
        },
        "http": {
            "path": "path",
            "port": 58747,
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
            "port": 54101
        },
        "exec_": {
            "command": [
                "command"
            ]
        },
        "initial_delay_seconds": 6,
        "period_seconds": 3,
        "timeout_seconds": 10,
        "success_threshold": 2,
        "failure_threshold": 1200
    }
)

result = sdk.container_groups.update_container_group(
    request_body=request_body,
    organization_name="hjn8ph-8qr9s",
    project_name="zpcs1c-85eq2giu1ly3ke1lk2gb3mqhp",
    container_group_name="obcxrd0mqez"
)

print(result)

```
