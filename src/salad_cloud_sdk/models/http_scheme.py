from enum import Enum


class HttpScheme(Enum):
    """An enumeration representing different categories.

    :cvar HTTP: "http"
    :vartype HTTP: str
    :cvar HTTPS: "https"
    :vartype HTTPS: str
    """

    HTTP = "http"
    HTTPS = "https"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(map(lambda x: x.value, HttpScheme._member_map_.values()))
