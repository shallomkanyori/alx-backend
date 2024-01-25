#!usr/bin/env python3
"""Pagination: Hypermedia pagination

Functions:
    index_range(page, page_size)

Classes:
    Server
"""
import csv
import math
from typing import Tuple, List, Any, Dict


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

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict[str, Any]:
        """Returns a page with data on the next and previous pages.

        Returns the appropriate page with the page size, current page number,
        next page number, previous page number and total number of pages.
        """

        page_data = self.get_page(page, page_size)
        data_size = len(self.dataset())

        total_pages = data_size // page_size
        total_pages += 1 if data_size % page_size != 0 else 0

        data = {
                "page_size": len(page_data),
                "page": page,
                "data": page_data,
                "next_page": page + 1 if page < total_pages else None,
                "prev_page": page - 1 if page > 1 else None,
                "total_pages": total_pages
                }

        return data
