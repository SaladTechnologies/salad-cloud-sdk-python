from enum import Enum


class LogEntryQuerySortOrder(Enum):
    """An enumeration representing different categories.

    :cvar DESC: "desc"
    :vartype DESC: str
    :cvar ASC: "asc"
    :vartype ASC: str
    """

    DESC = "desc"
    ASC = "asc"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(
            map(lambda x: x.value, LogEntryQuerySortOrder._member_map_.values())
        )
