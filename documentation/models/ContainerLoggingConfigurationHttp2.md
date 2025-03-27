# ContainerLoggingConfigurationHttp_2

Configuration for sending container logs to an HTTP endpoint. Defines how logs are formatted, compressed, and transmitted.

**Properties**

| Name        | Type                             | Required | Description                                                    |
| :---------- | :------------------------------- | :------- | :------------------------------------------------------------- |
| host        | str                              | ✅       | The hostname or IP address of the HTTP logging endpoint        |
| port        | int                              | ✅       | The port number of the HTTP logging endpoint (1-65535)         |
| format      | ContainerLoggingHttpFormat       | ✅       | The format in which logs will be delivered                     |
| compression | ContainerLoggingHttpCompression  | ✅       | The compression algorithm to apply to logs before transmission |
| user        | str                              | ❌       | Optional username for HTTP authentication                      |
| password    | str                              | ❌       | Optional password for HTTP authentication                      |
| path        | str                              | ❌       | Optional URL path for the HTTP endpoint                        |
| headers     | List[ContainerLoggingHttpHeader] | ❌       | Optional HTTP headers to include in log transmission requests  |
