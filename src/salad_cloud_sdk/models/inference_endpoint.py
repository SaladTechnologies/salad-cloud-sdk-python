from .utils.json_map import JsonMap
from .utils.base_model import BaseModel


@JsonMap({"id_": "id"})
class InferenceEndpoint(BaseModel):
    """Represents an inference endpoint

    :param description: The detailed description of the resource.
    :type description: str
    :param display_name: The display-friendly name of the resource.
    :type display_name: str
    :param icon_url: The URL of the icon image
    :type icon_url: str
    :param id_: The inference endpoint identifier.
    :type id_: str
    :param input_schema: The input schema
    :type input_schema: str
    :param name: The inference endpoint name.
    :type name: str
    :param organization_name: The organization name.
    :type organization_name: str
    :param output_schema: The output schema
    :type output_schema: str
    :param price_description: A description of the price
    :type price_description: str
    :param readme: A markdown file containing a detailed description of the inference endpoint
    :type readme: str
    """

    def __init__(
        self,
        description: str,
        display_name: str,
        icon_url: str,
        id_: str,
        input_schema: str,
        name: str,
        organization_name: str,
        output_schema: str,
        price_description: str,
        readme: str,
        **kwargs
    ):
        """Represents an inference endpoint

        :param description: The detailed description of the resource.
        :type description: str
        :param display_name: The display-friendly name of the resource.
        :type display_name: str
        :param icon_url: The URL of the icon image
        :type icon_url: str
        :param id_: The inference endpoint identifier.
        :type id_: str
        :param input_schema: The input schema
        :type input_schema: str
        :param name: The inference endpoint name.
        :type name: str
        :param organization_name: The organization name.
        :type organization_name: str
        :param output_schema: The output schema
        :type output_schema: str
        :param price_description: A description of the price
        :type price_description: str
        :param readme: A markdown file containing a detailed description of the inference endpoint
        :type readme: str
        """
        self.description = self._define_str(
            "description", description, pattern="^.*$", max_length=1000
        )
        self.display_name = self._define_str(
            "display_name",
            display_name,
            pattern="^[ ,-.0-9A-Za-z]+$",
            min_length=2,
            max_length=63,
        )
        self.icon_url = self._define_str(
            "icon_url", icon_url, pattern="^.*$", min_length=1, max_length=2048
        )
        self.id_ = self._define_str("id_", id_)
        self.input_schema = self._define_str(
            "input_schema",
            input_schema,
            pattern="^.*$",
            min_length=1,
            max_length=100000,
        )
        self.name = self._define_str(
            "name",
            name,
            pattern="^[a-z][a-z0-9-]{0,61}[a-z0-9]$",
            min_length=2,
            max_length=63,
        )
        self.organization_name = self._define_str(
            "organization_name",
            organization_name,
            pattern="^[a-z][a-z0-9-]{0,61}[a-z0-9]$",
            min_length=2,
            max_length=63,
        )
        self.output_schema = self._define_str(
            "output_schema",
            output_schema,
            pattern="^.*$",
            min_length=1,
            max_length=100000,
        )
        self.price_description = self._define_str(
            "price_description",
            price_description,
            pattern="^.*$",
            min_length=1,
            max_length=100,
        )
        self.readme = self._define_str(
            "readme", readme, pattern="^.*$", min_length=1, max_length=100000
        )
        self._kwargs = kwargs
