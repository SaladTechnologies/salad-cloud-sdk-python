from __future__ import annotations
from typing import List
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .inference_endpoint_job import InferenceEndpointJob


@JsonMap({})
class InferenceEndpointJobList(BaseModel):
    """Represents a list of inference endpoint jobs

    :param items: The list of items
    :type items: List[InferenceEndpointJob]
    """

    def __init__(self, items: List[InferenceEndpointJob]):
        """Represents a list of inference endpoint jobs

        :param items: The list of items
        :type items: List[InferenceEndpointJob]
        """
        self.items = self._define_list(items, InferenceEndpointJob)
