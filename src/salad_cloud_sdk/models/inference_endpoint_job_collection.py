from __future__ import annotations
from typing import List
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .inference_endpoint_job import InferenceEndpointJob


@JsonMap({})
class InferenceEndpointJobCollection(BaseModel):
    """Represents a collection of inference endpoint jobs

    :param items: The list of inference endpoint jobs.
    :type items: List[InferenceEndpointJob]
    :param page: The page number.
    :type page: int
    :param page_size: The maximum number of items per page.
    :type page_size: int
    :param total_size: The total number of items in the collection.
    :type total_size: int
    """

    def __init__(
        self,
        items: List[InferenceEndpointJob],
        page: int,
        page_size: int,
        total_size: int,
        **kwargs,
    ):
        """Represents a collection of inference endpoint jobs

        :param items: The list of inference endpoint jobs.
        :type items: List[InferenceEndpointJob]
        :param page: The page number.
        :type page: int
        :param page_size: The maximum number of items per page.
        :type page_size: int
        :param total_size: The total number of items in the collection.
        :type total_size: int
        """
        self.items = self._define_list(items, InferenceEndpointJob)
        self.page = self._define_number("page", page, ge=1, le=2147483647)
        self.page_size = self._define_number("page_size", page_size, ge=1, le=100)
        self.total_size = self._define_number(
            "total_size", total_size, ge=0, le=2147483647
        )
        self._kwargs = kwargs
