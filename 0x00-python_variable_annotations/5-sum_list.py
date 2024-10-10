#!/usr/bin/env python3
"""
sum_list.py

Module for summing a list of floats. The `sum_list` function takes a list 
of float numbers as input and returns their total sum as a float, returning 
0.0 for empty lists.
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