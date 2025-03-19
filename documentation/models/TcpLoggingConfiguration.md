# TcpLoggingConfiguration

Configuration for forwarding container logs to a remote TCP endpoint

**Properties**

| Name | Type | Required | Description                                                    |
| :--- | :--- | :------- | :------------------------------------------------------------- |
| host | str  | ✅       | The hostname or IP address of the remote TCP logging endpoint  |
| port | int  | ✅       | The port number on which the TCP logging endpoint is listening |
