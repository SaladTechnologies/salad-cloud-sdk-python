```python
from salad_cloud_sdk import SaladCloudSdk
from salad_cloud_sdk.models import UpdateContainerGroup

sdk = SaladCloudSdk(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    timeout=10000
)

request_body = UpdateContainerGroup(
    display_name="B9lINce",
    container={
        "image": "image",
        "resources": {
            "cpu": 6,
            "memory": 32135,
            "gpu_classes": [
                "gpu_classes"
            ],
            "storage_amount": 46738030912
        },
        "command": [
            "command"
        ],
        "priority": "high",
        "environment_variables": {},
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
                "port": 3757
            },
            "http": {
                "host": "host",
                "port": 4255,
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
    replicas=57,
    country_codes=[
        "af"
    ],
    networking={
        "port": 53904
    },
    liveness_probe={
        "tcp": {
            "port": 55801
        },
        "http": {
            "path": "path",
            "port": 15919,
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
            "port": 58232
        },
        "exec_": {
            "command": [
                "command"
            ]
        },
        "initial_delay_seconds": 3,
        "period_seconds": 10,
        "timeout_seconds": 30,
        "success_threshold": 1,
        "failure_threshold": 3
    },
    readiness_probe={
        "tcp": {
            "port": 55801
        },
        "http": {
            "path": "path",
            "port": 15919,
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
            "port": 58232
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
            "port": 55801
        },
        "http": {
            "path": "path",
            "port": 15919,
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
            "port": 58232
        },
        "exec_": {
            "command": [
                "command"
            ]
        },
        "initial_delay_seconds": 2,
        "period_seconds": 3,
        "timeout_seconds": 10,
        "success_threshold": 2,
        "failure_threshold": 1200
    },
    queue_autoscaler={
        "min_replicas": 68,
        "max_replicas": 62,
        "desired_queue_length": 38,
        "polling_period": 711,
        "max_upscale_per_minute": 41,
        "max_downscale_per_minute": 89
    }
)

result = sdk.container_groups.update_container_group(
    request_body=request_body,
    organization_name="acme-corp",
    project_name="dev-env",
    container_group_name="j2i7s81kn7vit2ttnz26lyemw7nednorlqjlsihb42092pn8d6"
)

print(result)

```
