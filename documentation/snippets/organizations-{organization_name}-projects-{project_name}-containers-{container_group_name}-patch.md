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
    display_name="s1RiI 0-",
    container={
        "image": "ipsum pariatur non proident dolore",
        "resources": {
            "cpu": 2,
            "memory": 19703,
            "gpu_classes": [
                "gpu_classes"
            ],
            "storage_amount": 4820479057
        },
        "command": [
            "command"
        ],
        "priority": "high",
        "environment_variables": {},
        "logging": {
            "axiom": {
                "host": "aliquip magna est ex tempor",
                "api_token": "esse magna eu ut amet",
                "dataset": "in pariatur Duis non"
            },
            "datadog": {
                "host": "Duis",
                "api_key": "id magna cupidatat ipsum aliqua",
                "tags": [
                    {
                        "name": "name",
                        "value": "value"
                    }
                ]
            },
            "new_relic": {
                "host": "Duis culpa cillum",
                "ingestion_key": "exercitation sint aute aliqua ex"
            },
            "splunk": {
                "host": "ex culpa exercitation ad proident",
                "token": "laborum"
            },
            "tcp": {
                "host": "pariatur",
                "port": 45370
            },
            "http": {
                "host": "ut in et quis adipisicing",
                "port": 33069,
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
    replicas=97,
    country_codes=[
        "af"
    ],
    networking={
        "port": 14234
    },
    liveness_probe={
        "tcp": {
            "port": 39336
        },
        "http": {
            "path": "path",
            "port": 8799,
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
            "port": 15387
        },
        "exec_": {
            "command": [
                "command"
            ]
        },
        "initial_delay_seconds": 0,
        "period_seconds": 10,
        "timeout_seconds": 30,
        "success_threshold": 1,
        "failure_threshold": 3
    },
    readiness_probe={
        "tcp": {
            "port": 39336
        },
        "http": {
            "path": "path",
            "port": 8799,
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
            "port": 15387
        },
        "exec_": {
            "command": [
                "command"
            ]
        },
        "initial_delay_seconds": 9,
        "period_seconds": 1,
        "timeout_seconds": 1,
        "success_threshold": 1,
        "failure_threshold": 3
    },
    startup_probe={
        "tcp": {
            "port": 39336
        },
        "http": {
            "path": "path",
            "port": 8799,
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
            "port": 15387
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
    }
)

result = sdk.container_groups.update_container_group(
    request_body=request_body,
    organization_name="a147vxii7gy6-eg0n389rp",
    project_name="zcgtz8t87b",
    container_group_name="jonf9u1s785z-11dylxjw4966ge-9p6qcjc-qtefzoj09ev3nsih"
)

print(result)

```
