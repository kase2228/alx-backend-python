#!/usr/bin/env python3
"""
8-make_multiplier.py

Module for creating a multiplier function.
This module provides the `make_multiplier` function, which
returns a function that multiplies a float by a specified multiplier.
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Returns a function that multiplies a float by the given multiplier.

    Parameters:
    multiplier (float): The multiplier to be used.

    Returns:
    Callable[[float], float]: A function that takes a float and returns
                               the product of that float and the multiplier.

    Example:
    >>> multiplier_by_2 = make_multiplier(2.0)
    >>> multiplier_by_2(3.0)
    6.0
    """
    def multiplier_function(value: float) -> float:
        return multiplier * value

    return multiplier_function
