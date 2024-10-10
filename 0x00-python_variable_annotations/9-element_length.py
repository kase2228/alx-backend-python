#!/usr/bin/env python3
"""
9-element_length.py

Module for calculating the lengths of elements in an iterable.
This module provides a function `element_length` that returns a list
of tuples, each containing an element and its length.
"""

from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Returns a list of tuples containing elements and their lengths.

    Parameters:
    lst (Iterable[Sequence]): An iterable containing sequences (e.g., strings, lists).

    Returns:
    List[Tuple[Sequence, int]]: A list of tuples where each tuple contains
                                 an element from the input iterable and its length.

    Example:
    >>> element_length(["hello", "world", [1, 2, 3]])
    [('hello', 5), ('world', 5), ([1, 2, 3], 3)]
    """
    return [(i, len(i)) for i in lst]
