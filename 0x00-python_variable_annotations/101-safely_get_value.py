#!/usr/bin/env python3
"""
101-safely_get_value.py

Module for retrieving a value from a dictionary safely.
"""

from typing import Mapping, Any, Union, TypeVar

T = TypeVar('T')


def safely_get_value(dct: Mapping[str, T], key: Any, default: Union[T, None] = None) -> Union[T, None]:
    """
    Retrieves a value from a dictionary by key, or returns a default value if the key is not found.

    Parameters:
    dct (Mapping[str, T]): The dictionary to search.
    key (Any): The key to look up.
    default (Union[T, None]): The value to return if the key is absent.

    Returns:
    Union[T, None]: The found value or the default.
    """
    if key in dct:
        return dct[key]
    else:
        return default
