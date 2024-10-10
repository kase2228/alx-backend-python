#!/usr/bin/env python3
"""
sum_mixed_list.py

Module for summing a mixed list of integers and floats.
"""

def sum_mixed_list(mxd_lst: list) -> float:
    """
    Sums a mixed list of integers and floats.

    Parameters:
    mxd_lst (list): A list containing both integers and floats.

    Returns:
    float: The sum of the numbers in the mixed list.
    
    Example:
    >>> sum_mixed_list([1, 2.5, 3, 4.0])
    10.5
    """
    return sum(mxd_lst)