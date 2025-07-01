# LogEntryQuery

Represents a query for logs

**Properties**

| Name       | Type                   | Required | Description                                                                                                                                                 |
| :--------- | :--------------------- | :------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------- |
| end_time   | str                    | ✅       | The end time of the time range                                                                                                                              |
| query      | str                    | ✅       | The query string for filtering logs                                                                                                                         |
| start_time | str                    | ✅       | The start time of the time range                                                                                                                            |
| page_size  | int                    | ❌       | The maximum number of items per page.                                                                                                                       |
| sort_order | LogEntryQuerySortOrder | ❌       | The sort order of the log entries. `asc` will sort the log entries in chronological order. `desc` will sort the log entries in reverse chronological order. |
