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
    name="qfojt-6ccoil4t55-ccoyybgw92dermtsdfn3t2xmag",
    display_name="O0hSlJUW",
    container={
        "image": "voluptate officia adipisicing",
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
                "host": "Ut con",
                "api_token": "nostrud irure dolore",
                "dataset": "mollit irure et Duis dolore"
            },
            "datadog": {
                "host": "pariatur",
                "api_key": "non ut",
                "tags": [
                    {
                        "name": "name",
                        "value": "value"
                    }
                ]
            },
            "new_relic": {
                "host": "cupidatat cillum est sit minim",
                "ingestion_key": "dolore laboris fugiat Duis"
            },
            "splunk": {
                "host": "aliquip velit culpa",
                "token": "ex"
            },
            "tcp": {
                "host": "aliqua",
                "port": 17249
            },
            "http": {
                "host": "magna",
                "port": 62049,
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
    replicas=114,
    country_codes=[
        "af"
    ],
    networking={
        "protocol": "http",
        "port": 9813,
        "auth": False
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
    },
    queue_autoscaler={
        "min_replicas": 57,
        "max_replicas": 24,
        "desired_queue_length": 20,
        "polling_period": 1406,
        "max_upscale_per_minute": 35,
        "max_downscale_per_minute": 42
    }
)

result = sdk.container_groups.create_container_group(
    request_body=request_body,
    organization_name="v50imwzgi4em4q035",
    project_name="m6yw3-xm60cb7tiev8rketqiiwjepibzf2ust1cvjx8oua8mepeueo5-1"
)

print(result)

```
