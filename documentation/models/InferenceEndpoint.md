# InferenceEndpoint

Represents an inference endpoint

**Properties**

| Name              | Type  | Required | Description                                                                 |
| :---------------- | :---- | :------- | :-------------------------------------------------------------------------- |
| id\_              | `str` | ✅       | The unique identifier                                                       |
| name              | `str` | ✅       | The inference endpoint name                                                 |
| display_name      | `str` | ✅       | The inference endpoint display name                                         |
| description       | `str` | ✅       | a brief description of the inference endpoint                               |
| endpoint_url      | `str` | ✅       | The URL of the inference endpoint                                           |
| readme            | `str` | ✅       | A markdown file containing a detailed description of the inference endpoint |
| price_description | `str` | ✅       | A description of the price                                                  |
| icon_image        | `str` | ✅       | The URL of the icon image                                                   |
