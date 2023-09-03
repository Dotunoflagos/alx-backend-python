#!/usr/bin/env python3
"""
sum use of float
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Sums up the elements of a list of integers
    and floats and returns the result as a float."""
    return float(sum(mxd_lst))
