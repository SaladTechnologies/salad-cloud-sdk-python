# InferenceEndpoint

Represents an inference endpoint

**Properties**

| Name              | Type | Required | Description                                                                 |
| :---------------- | :--- | :------- | :-------------------------------------------------------------------------- |
| id\_              | str  | ✅       | The inference endpoint identifier.                                          |
| name              | str  | ✅       | The inference endpoint name.                                                |
| organization_name | str  | ✅       | The organization name.                                                      |
| display_name      | str  | ✅       | The display-friendly name of the resource.                                  |
| description       | str  | ✅       | The detailed description of the resource.                                   |
| readme            | str  | ✅       | A markdown file containing a detailed description of the inference endpoint |
| price_description | str  | ✅       | A description of the price                                                  |
| icon_url          | str  | ✅       | The URL of the icon image                                                   |
| input_schema      | str  | ✅       | The input schema                                                            |
| output_schema     | str  | ✅       | The output schema                                                           |
