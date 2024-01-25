#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """Implements deletion resilient hypermedia pagination"""

        ind_dataset = self.indexed_dataset()
        datasize = len(ind_dataset)

        assert type(index) is int and type(page_size) is int
        assert page_size > 0
        assert index >= 0 and index < datasize

        curr_size = 0
        last_ind = index
        data = []

        while curr_size <= page_size and last_ind < datasize:
            try:
                data.append(ind_dataset[last_ind])
                curr_size += 1

                if curr_size < page_size:
                    last_ind += 1
                elif curr_size == page_size:
                    break

            except KeyError:
                last_ind += 1
                continue

        result = {
                 "index": index,
                 "next_index": last_ind + 1,
                 "page_size": curr_size,
                 "data": data
                 }

        return result
