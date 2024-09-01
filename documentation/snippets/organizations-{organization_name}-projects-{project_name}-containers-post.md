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
    name="qqgh5gtdxccg-tsuo",
    display_name="0GALm",
    container={
        "image": "exercitation eu pariatur elit adipisicing",
        "resources": {
            "cpu": 12,
            "memory": 26125,
            "gpu_classes": [
                "gpu_classes"
            ],
            "storage_amount": 30852754821
        },
        "command": [
            "command"
        ],
        "priority": "high",
        "environment_variables": {},
        "logging": {
            "axiom": {
                "host": "incididunt cupidatat",
                "api_token": "ullamco",
                "dataset": "ad nisi laborum"
            },
            "datadog": {
                "host": "sint",
                "api_key": "labore cupidatat",
                "tags": [
                    {
                        "name": "name",
                        "value": "value"
                    }
                ]
            },
            "new_relic": {
                "host": "cupidatat",
                "ingestion_key": "dolor occaecat in dolore in"
            },
            "splunk": {
                "host": "cillum in dolor",
                "token": "ex incididunt elit adipisicing"
            },
            "tcp": {
                "host": "incididunt fugiat enim officia sed",
                "port": 30285
            },
            "http": {
                "host": "enim magna esse",
                "port": 30824,
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
    replicas=81,
    country_codes=[
        "af"
    ],
    networking={
        "protocol": "http",
        "port": 4886,
        "auth": False
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
    },
    queue_connection={
        "path": "velit elit",
        "port": 7009,
        "queue_name": "wh1ewe-69ifjpdhw0h4i3hwpdzw-n1fpjd0naycxeb1u1iiyrp-4y1t7"
    }
)

result = sdk.container_groups.create_container_group(
    request_body=request_body,
    organization_name="apihl1d8o144-mf49qtwmztxy5e3c9v5qfb4l0g8j1lcj9-nh4i6dz2e7jf3",
    project_name="vjbveijqip5mysgje2g39crv0td0zupa8uxmseld79zsgkh7je6z"
)

print(result)

```
