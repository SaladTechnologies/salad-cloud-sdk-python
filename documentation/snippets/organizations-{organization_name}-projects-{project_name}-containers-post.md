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
    display_name="uPpL",
    container={
        "image": "image",
        "resources": {
            "cpu": 7,
            "memory": 51618,
            "gpu_classes": [
                "gpu_classes"
            ],
            "storage_amount": 23627499788
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
                "port": 14084
            },
            "http": {
                "host": "host",
                "port": 31838,
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
        },
        "image_caching": False
    },
    autostart_policy=False,
    restart_policy="always",
    replicas=437,
    country_codes=[
        "af"
    ],
    networking={
        "protocol": "http",
        "port": 51618,
        "auth": True,
        "load_balancer": "round_robin",
        "single_connection_limit": True,
        "client_request_timeout": 100000,
        "server_response_timeout": 100000
    },
    liveness_probe={
        "tcp": {
            "port": 63625
        },
        "http": {
            "path": "path",
            "port": 28190,
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
            "port": 43451
        },
        "exec_": {
            "command": [
                "command"
            ]
        },
        "initial_delay_seconds": 2,
        "period_seconds": 10,
        "timeout_seconds": 30,
        "success_threshold": 1,
        "failure_threshold": 3
    },
    readiness_probe={
        "tcp": {
            "port": 63625
        },
        "http": {
            "path": "path",
            "port": 28190,
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
            "port": 43451
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
            "port": 63625
        },
        "http": {
            "path": "path",
            "port": 28190,
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
            "port": 43451
        },
        "exec_": {
            "command": [
                "command"
            ]
        },
        "initial_delay_seconds": 7,
        "period_seconds": 3,
        "timeout_seconds": 10,
        "success_threshold": 2,
        "failure_threshold": 1200
    },
    queue_connection={
        "path": "path",
        "port": 33046,
        "queue_name": "dbfand1htyt3qna2yfhck403bsaqbf"
    },
    queue_autoscaler={
        "min_replicas": 60,
        "max_replicas": 62,
        "desired_queue_length": 67,
        "polling_period": 39,
        "max_upscale_per_minute": 62,
        "max_downscale_per_minute": 52
    }
)

result = sdk.container_groups.create_container_group(
    request_body=request_body,
    organization_name="acme-corp",
    project_name="dev-env"
)

print(result)

```
