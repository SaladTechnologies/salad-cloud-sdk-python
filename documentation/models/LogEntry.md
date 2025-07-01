# LogEntry

**Properties**

| Name           | Type             | Required | Description                                |
| :------------- | :--------------- | :------- | :----------------------------------------- |
| receive_time   | str              | ✅       | The time when the log entry was received   |
| resource       | LogEntryResource | ✅       | The resource associated with the log entry |
| severity       | LogEntrySeverity | ✅       | The severity level of the log entry        |
| time           | str              | ✅       | The timestamp of the log entry             |
| json_log       | dict             | ❌       | The log message in JSON format.            |
| parent_span_id | str              | ❌       | The parent span ID of the log entry        |
| span_id        | str              | ❌       | The span ID of the log entry               |
| text_log       | str              | ❌       | The log message in text format.            |
| trace_id       | str              | ❌       | The trace ID of the log entry              |
