#!/usr/bin/env python3
""" helper function """


def index_range(page: int, page_size: int) -> tuple:
    """ This function returns a tuple of size two containing a start index """
    return ((page - 1) * page_size, page * page_size)
