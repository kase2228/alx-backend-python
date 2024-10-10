#!/usr/bin/env python3
"""
102-type_checking.py

Module for zooming into an array by a given factor.
"""

from typing import Tuple, List, Any

def zoom_array(lst: Tuple[Any, ...], factor: int = 2) -> Tuple[Any, ...]:
    """
    Zooms into an array by a specified factor.

    Parameters:
    lst (Tuple[Any, ...]): The input tuple to zoom in on.
    factor (int): The number of times to repeat each element (default is 2).

    Returns:
    Tuple[Any, ...]: A tuple with the zoomed-in elements.
    """
    zoomed_in: List[Any] = [
        item for item in lst
        for _ in range(factor)
    ]
    return tuple(zoomed_in)


array = (12, 72, 91)  # Changed to a tuple for type compatibility

zoom_2x = zoom_array(array)
zoom_3x = zoom_array(array, 3)  # Ensure this is an int
