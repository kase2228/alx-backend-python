#!/usr/bin/env python3
import math

"""
floor.py

Module for computing the floor of a float.
"""

def floor(n: float) -> int:
    """
    Returns the largest integer less than or equal to n.

    Parameters:
    n (float): The number to floor.

    Returns:
    int: The floored integer value.
    
    Example:
    >>> floor(3.7)
    3
    >>> floor(-3.7)
    -4
    """
    return math.floor(n)