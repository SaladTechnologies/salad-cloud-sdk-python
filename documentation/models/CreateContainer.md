# CreateContainer

Represents a container

**Properties**

| Name                    | Type                                  | Required | Description                                                                                      |
| :---------------------- | :------------------------------------ | :------- | :----------------------------------------------------------------------------------------------- |
| image                   | str                                   | ✅       |                                                                                                  |
| resources               | ContainerResourceRequirements         | ✅       | Represents a container resource requirements                                                     |
| command                 | List[str]                             | ❌       | Pass a command (and optional arguments) to override the ENTRYPOINT and CMD of a container image. |
| priority                | ContainerGroupPriority                | ❌       |                                                                                                  |
| environment_variables   | dict                                  | ❌       |                                                                                                  |
| logging                 | CreateContainerLogging                | ❌       |                                                                                                  |
| registry_authentication | CreateContainerRegistryAuthentication | ❌       |                                                                                                  |

# CreateContainerLogging

**Properties**

| Name      | Type             | Required | Description |
| :-------- | :--------------- | :------- | :---------- |
| axiom     | LoggingAxiom2    | ❌       |             |
| datadog   | LoggingDatadog2  | ❌       |             |
| new_relic | LoggingNewRelic2 | ❌       |             |
| splunk    | LoggingSplunk2   | ❌       |             |
| tcp       | LoggingTcp2      | ❌       |             |
| http      | LoggingHttp2     | ❌       |             |

# LoggingAxiom_2

**Properties**

| Name      | Type | Required | Description |
| :-------- | :--- | :------- | :---------- |
| host      | str  | ✅       |             |
| api_token | str  | ✅       |             |
| dataset   | str  | ✅       |             |

# LoggingDatadog_2

**Properties**

| Name    | Type               | Required | Description |
| :------ | :----------------- | :------- | :---------- |
| host    | str                | ✅       |             |
| api_key | str                | ✅       |             |
| tags    | List[DatadogTags2] | ❌       |             |

# DatadogTags_2

**Properties**

| Name  | Type | Required | Description |
| :---- | :--- | :------- | :---------- |
| name  | str  | ✅       |             |
| value | str  | ✅       |             |

# LoggingNewRelic_2

**Properties**

| Name          | Type | Required | Description |
| :------------ | :--- | :------- | :---------- |
| host          | str  | ✅       |             |
| ingestion_key | str  | ✅       |             |

# LoggingSplunk_2

**Properties**

| Name  | Type | Required | Description |
| :---- | :--- | :------- | :---------- |
| host  | str  | ✅       |             |
| token | str  | ✅       |             |

# LoggingTcp_2

**Properties**

| Name | Type | Required | Description |
| :--- | :--- | :------- | :---------- |
| host | str  | ✅       |             |
| port | int  | ✅       |             |

# LoggingHttp_2

**Properties**

| Name        | Type               | Required | Description |
| :---------- | :----------------- | :------- | :---------- |
| host        | str                | ✅       |             |
| port        | int                | ✅       |             |
| format      | HttpFormat2        | ✅       |             |
| compression | HttpCompression2   | ✅       |             |
| user        | str                | ❌       |             |
| password    | str                | ❌       |             |
| path        | str                | ❌       |             |
| headers     | List[HttpHeaders3] | ❌       |             |

# HttpFormat_2

**Properties**

| Name      | Type | Required | Description  |
| :-------- | :--- | :------- | :----------- |
| JSON      | str  | ✅       | "json"       |
| JSONLINES | str  | ✅       | "json_lines" |

# HttpHeaders_3

**Properties**

| Name  | Type | Required | Description |
| :---- | :--- | :------- | :---------- |
| name  | str  | ✅       |             |
| value | str  | ✅       |             |

# HttpCompression_2

**Properties**

| Name | Type | Required | Description |
| :--- | :--- | :------- | :---------- |
| NONE | str  | ✅       | "none"      |
| GZIP | str  | ✅       | "gzip"      |

# CreateContainerRegistryAuthentication

**Properties**

| Name       | Type                             | Required | Description |
| :--------- | :------------------------------- | :------- | :---------- |
| basic      | RegistryAuthenticationBasic1     | ❌       |             |
| gcp_gcr    | RegistryAuthenticationGcpGcr1    | ❌       |             |
| aws_ecr    | RegistryAuthenticationAwsEcr1    | ❌       |             |
| docker_hub | RegistryAuthenticationDockerHub1 | ❌       |             |
| gcp_gar    | RegistryAuthenticationGcpGar1    | ❌       |             |

# RegistryAuthenticationBasic_1

**Properties**

| Name     | Type | Required | Description |
| :------- | :--- | :------- | :---------- |
| username | str  | ✅       |             |
| password | str  | ✅       |             |

# RegistryAuthenticationGcpGcr_1

**Properties**

| Name        | Type | Required | Description |
| :---------- | :--- | :------- | :---------- |
| service_key | str  | ✅       |             |

# RegistryAuthenticationAwsEcr_1

**Properties**

| Name              | Type | Required | Description |
| :---------------- | :--- | :------- | :---------- |
| access_key_id     | str  | ✅       |             |
| secret_access_key | str  | ✅       |             |

# RegistryAuthenticationDockerHub_1

**Properties**

| Name                  | Type | Required | Description |
| :-------------------- | :--- | :------- | :---------- |
| username              | str  | ✅       |             |
| personal_access_token | str  | ✅       |             |

# RegistryAuthenticationGcpGar_1

**Properties**

| Name        | Type | Required | Description |
| :---------- | :--- | :------- | :---------- |
| service_key | str  | ✅       |             |
