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
    display_name="ny",
    container={
        "image": "image",
        "resources": {
            "cpu": 3,
            "memory": 16094,
            "gpu_classes": [
                "gpu_classes"
            ],
            "storage_amount": 50473301867
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
                "port": 52754
            },
            "http": {
                "host": "host",
                "port": 58619,
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
    replicas=47,
    country_codes=[
        "af"
    ],
    networking={
        "protocol": "http",
        "port": 64929,
        "auth": True,
        "load_balancer": "round_robin",
        "single_connection_limit": True,
        "client_request_timeout": 100000,
        "server_response_timeout": 100000
    },
    liveness_probe={
        "tcp": {
            "port": 9366
        },
        "http": {
            "path": "path",
            "port": 398,
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
            "port": 23866
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
            "port": 9366
        },
        "http": {
            "path": "path",
            "port": 398,
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
            "port": 23866
        },
        "exec_": {
            "command": [
                "command"
            ]
        },
        "initial_delay_seconds": 8,
        "period_seconds": 1,
        "timeout_seconds": 1,
        "success_threshold": 1,
        "failure_threshold": 3
    },
    startup_probe={
        "tcp": {
            "port": 9366
        },
        "http": {
            "path": "path",
            "port": 398,
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
            "port": 23866
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
    queue_connection={
        "path": "path",
        "port": 34806,
        "queue_name": "r3qna2yfhck403bsaqbf6nweyawtm7q4ohr"
    },
    queue_autoscaler={
        "min_replicas": 88,
        "max_replicas": 197,
        "desired_queue_length": 57,
        "polling_period": 1449,
        "max_upscale_per_minute": 85,
        "max_downscale_per_minute": 33
    }
)

result = sdk.container_groups.create_container_group(
    request_body=request_body,
    organization_name="acme-corp",
    project_name="dev-env"
)

print(result)

```
