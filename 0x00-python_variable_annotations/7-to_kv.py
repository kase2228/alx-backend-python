#!/usr/bin/env python3
"""
to_kv.py

Module for converting a string and a number into a tuple.
This module provides a function `to_kv` that takes a string
and a number (int or float), returning a tuple with the string
and the square of the number.
"""

from typing import Union, Tuple

def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Converts a string and a number into a tuple.

    Parameters:
    k (str): A string.
    v (Union[int, float]): An integer or float number.

    Returns:
    Tuple[str, float]: A tuple containing the string k and the square of v.
    
    Example:
    >>> to_kv("eggs", 3)
    ('eggs', 9)
    >>> to_kv("school", 0.02)
    ('school', 0.0004)
    """
    return (k, float(v ** 2))
