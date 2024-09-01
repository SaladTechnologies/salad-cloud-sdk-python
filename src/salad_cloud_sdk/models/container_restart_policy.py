from enum import Enum


class ContainerRestartPolicy(Enum):
    """An enumeration representing different categories.

    :cvar ALWAYS: "always"
    :vartype ALWAYS: str
    :cvar ONFAILURE: "on_failure"
    :vartype ONFAILURE: str
    :cvar NEVER: "never"
    :vartype NEVER: str
    """

    ALWAYS = "always"
    ONFAILURE = "on_failure"
    NEVER = "never"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(
            map(lambda x: x.value, ContainerRestartPolicy._member_map_.values())
        )
