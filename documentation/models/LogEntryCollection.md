# LogEntryCollection

Represents a page of organization logs

**Properties**

| Name              | Type           | Required | Description                                                                      |
| :---------------- | :------------- | :------- | :------------------------------------------------------------------------------- |
| items             | List[LogEntry] | ✅       | A collection of log entries                                                      |
| organization_name | str            | ✅       | The organization name.                                                           |
| page_max_time     | str            | ✅       | The maximum time page boundary. This may be used when getting paginated results. |
| page_min_time     | str            | ✅       | The minimum time page boundary. This may be used when getting paginated results. |
