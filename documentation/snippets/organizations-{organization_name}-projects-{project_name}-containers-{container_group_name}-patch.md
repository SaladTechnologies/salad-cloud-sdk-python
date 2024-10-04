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
    display_name="01n75",
    container={
        "image": "labore",
        "resources": {
            "cpu": 3,
            "memory": 14678,
            "gpu_classes": [
                "gpu_classes"
            ],
            "storage_amount": 47984533464
        },
        "command": [
            "command"
        ],
        "priority": "high",
        "environment_variables": {},
        "logging": {
            "axiom": {
                "host": "aute veniam exercitation eiusmod et",
                "api_token": "mollit",
                "dataset": "nisi in Lorem"
            },
            "datadog": {
                "host": "velit officia consequat",
                "api_key": "sit in veniam",
                "tags": [
                    {
                        "name": "name",
                        "value": "value"
                    }
                ]
            },
            "new_relic": {
                "host": "consequat sed",
                "ingestion_key": "tempor exercitation"
            },
            "splunk": {
                "host": "qui enim Ut nostrud deserunt",
                "token": "cillum sint ullamco veniam occaecat"
            },
            "tcp": {
                "host": "Ut amet",
                "port": 30110
            },
            "http": {
                "host": "eiusmod labore proident sit ut",
                "port": 17490,
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
    replicas=232,
    country_codes=[
        "af"
    ],
    networking={
        "port": 35022
    },
    liveness_probe={
        "tcp": {
            "port": 61900
        },
        "http": {
            "path": "path",
            "port": 58759,
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
            "port": 32748
        },
        "exec_": {
            "command": [
                "command"
            ]
        },
        "initial_delay_seconds": 6,
        "period_seconds": 10,
        "timeout_seconds": 30,
        "success_threshold": 1,
        "failure_threshold": 3
    },
    readiness_probe={
        "tcp": {
            "port": 61900
        },
        "http": {
            "path": "path",
            "port": 58759,
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
            "port": 32748
        },
        "exec_": {
            "command": [
                "command"
            ]
        },
        "initial_delay_seconds": 4,
        "period_seconds": 1,
        "timeout_seconds": 1,
        "success_threshold": 1,
        "failure_threshold": 3
    },
    startup_probe={
        "tcp": {
            "port": 61900
        },
        "http": {
            "path": "path",
            "port": 58759,
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
            "port": 32748
        },
        "exec_": {
            "command": [
                "command"
            ]
        },
        "initial_delay_seconds": 10,
        "period_seconds": 3,
        "timeout_seconds": 10,
        "success_threshold": 2,
        "failure_threshold": 1200
    },
    queue_autoscaler={
        "min_replicas": 96,
        "max_replicas": 190,
        "desired_queue_length": 42,
        "polling_period": 684,
        "max_upscale_per_minute": 95,
        "max_downscale_per_minute": 10
    }
)

result = sdk.container_groups.update_container_group(
    request_body=request_body,
    organization_name="oji7lyvxb3ca5hc",
    project_name="olb1uzytbhhukf1u0-ahl0b9oqfjj",
    container_group_name="s7z7dvdopv2czgde1zrufxgiv5tp-j"
)

print(result)

```
