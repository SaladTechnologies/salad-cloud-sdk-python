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
    name="yywq967xo8ifvlka8kdg6t3d8cqm9k9rc7a8bvhvcpg50j51gan4fglcmonhm",
    display_name="0hxi6,PR",
    container={
        "image": "nostrud aute adipisicing",
        "resources": {
            "cpu": 10,
            "memory": 7505,
            "gpu_classes": [
                "gpu_classes"
            ],
            "storage_amount": 3605508236
        },
        "command": [
            "command"
        ],
        "priority": "high",
        "environment_variables": {},
        "logging": {
            "axiom": {
                "host": "sed",
                "api_token": "nisi elit est",
                "dataset": "Excepteur"
            },
            "datadog": {
                "host": "Lorem magna qui Duis",
                "api_key": "minim aliquip qui",
                "tags": [
                    {
                        "name": "name",
                        "value": "value"
                    }
                ]
            },
            "new_relic": {
                "host": "adipisicing",
                "ingestion_key": "culpa enim"
            },
            "splunk": {
                "host": "ut",
                "token": "aliquip dolore"
            },
            "tcp": {
                "host": "irure reprehenderit ut",
                "port": 26986
            },
            "http": {
                "host": "cupidatat irure reprehenderit amet",
                "port": 9553,
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
    replicas=122,
    country_codes=[
        "af"
    ],
    networking={
        "protocol": "http",
        "port": 53954,
        "auth": False
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
    },
    queue_connection={
        "path": "qui cupidatat esse labore",
        "port": 36246,
        "queue_name": "tv1-ax-msj6w-h3wkst4x03b6y4ltw1qvh-38ot"
    }
)

result = sdk.container_groups.create_container_group(
    request_body=request_body,
    organization_name="nhyrq",
    project_name="r92pbz5hsuado6z0y3kws22ptp7cp7eaw33zizk"
)

print(result)

```
