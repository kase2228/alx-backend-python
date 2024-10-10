#!/usr/bin/env python3
"""
100-safe_first_element.py

Module for safely retrieving the first element of a sequence.
This module provides a function `safe_first_element` that returns
the first element of a sequence or None if the sequence is empty.
"""

from typing import Sequence, Any, Union

def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    Returns the first element of a sequence or None if the sequence is empty.

    Parameters:
    lst (Sequence[Any]): A sequence from which the first element will be retrieved.

    Returns:
    Union[Any, None]: The first element of the sequence or None if the sequence is empty.
    
    Example:
    >>> safe_first_element([1, 2, 3])
    1
    >>> safe_first_element([])
    None
    """
    if lst:
        return lst[0]
    else:
        return None
