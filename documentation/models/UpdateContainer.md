# UpdateContainer

Represents an update container object

**Properties**

| Name                    | Type                                    | Required | Description                                                                                      |
| :---------------------- | :-------------------------------------- | :------- | :----------------------------------------------------------------------------------------------- |
| image                   | `str`                                   | ❌       |                                                                                                  |
| resources               | `Resources`                             | ❌       |                                                                                                  |
| command                 | `List[str]`                             | ❌       | Pass a command (and optional arguments) to override the ENTRYPOINT and CMD of a container image. |
| priority                | `ContainerGroupPriority`                | ❌       |                                                                                                  |
| environment_variables   | `dict`                                  | ❌       |                                                                                                  |
| logging                 | `UpdateContainerLogging`                | ❌       |                                                                                                  |
| registry_authentication | `UpdateContainerRegistryAuthentication` | ❌       |                                                                                                  |

# Resources

**Properties**

| Name           | Type        | Required | Description |
| :------------- | :---------- | :------- | :---------- |
| cpu            | `int`       | ❌       |             |
| memory         | `int`       | ❌       |             |
| gpu_classes    | `List[str]` | ❌       |             |
| storage_amount | `int`       | ❌       |             |

# UpdateContainerLogging

**Properties**

| Name      | Type               | Required | Description |
| :-------- | :----------------- | :------- | :---------- |
| axiom     | `LoggingAxiom3`    | ❌       |             |
| datadog   | `LoggingDatadog3`  | ❌       |             |
| new_relic | `LoggingNewRelic3` | ❌       |             |
| splunk    | `LoggingSplunk3`   | ❌       |             |
| tcp       | `LoggingTcp3`      | ❌       |             |
| http      | `LoggingHttp3`     | ❌       |             |

# LoggingAxiom_3

**Properties**

| Name      | Type  | Required | Description |
| :-------- | :---- | :------- | :---------- |
| host      | `str` | ✅       |             |
| api_token | `str` | ✅       |             |
| dataset   | `str` | ✅       |             |

# LoggingDatadog_3

**Properties**

| Name    | Type                 | Required | Description |
| :------ | :------------------- | :------- | :---------- |
| host    | `str`                | ✅       |             |
| api_key | `str`                | ✅       |             |
| tags    | `List[DatadogTags3]` | ❌       |             |

# DatadogTags_3

**Properties**

| Name  | Type  | Required | Description |
| :---- | :---- | :------- | :---------- |
| name  | `str` | ✅       |             |
| value | `str` | ✅       |             |

# LoggingNewRelic_3

**Properties**

| Name          | Type  | Required | Description |
| :------------ | :---- | :------- | :---------- |
| host          | `str` | ✅       |             |
| ingestion_key | `str` | ✅       |             |

# LoggingSplunk_3

**Properties**

| Name  | Type  | Required | Description |
| :---- | :---- | :------- | :---------- |
| host  | `str` | ✅       |             |
| token | `str` | ✅       |             |

# LoggingTcp_3

**Properties**

| Name | Type  | Required | Description |
| :--- | :---- | :------- | :---------- |
| host | `str` | ✅       |             |
| port | `int` | ✅       |             |

# LoggingHttp_3

**Properties**

| Name        | Type                 | Required | Description |
| :---------- | :------------------- | :------- | :---------- |
| host        | `str`                | ✅       |             |
| port        | `int`                | ✅       |             |
| format      | `HttpFormat3`        | ✅       |             |
| compression | `HttpCompression3`   | ✅       |             |
| user        | `str`                | ❌       |             |
| password    | `str`                | ❌       |             |
| path        | `str`                | ❌       |             |
| headers     | `List[HttpHeaders4]` | ❌       |             |

# HttpFormat_3

**Properties**

| Name      | Type  | Required | Description  |
| :-------- | :---- | :------- | :----------- |
| JSON      | `str` | ✅       | "json"       |
| JSONLINES | `str` | ✅       | "json_lines" |

# HttpHeaders_4

**Properties**

| Name  | Type  | Required | Description |
| :---- | :---- | :------- | :---------- |
| name  | `str` | ✅       |             |
| value | `str` | ✅       |             |

# HttpCompression_3

**Properties**

| Name | Type  | Required | Description |
| :--- | :---- | :------- | :---------- |
| NONE | `str` | ✅       | "none"      |
| GZIP | `str` | ✅       | "gzip"      |

# UpdateContainerRegistryAuthentication

**Properties**

| Name       | Type                               | Required | Description |
| :--------- | :--------------------------------- | :------- | :---------- |
| basic      | `RegistryAuthenticationBasic2`     | ❌       |             |
| gcp_gcr    | `RegistryAuthenticationGcpGcr2`    | ❌       |             |
| aws_ecr    | `RegistryAuthenticationAwsEcr2`    | ❌       |             |
| docker_hub | `RegistryAuthenticationDockerHub2` | ❌       |             |
| gcp_gar    | `RegistryAuthenticationGcpGar2`    | ❌       |             |

# RegistryAuthenticationBasic_2

**Properties**

| Name     | Type  | Required | Description |
| :------- | :---- | :------- | :---------- |
| username | `str` | ✅       |             |
| password | `str` | ✅       |             |

# RegistryAuthenticationGcpGcr_2

**Properties**

| Name        | Type  | Required | Description |
| :---------- | :---- | :------- | :---------- |
| service_key | `str` | ✅       |             |

# RegistryAuthenticationAwsEcr_2

**Properties**

| Name              | Type  | Required | Description |
| :---------------- | :---- | :------- | :---------- |
| access_key_id     | `str` | ✅       |             |
| secret_access_key | `str` | ✅       |             |

# RegistryAuthenticationDockerHub_2

**Properties**

| Name                  | Type  | Required | Description |
| :-------------------- | :---- | :------- | :---------- |
| username              | `str` | ✅       |             |
| personal_access_token | `str` | ✅       |             |

# RegistryAuthenticationGcpGar_2

**Properties**

| Name        | Type  | Required | Description |
| :---------- | :---- | :------- | :---------- |
| service_key | `str` | ✅       |             |
