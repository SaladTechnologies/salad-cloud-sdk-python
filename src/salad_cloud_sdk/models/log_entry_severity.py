from enum import Enum


class LogEntrySeverity(Enum):
    """An enumeration representing different categories.

    :cvar DEBUG: "debug"
    :vartype DEBUG: str
    :cvar INFO: "info"
    :vartype INFO: str
    :cvar NOTICE: "notice"
    :vartype NOTICE: str
    :cvar WARNING: "warning"
    :vartype WARNING: str
    :cvar ERROR: "error"
    :vartype ERROR: str
    :cvar CRITICAL: "critical"
    :vartype CRITICAL: str
    :cvar ALERT: "alert"
    :vartype ALERT: str
    :cvar EMERGENCY: "emergency"
    :vartype EMERGENCY: str
    """

    DEBUG = "debug"
    INFO = "info"
    NOTICE = "notice"
    WARNING = "warning"
    ERROR = "error"
    CRITICAL = "critical"
    ALERT = "alert"
    EMERGENCY = "emergency"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(map(lambda x: x.value, LogEntrySeverity._member_map_.values()))
