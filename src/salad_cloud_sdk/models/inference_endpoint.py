from .utils.json_map import JsonMap
from .utils.base_model import BaseModel


@JsonMap({"id_": "id"})
class InferenceEndpoint(BaseModel):
    """Represents an inference endpoint

    :param id_: The unique identifier
    :type id_: str
    :param name: The inference endpoint name
    :type name: str
    :param display_name: The inference endpoint display name
    :type display_name: str
    :param description: a brief description of the inference endpoint
    :type description: str
    :param endpoint_url: The URL of the inference endpoint
    :type endpoint_url: str
    :param readme: A markdown file containing a detailed description of the inference endpoint
    :type readme: str
    :param price_description: A description of the price
    :type price_description: str
    :param icon_image: The URL of the icon image
    :type icon_image: str
    """

    def __init__(
        self,
        id_: str,
        name: str,
        display_name: str,
        description: str,
        endpoint_url: str,
        readme: str,
        price_description: str,
        icon_image: str,
    ):
        """Represents an inference endpoint

        :param id_: The unique identifier
        :type id_: str
        :param name: The inference endpoint name
        :type name: str
        :param display_name: The inference endpoint display name
        :type display_name: str
        :param description: a brief description of the inference endpoint
        :type description: str
        :param endpoint_url: The URL of the inference endpoint
        :type endpoint_url: str
        :param readme: A markdown file containing a detailed description of the inference endpoint
        :type readme: str
        :param price_description: A description of the price
        :type price_description: str
        :param icon_image: The URL of the icon image
        :type icon_image: str
        """
        self.id_ = id_
        self.name = name
        self.display_name = self._define_str(
            "display_name",
            display_name,
            pattern="^[ ,-.0-9A-Za-z]+$",
            min_length=2,
            max_length=63,
        )
        self.description = description
        self.endpoint_url = endpoint_url
        self.readme = readme
        self.price_description = price_description
        self.icon_image = icon_image
