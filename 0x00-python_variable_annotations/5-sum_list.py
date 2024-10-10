#!/usr/bin/env python3
"""
sum_list.py

Module for summing a list of floats.
"""

from typing import List

def sum_list(input_list: List[float]) -> float:
    """
    Sums a list of floats and returns the total.

    Parameters:
    input_list (List[float]): A list of float numbers.

    Returns:
    float: The sum of the float numbers in the input list.
    
    Example:
    >>> sum_list([1.1, 2.2, 3.3])
    6.6
    """
    return sum(input_list)
