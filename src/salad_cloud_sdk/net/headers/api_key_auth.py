from typing import Dict

from .base_header import BaseHeader


class ApiKeyAuth(BaseHeader):
    """
    A class for handling API key authentication in headers.

    :ivar str _api_key: The API key.
    :ivar str _api_key_header: The header field for the API key.
    """

    _api_key: str
    _api_key_header: str

    def __init__(self, api_key: str, api_key_header="Salad-Api-Key"):
        """
        Initialize the ApiKeyAuth instance.

        :param api_key: The API key.
        :type api_key: str
        :param api_key_header: The header field for the API key.
        :type api_key_header: str
        """
        self._api_key = api_key
        self._api_key_header = api_key_header

    def set_value(self, value: str) -> None:
        """
        Set the value of the API key.

        :param value: The new value of the API key.
        :type value: str
        """
        self._api_key = value

    def get_headers(self) -> Dict[str, str]:
        """
        Get the headers with the API key field set to the API key.

        :return: A dictionary with the API key field set to the API key.
        :rtype: Dict[str, str]
        """
        return {self._api_key_header: self._api_key}
