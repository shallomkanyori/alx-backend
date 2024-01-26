#!/usr/bin/env python3
"""Pagination: Simple helper function

Functions:
    index_range(page, page_size)
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Returns start and end index for pagination parameters.

    Args:
        page: The page to get the indices for.
        page_size: The size of each page.
    """
    return (page_size * (page - 1), page_size * page)
