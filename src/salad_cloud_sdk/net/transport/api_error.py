from ...models.utils.base_model import BaseModel
from .response import Response
from typing import Optional


class ApiError(BaseModel, Exception):
    """
    Class representing an API Error.

    :ivar Optional[int] status: The status code of the HTTP error.
    :ivar Optional[Response] response: The response associated with the error.
    """

    def __init__(
        self,
        message: Optional[str] = None,
        status: Optional[int] = None,
        response: Optional[Response] = None,
    ):
        """
        Initialize a new instance of API Error.

        :param Optional[int] status: The status code of the HTTP error.
        :param Optional[Response] response: The response associated with the error.
        """
        self.message = message
        self.status = status
        self.response = response
