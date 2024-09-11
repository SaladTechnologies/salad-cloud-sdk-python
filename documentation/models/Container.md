# Container

Represents a container

**Properties**

| Name                  | Type                            | Required | Description                                  |
| :-------------------- | :------------------------------ | :------- | :------------------------------------------- |
| image                 | `str`                           | ✅       |                                              |
| resources             | `ContainerResourceRequirements` | ✅       | Represents a container resource requirements |
| command               | `List[str]`                     | ✅       |                                              |
| priority              | `ContainerGroupPriority`        | ❌       |                                              |
| size                  | `int`                           | ❌       |                                              |
| hash                  | `str`                           | ❌       |                                              |
| environment_variables | `dict`                          | ❌       |                                              |
| logging               | `ContainerLogging`              | ❌       |                                              |

# ContainerLogging

**Properties**

| Name      | Type               | Required | Description |
| :-------- | :----------------- | :------- | :---------- |
| axiom     | `LoggingAxiom1`    | ❌       |             |
| datadog   | `LoggingDatadog1`  | ❌       |             |
| new_relic | `LoggingNewRelic1` | ❌       |             |
| splunk    | `LoggingSplunk1`   | ❌       |             |
| tcp       | `LoggingTcp1`      | ❌       |             |
| http      | `LoggingHttp1`     | ❌       |             |

# LoggingAxiom_1

**Properties**

| Name      | Type  | Required | Description |
| :-------- | :---- | :------- | :---------- |
| host      | `str` | ✅       |             |
| api_token | `str` | ✅       |             |
| dataset   | `str` | ✅       |             |

# LoggingDatadog_1

**Properties**

| Name    | Type                 | Required | Description |
| :------ | :------------------- | :------- | :---------- |
| host    | `str`                | ✅       |             |
| api_key | `str`                | ✅       |             |
| tags    | `List[DatadogTags1]` | ❌       |             |

# DatadogTags_1

**Properties**

| Name  | Type  | Required | Description |
| :---- | :---- | :------- | :---------- |
| name  | `str` | ✅       |             |
| value | `str` | ✅       |             |

# LoggingNewRelic_1

**Properties**

| Name          | Type  | Required | Description |
| :------------ | :---- | :------- | :---------- |
| host          | `str` | ✅       |             |
| ingestion_key | `str` | ✅       |             |

# LoggingSplunk_1

**Properties**

| Name  | Type  | Required | Description |
| :---- | :---- | :------- | :---------- |
| host  | `str` | ✅       |             |
| token | `str` | ✅       |             |

# LoggingTcp_1

**Properties**

| Name | Type  | Required | Description |
| :--- | :---- | :------- | :---------- |
| host | `str` | ✅       |             |
| port | `int` | ✅       |             |

# LoggingHttp_1

**Properties**

| Name        | Type                 | Required | Description |
| :---------- | :------------------- | :------- | :---------- |
| host        | `str`                | ✅       |             |
| port        | `int`                | ✅       |             |
| format      | `HttpFormat1`        | ✅       |             |
| compression | `HttpCompression1`   | ✅       |             |
| user        | `str`                | ❌       |             |
| password    | `str`                | ❌       |             |
| path        | `str`                | ❌       |             |
| headers     | `List[HttpHeaders1]` | ❌       |             |

# HttpFormat_1

**Properties**

| Name      | Type  | Required | Description  |
| :-------- | :---- | :------- | :----------- |
| JSON      | `str` | ✅       | "json"       |
| JSONLINES | `str` | ✅       | "json_lines" |

# HttpHeaders_1

**Properties**

| Name  | Type  | Required | Description |
| :---- | :---- | :------- | :---------- |
| name  | `str` | ✅       |             |
| value | `str` | ✅       |             |

# HttpCompression_1

**Properties**

| Name | Type  | Required | Description |
| :--- | :---- | :------- | :---------- |
| NONE | `str` | ✅       | "none"      |
| GZIP | `str` | ✅       | "gzip"      |
