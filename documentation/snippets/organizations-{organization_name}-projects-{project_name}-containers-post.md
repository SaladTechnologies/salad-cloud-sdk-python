```python
from salad_cloud_sdk import SaladCloudSdk
from salad_cloud_sdk.models import CreateContainerGroup

sdk = SaladCloudSdk(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    timeout=10000
)

request_body = CreateContainerGroup(
    name="name",
    display_name=".x9,4l5Qs6",
    container={
        "image": "image",
        "resources": {
            "cpu": 2,
            "memory": 50123,
            "gpu_classes": [
                "gpu_classes"
            ],
            "storage_amount": 10520457433
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
                "port": 54933
            },
            "http": {
                "host": "host",
                "port": 34196,
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
    autostart_policy=True,
    restart_policy="always",
    replicas=65,
    country_codes=[
        "af"
    ],
    networking={
        "protocol": "http",
        "port": 47917,
        "auth": False,
        "load_balancer": "round_robin",
        "single_connection_limit": True,
        "client_request_timeout": 100000,
        "server_response_timeout": 100000
    },
    liveness_probe={
        "tcp": {
            "port": 5853
        },
        "http": {
            "path": "path",
            "port": 64861,
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
            "port": 15336
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
            "port": 5853
        },
        "http": {
            "path": "path",
            "port": 64861,
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
            "port": 15336
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
            "port": 5853
        },
        "http": {
            "path": "path",
            "port": 64861,
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
            "port": 15336
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
    },
    queue_connection={
        "path": "path",
        "port": 48169,
        "queue_name": "rozs9trd4v0bll7qwslfehyhnfadnjp2w52gw"
    },
    queue_autoscaler={
        "min_replicas": 72,
        "max_replicas": 136,
        "desired_queue_length": 49,
        "polling_period": 497,
        "max_upscale_per_minute": 27,
        "max_downscale_per_minute": 25
    }
)

result = sdk.container_groups.create_container_group(
    request_body=request_body,
    organization_name="dj0q7z7dvdopv2czf",
    project_name="c1zrufxgh"
)

print(result)

```
