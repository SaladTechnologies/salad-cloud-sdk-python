from typing import Any, Dict


class BaseHeader:
    """
    Base class for authentication header implementations.
    Defines the interface for setting authentication values and retrieving HTTP headers.
    """

    def set_value(self, value: Any) -> None:
        """
        Set the authentication value.
        Subclasses should override this method to store authentication credentials.

        :param value: The authentication value to set.
        """
        pass

    def get_headers(self) -> Dict[str, str]:
        """
        Get the HTTP headers containing authentication information.
        Subclasses should override this method to return appropriate authentication headers.

        :return: A dictionary of HTTP headers with authentication data.
        """
        pass
