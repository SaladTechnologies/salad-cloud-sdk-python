```python
from salad_cloud_sdk import SaladCloudSdk, Environment
from salad_cloud_sdk.models import CreateContainerGroup

sdk = SaladCloudSdk(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

request_body = CreateContainerGroup(
    name="n1yhwjdpa4rchjtb6qp-hyt0s34",
    display_name="ICNHy",
    container={
        "image": "velit irure dolore cupidatat",
        "resources": {
            "cpu": 2,
            "memory": 20102,
            "gpu_classes": [
                "gpu_classes"
            ],
            "storage_amount": 4874892434
        },
        "command": [
            "command"
        ],
        "priority": "high",
        "environment_variables": {},
        "logging": {
            "axiom": {
                "host": "sed aute in cillum",
                "api_token": "sunt aute pariatur",
                "dataset": "tempor"
            },
            "datadog": {
                "host": "incid",
                "api_key": "dolor eu pariatur",
                "tags": [
                    {
                        "name": "name",
                        "value": "value"
                    }
                ]
            },
            "new_relic": {
                "host": "laborum ea aliqua",
                "ingestion_key": "anim in incididunt ut Ut"
            },
            "splunk": {
                "host": "officia dolor in aliqua consectetur",
                "token": "ipsum consectetur ea"
            },
            "tcp": {
                "host": "cupidatat do labore pariatur",
                "port": 58307
            },
            "http": {
                "host": "Excepteur sunt",
                "port": 49224,
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
    autostart_policy=False,
    restart_policy="always",
    replicas=67,
    country_codes=[
        "af"
    ],
    networking={
        "protocol": "http",
        "port": 40145,
        "auth": False
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
    },
    queue_connection={
        "path": "ipsum proident",
        "port": 10282,
        "queue_name": "cnb3eo62nsjao0"
    },
    queue_autoscaler={
        "min_replicas": 45,
        "max_replicas": 217,
        "desired_queue_length": 98,
        "polling_period": 897,
        "max_upscale_per_minute": 40,
        "max_downscale_per_minute": 82
    }
)

result = sdk.container_groups.create_container_group(
    request_body=request_body,
    organization_name="g4zikv73wys88ns82g85qcczec2y8bnwc4gs8q6aeebojnkc8rl8-7px",
    project_name="n62j25cdo2sjh0v34w5-21z63jxnxh38ckz48-k1ecu"
)

print(result)

```
