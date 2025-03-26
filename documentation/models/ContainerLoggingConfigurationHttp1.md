# ContainerLoggingConfigurationHttp_1

Configuration for sending container logs to an HTTP endpoint. Defines how logs are formatted, compressed, and transmitted.

**Properties**

| Name        | Type                                          | Required | Description                                                    |
| :---------- | :-------------------------------------------- | :------- | :------------------------------------------------------------- |
| host        | str                                           | ✅       | The hostname or IP address of the HTTP logging endpoint        |
| port        | int                                           | ✅       | The port number of the HTTP logging endpoint (1-65535)         |
| format      | ContainerHttpLoggingConfigurationFormat1      | ✅       | The format in which logs will be delivered                     |
| headers     | List[ContainerLoggingHttpHeader]              | ✅       | Optional HTTP headers to include in log transmission requests  |
| compression | ContainerHttpLoggingConfigurationCompression1 | ✅       | The compression algorithm to apply to logs before transmission |
| user        | str                                           | ❌       | Optional username for HTTP authentication                      |
| password    | str                                           | ❌       | Optional password for HTTP authentication                      |
| path        | str                                           | ❌       | Optional URL path for the HTTP endpoint                        |

# ContainerHttpLoggingConfigurationFormat_1

The format in which logs will be delivered

**Properties**

| Name      | Type | Required | Description  |
| :-------- | :--- | :------- | :----------- |
| JSON      | str  | ✅       | "json"       |
| JSONLINES | str  | ✅       | "json_lines" |

# ContainerHttpLoggingConfigurationCompression_1

The compression algorithm to apply to logs before transmission

**Properties**

| Name | Type | Required | Description |
| :--- | :--- | :------- | :---------- |
| NONE | str  | ✅       | "none"      |
| GZIP | str  | ✅       | "gzip"      |
