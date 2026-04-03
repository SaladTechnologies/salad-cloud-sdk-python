```python
from salad_cloud_sdk import SaladCloudSdk
from salad_cloud_sdk.models import ContainerGroupCreationRequest

sdk = SaladCloudSdk(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    timeout=10000
)

request_body = ContainerGroupCreationRequest(
    autostart_policy=False,
    container={
        "command": [
            "command"
        ],
        "environment_variables": {},
        "image": "acme/:latest",
        "image_caching": True,
        "logging": {
            "axiom": {
                "api_token": "api_token",
                "dataset": "dataset",
                "host": "host"
            },
            "datadog": {
                "api_key": "api_key",
                "host": "host",
                "tags": [
                    {
                        "name": "name",
                        "value": "value"
                    }
                ]
            },
            "http": {
                "compression": "none",
                "format": "json",
                "headers": [
                    {
                        "name": "name",
                        "value": "value"
                    }
                ],
                "host": "host",
                "password": "password",
                "path": "path",
                "port": 42056,
                "user": "user"
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
                "port": 44671
            }
        },
        "priority": "high",
        "registry_authentication": {
            "aws_ecr": {
                "access_key_id": "access_key_id",
                "secret_access_key": "secret_access_key"
            },
            "basic": {
                "password": "password",
                "username": "username"
            },
            "docker_hub": {
                "personal_access_token": "personal_access_token",
                "username": "username"
            },
            "gcp_gar": {
                "service_key": "service_key"
            },
            "gcp_gcr": {
                "service_key": "service_key"
            }
        },
        "resources": {
            "cpu": 827,
            "gpu_classes": [
                "gpu_classes"
            ],
            "memory": 734164836,
            "shm_size": 64,
            "storage_amount": 761306530849177.9
        }
    },
    country_codes=[
        "af"
    ],
    display_name="KMg0KyVwpb",
    liveness_probe={
        "exec_": {
            "command": [
                "command"
            ]
        },
        "failure_threshold": 3,
        "grpc": {
            "port": 37648,
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
            "port": 29069,
            "scheme": "http"
        },
        "initial_delay_seconds": 670,
        "period_seconds": 10,
        "success_threshold": 1,
        "tcp": {
            "port": 13817
        },
        "timeout_seconds": 30
    },
    name="name",
    networking={
        "auth": False,
        "client_request_timeout": 100000,
        "load_balancer": "round_robin",
        "port": 60000,
        "protocol": "http",
        "server_response_timeout": 100000,
        "single_connection_limit": False
    },
    queue_autoscaler={
        "desired_queue_length": 53,
        "max_downscale_per_minute": 59,
        "max_replicas": 321,
        "max_upscale_per_minute": 100,
        "min_replicas": 54,
        "polling_period": 140
    },
    queue_connection={
        "path": "path",
        "port": 47568,
        "queue_name": "z1h-3z01x9"
    },
    readiness_probe={
        "exec_": {
            "command": [
                "command"
            ]
        },
        "failure_threshold": 3,
        "grpc": {
            "port": 37648,
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
            "port": 29069,
            "scheme": "http"
        },
        "initial_delay_seconds": 262,
        "period_seconds": 1,
        "success_threshold": 1,
        "tcp": {
            "port": 13817
        },
        "timeout_seconds": 1
    },
    replicas=77,
    restart_policy="always",
    scaling_actions=[
        {
            "replicas": 461,
            "schedule": "7kwC/T8C   da       x6Ci   bM-rgGYn     bDY6,vT"
        }
    ],
    scheduled_scaling_enabled=True,
    startup_probe={
        "exec_": {
            "command": [
                "command"
            ]
        },
        "failure_threshold": 15,
        "grpc": {
            "port": 37648,
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
            "port": 29069,
            "scheme": "http"
        },
        "initial_delay_seconds": 503,
        "period_seconds": 3,
        "success_threshold": 2,
        "tcp": {
            "port": 13817
        },
        "timeout_seconds": 10
    }
)

result = sdk.container_groups.create_container_group(
    request_body=request_body,
    organization_name="acme-corp",
    project_name="dev-env"
)

print(result)

```
