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
    name="oh2mpxyfojt-6cco",
    display_name="HoT",
    container={
        "image": "velit qui cillum veniam ullamco",
        "resources": {
            "cpu": 10,
            "memory": 17858,
            "gpu_classes": [
                "gpu_classes"
            ],
            "storage_amount": 32391110488
        },
        "command": [
            "command"
        ],
        "priority": "high",
        "environment_variables": {},
        "logging": {
            "axiom": {
                "host": "in culpa aute",
                "api_token": "mollit culpa",
                "dataset": "qui nulla laborum ex"
            },
            "datadog": {
                "host": "id fugiat cillum",
                "api_key": "nostrud",
                "tags": [
                    {
                        "name": "name",
                        "value": "value"
                    }
                ]
            },
            "new_relic": {
                "host": "en",
                "ingestion_key": "aliqua ad laboris anim"
            },
            "splunk": {
                "host": "enim cupidatat eiusmod",
                "token": "do"
            },
            "tcp": {
                "host": "aliquip labore dolor id",
                "port": 45778
            },
            "http": {
                "host": "pariatur",
                "port": 16204,
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
    replicas=225,
    country_codes=[
        "af"
    ],
    networking={
        "protocol": "http",
        "port": 19760,
        "auth": True
    },
    liveness_probe={
        "tcp": {
            "port": 23269
        },
        "http": {
            "path": "path",
            "port": 61900,
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
            "port": 58759
        },
        "exec_": {
            "command": [
                "command"
            ]
        },
        "initial_delay_seconds": 5,
        "period_seconds": 10,
        "timeout_seconds": 30,
        "success_threshold": 1,
        "failure_threshold": 3
    },
    readiness_probe={
        "tcp": {
            "port": 23269
        },
        "http": {
            "path": "path",
            "port": 61900,
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
            "port": 58759
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
            "port": 23269
        },
        "http": {
            "path": "path",
            "port": 61900,
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
            "port": 58759
        },
        "exec_": {
            "command": [
                "command"
            ]
        },
        "initial_delay_seconds": 4,
        "period_seconds": 3,
        "timeout_seconds": 10,
        "success_threshold": 2,
        "failure_threshold": 1200
    },
    queue_connection={
        "path": "ullamco magna est nulla aliqua",
        "port": 49952,
        "queue_name": "nnz26lyemw7nednorlqjlsihb42092pn8d"
    }
)

result = sdk.container_groups.create_container_group(
    request_body=request_body,
    organization_name="v50imwzgi4em4q035",
    project_name="m6yw3-xm60cb7tiev8rketqiiwjepibzf2ust1cvjx8oua8mepeueo5-1"
)

print(result)

```
