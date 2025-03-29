```python
from salad_cloud_sdk import SaladCloudSdk
from salad_cloud_sdk.models import ContainerGroupPatch

sdk = SaladCloudSdk(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    timeout=10000
)

request_body = ContainerGroupPatch(
    display_name="rukYe",
    container={
        "command": [
            "command"
        ],
        "environment_variables": {},
        "image": "image",
        "image_caching": True,
        "logging": {
            "axiom": {
                "host": "host",
                "api_token": "api_token",
                "dataset": "dataset"
            },
            "datadog": {
                "host": "host",
                "api_key": "api_key",
                "tags": [
                    {
                        "name": "name",
                        "value": "value"
                    }
                ]
            },
            "http": {
                "host": "host",
                "port": 29098,
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
            },
            "new_relic": {
                "host": "host",
                "ingestion_key": "ingestion_key"
            },
            "splunk": {
                "host": "host",
                "token": "token"
            },
            "tcp": {
                "host": "host",
                "port": 54633
            }
        },
        "priority": "high",
        "registry_authentication": {
            "aws_ecr": {
                "access_key_id": "access_key_id",
                "secret_access_key": "secret_access_key"
            },
            "basic": {
                "username": "username",
                "password": "password"
            },
            "docker_hub": {
                "username": "username",
                "personal_access_token": "personal_access_token"
            },
            "gcp_gar": {
                "service_key": "service_key"
            },
            "gcp_gcr": {
                "service_key": "service_key"
            }
        },
        "resources": {
            "cpu": 4,
            "memory": 50175,
            "gpu_classes": [
                "gpu_classes"
            ],
            "storage_amount": 27536827537
        }
    },
    replicas=476,
    country_codes=[
        "af"
    ],
    networking={
        "port": 27606
    },
    liveness_probe={
        "exec_": {
            "command": [
                "command"
            ]
        },
        "failure_threshold": 3,
        "grpc": {
            "port": 52641,
            "service": "service"
        },
        "http": {
            "headers": [
                {
                    "name": "name",
                    "value": "value"
                }
            ],
            "path": "path",
            "port": 55367,
            "scheme": "http"
        },
        "initial_delay_seconds": 392,
        "period_seconds": 10,
        "success_threshold": 1,
        "tcp": {
            "port": 27294
        },
        "timeout_seconds": 30
    },
    readiness_probe={
        "exec_": {
            "command": [
                "command"
            ]
        },
        "failure_threshold": 3,
        "grpc": {
            "port": 52641,
            "service": "service"
        },
        "http": {
            "headers": [
                {
                    "name": "name",
                    "value": "value"
                }
            ],
            "path": "path",
            "port": 55367,
            "scheme": "http"
        },
        "initial_delay_seconds": 202,
        "period_seconds": 1,
        "success_threshold": 1,
        "tcp": {
            "port": 27294
        },
        "timeout_seconds": 1
    },
    startup_probe={
        "exec_": {
            "command": [
                "command"
            ]
        },
        "failure_threshold": 15,
        "grpc": {
            "port": 52641,
            "service": "service"
        },
        "http": {
            "headers": [
                {
                    "name": "name",
                    "value": "value"
                }
            ],
            "path": "path",
            "port": 55367,
            "scheme": "http"
        },
        "initial_delay_seconds": 312,
        "tcp": {
            "port": 27294
        },
        "period_seconds": 3,
        "success_threshold": 2,
        "timeout_seconds": 10
    },
    queue_autoscaler={
        "desired_queue_length": 81,
        "max_replicas": 448,
        "max_downscale_per_minute": 72,
        "max_upscale_per_minute": 19,
        "min_replicas": 100,
        "polling_period": 1772
    }
)

result = sdk.container_groups.update_container_group(
    request_body=request_body,
    organization_name="acme-corp",
    project_name="dev-env",
    container_group_name="mandlebrot"
)

print(result)

```
