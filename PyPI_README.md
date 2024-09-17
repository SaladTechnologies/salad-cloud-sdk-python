# SaladCloudSdk Python SDK 0.9.0-alpha.3<a id="saladcloudsdk-python-sdk-090-alpha3"></a>

Welcome to the SaladCloudSdk SDK documentation. This guide will help you get started with integrating and using the SaladCloudSdk SDK in your project.

## Versions<a id="versions"></a>

- API version: `0.9.0-alpha.3`
- SDK version: `0.9.0-alpha.3`

## About the API<a id="about-the-api"></a>

The SaladCloud REST API. Please refer to the [SaladCloud API Documentation](https://docs.salad.com/api-reference) for more details.

## Table of Contents<a id="table-of-contents"></a>

- [Setup & Configuration](#setup--configuration)
  - [Supported Language Versions](#supported-language-versions)
  - [Installation](#installation)
- [Authentication](#authentication)
  - [API Key Authentication](#api-key-authentication)
- [Setting a Custom Timeout](#setting-a-custom-timeout)
- [Sample Usage](#sample-usage)
- [Services](#services)
- [Models](#models)
- [License](#license)

## Setup & Configuration<a id="setup--configuration"></a>

### Supported Language Versions<a id="supported-language-versions"></a>

This SDK is compatible with the following versions: `Python >= 3.7`

### Installation<a id="installation"></a>

To get started with the SDK, we recommend installing using `pip`:

```bash
pip install salad-cloud-sdk
```

## Authentication<a id="authentication"></a>

### API Key Authentication<a id="api-key-authentication"></a>

The SaladCloudSdk API uses API keys as a form of authentication. An API key is a unique identifier used to authenticate a user, developer, or a program that is calling the API.

#### Setting the API key<a id="setting-the-api-key"></a>

When you initialize the SDK, you can set the API key as follows:

```py
SaladCloudSdk(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    timeout=10000
)
```

If you need to set or update the API key after initializing the SDK, you can use:

```py
sdk.set_api_key("YOUR_API_KEY", "YOUR_API_KEY_HEADER")
```

## Setting a Custom Timeout<a id="setting-a-custom-timeout"></a>

You can set a custom timeout for the SDK's HTTP requests as follows:

```py
from salad_cloud_sdk import SaladCloudSdk

sdk = SaladCloudSdk(timeout=10000)
```

# Sample Usage<a id="sample-usage"></a>

Below is a comprehensive example demonstrating how to authenticate and call a simple endpoint:

```py
from salad_cloud_sdk import SaladCloudSdk, Environment

sdk = SaladCloudSdk(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

result = sdk.quotas.get_quotas(organization_name="yp5d1ln00phm36ghf3imgjjp6z9mn")

print(result)

```

## Services<a id="services"></a>

The SDK provides various services to interact with the API.

<details> 
<summary>Below is a list of all available services:</summary>

| Name                |
| :------------------ |
| container_groups    |
| workload_errors     |
| queues              |
| quotas              |
| inference_endpoints |
| organization_data   |
| webhook_secret_key  |

</details>

## Models<a id="models"></a>

The SDK includes several models that represent the data structures used in API requests and responses. These models help in organizing and managing the data efficiently.

<details> 
<summary>Below is a list of all available models:</summary>

| Name                              | Description                                                              |
| :-------------------------------- | :----------------------------------------------------------------------- |
| ContainerGroupList                | Represents a list of container groups                                    |
| CreateContainerGroup              | Represents a request to create a container group                         |
| ContainerGroup                    | Represents a container group                                             |
| UpdateContainerGroup              | Represents a request to update a container group                         |
| ContainerGroupInstances           | Represents a list of container group instances                           |
| ContainerGroupInstance            | Represents the details of a single container group instance              |
| WorkloadErrorList                 | Represents a list of workload errors                                     |
| QueueList                         | Represents a list of queues                                              |
| CreateQueue                       | Represents a request to create a new queue.                              |
| Queue                             | Represents a queue.                                                      |
| UpdateQueue                       | Represents a request to update an existing queue.                        |
| QueueJobList                      | Represents a list of queue jobs                                          |
| CreateQueueJob                    | Represents a request to create a queue job                               |
| QueueJob                          | Represents a queue job                                                   |
| Quotas                            | Represents the organization quotas                                       |
| InferenceEndpointsList            | Represents a list of inference endpoints                                 |
| InferenceEndpoint                 | Represents an inference endpoint                                         |
| InferenceEndpointJobList          | Represents a list of inference endpoint jobs                             |
| CreateInferenceEndpointJob        | Represents a request to create a inference endpoint job                  |
| InferenceEndpointJob              | Represents a inference endpoint job                                      |
| GpuClassesList                    | Represents a list of GPU classes                                         |
| WebhookSecretKey                  | Represents a webhook secret key                                          |
| Container                         | Represents a container                                                   |
| ContainerRestartPolicy            |                                                                          |
| ContainerGroupState               | Represents a container group state                                       |
| CountryCode                       |                                                                          |
| ContainerGroupNetworking          | Represents container group networking parameters                         |
| ContainerGroupLivenessProbe       | Represents the container group liveness probe                            |
| ContainerGroupReadinessProbe      | Represents the container group readiness probe                           |
| ContainerGroupStartupProbe        | Represents the container group startup probe                             |
| ContainerGroupQueueConnection     | Represents container group queue connection                              |
| QueueAutoscaler                   | Represents the autoscaling rules for a queue                             |
| ContainerResourceRequirements     | Represents a container resource requirements                             |
| ContainerGroupPriority            |                                                                          |
| ContainerGroupStatus              |                                                                          |
| ContainerGroupInstanceStatusCount | Represents a container group instance status count                       |
| ContainerNetworkingProtocol       |                                                                          |
| ContainerGroupProbeTcp            |                                                                          |
| ContainerGroupProbeHttp           |                                                                          |
| ContainerGroupProbeGrpc           |                                                                          |
| ContainerGroupProbeExec           |                                                                          |
| ContainerProbeHttpScheme          |                                                                          |
| ContainerGroupProbeHttpHeaders2   |                                                                          |
| CreateContainer                   | Represents a container                                                   |
| CreateContainerGroupNetworking    | Represents container group networking parameters                         |
| UpdateContainer                   | Represents an update container object                                    |
| UpdateContainerGroupNetworking    | Represents update container group networking parameters                  |
| WorkloadError                     | Represents a workload error                                              |
| QueueJobEvent                     | Represents an event for queue job                                        |
| ContainerGroupsQuotas             |                                                                          |
| RecipesQuotas                     |                                                                          |
| InferenceEndpointJobEvent         | Represents an event for inference endpoint job                           |
| GpuClass                          | Represents a GPU Class                                                   |
| GpuClassPrice                     | Represents the price of a GPU class for a given container group priority |

</details>

## License<a id="license"></a>

This SDK is licensed under the MIT License.

See the [LICENSE](LICENSE) file for more details.
