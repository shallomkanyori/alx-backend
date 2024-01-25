#!usr/bin/env python3
"""Pagination: Simple pagination

Functions:
    index_range(page, page_size)

Classes:
    Server
"""
import csv
import math
from typing import Tuple, List


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Returns start and end index for pagination parameters.

    Args:
        page: The page to get the indices for.
        page_size: The size of each page.
    """
    return (page_size * (page - 1), page_size * page)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Returns the appropriate 'page' slice from the dataset"""

        assert type(page) is int and type(page_size) is int
        assert page > 0 and page_size > 0

        ind_range = index_range(page, page_size)
        data = self.dataset()

        return data[ind_range[0]: ind_range[1]]
