#!/usr/bin/env python3
"""
6-sum_mixed_list.py

Module for summing a mixed list of integers and floats.
This module contains a function that takes a list containing
both integer and float values and returns their sum as a float.
"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Sums a mixed list of integers and floats.

    Parameters:
    mxd_lst (List[Union[int, float]]): A list containing 
    both integers and floats.

    Returns:
    float: The sum of the numbers in the mixed list.

    Example:
    >>> sum_mixed_list([5, 4, 3.14, 666, 0.99])
    679.13
    """
    return sum(mxd_lst)
