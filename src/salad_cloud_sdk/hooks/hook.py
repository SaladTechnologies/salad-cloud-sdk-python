class Request:
    """
    Simplified Request class for hook demonstrations and testing.

    :ivar str method: The HTTP method (e.g., 'GET', 'POST').
    :ivar str url: The request URL.
    :ivar dict headers: Request headers.
    :ivar str body: Request body content.
    """

    def __init__(self, method, url, headers, body=""):
        """
        Initialize a Request instance.

        :param method: The HTTP method.
        :param url: The request URL.
        :param headers: Request headers.
        :param body: Request body content (defaults to empty string).
        """
        self.method = method
        self.url = url
        self.headers = headers
        self.body = body

    def __str__(self):
        """
        Return a string representation of the Request.

        :return: String representation of the request.
        """
        return f"method={self.method}, url={self.url}, headers={self.headers}, body={self.body})"


class Response:
    """
    Simplified Response class for hook demonstrations and testing.

    :ivar int status: The HTTP status code.
    :ivar dict headers: Response headers.
    :ivar body: Response body content.
    """

    def __init__(self, status, headers, body):
        """
        Initialize a Response instance.

        :param status: The HTTP status code.
        :param headers: Response headers.
        :param body: Response body content.
        """
        self.status = status
        self.headers = headers
        self.body = body

    def __str__(self):
        """
        Return a string representation of the Response.

        :return: String representation of the response.
        """
        return "Response(status={}, headers={}, body={})".format(
            self.status, self.headers, self.body
        )


class DefaultHook:
    """
    Default hook implementation with no-op methods.
    Provides lifecycle hooks for request/response interception.
    Extend this class to implement custom request/response handling logic.
    """

    def before_request(self, request: Request, **kwargs):
        """
        Hook called before a request is sent.
        Override this method to modify requests or add custom logic before execution.

        :param request: The request about to be sent.
        :param kwargs: Additional keyword arguments passed to the hook.
        """
        pass

    def after_response(self, request: Request, response: Response, **kwargs):
        """
        Hook called after a successful response is received.
        Override this method to process responses or add custom logging.

        :param request: The original request that was sent.
        :param response: The response received from the server.
        :param kwargs: Additional keyword arguments passed to the hook.
        """
        pass

    def on_error(
        self, error: Exception, request: Request, response: Response, **kwargs
    ):
        """
        Hook called when an error occurs during request execution.
        Override this method to implement custom error handling or logging.

        :param error: The error that occurred.
        :param request: The original request that was sent.
        :param response: The response received (if any).
        :param kwargs: Additional keyword arguments passed to the hook.
        """
        pass
