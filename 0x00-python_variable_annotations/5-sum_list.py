#!/usr/bin/env python3
"""
sum_list.py

Modlue that returns the sum of provided list of floats as a float.
"""
def sum_list(input_list: list[float]) -> float:
    """
    Sums a list of floats and returns the total.

    Parameters:
    input_list (list[float]): A list of float numbers.

    Returns:
    float: The sum of the float numbers in the input list.
    
    Example:
    >>> sum_list([1.1, 2.2, 3.3])
    6.6
    """
    return sum(input_list)