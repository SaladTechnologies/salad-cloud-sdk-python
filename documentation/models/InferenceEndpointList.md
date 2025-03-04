# InferenceEndpointList

Represents a page from the collection of inference endpoints.

**Properties**

| Name       | Type                    | Required | Description                                  |
| :--------- | :---------------------- | :------- | :------------------------------------------- |
| items      | List[InferenceEndpoint] | ✅       | The list of inference endpoints.             |
| page       | int                     | ✅       | The page number.                             |
| page_size  | int                     | ✅       | The maximum number of items per page.        |
| total_size | int                     | ✅       | The total number of items in the collection. |
