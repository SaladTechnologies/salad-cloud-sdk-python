from __future__ import annotations
from typing import List
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .inference_endpoint import InferenceEndpoint


@JsonMap({})
class InferenceEndpointsList(BaseModel):
    """Represents a list of inference endpoints

    :param items: The list of items
    :type items: List[InferenceEndpoint]
    """

    def __init__(self, items: List[InferenceEndpoint]):
        """Represents a list of inference endpoints

        :param items: The list of items
        :type items: List[InferenceEndpoint]
        """
        self.items = self._define_list(items, InferenceEndpoint)
