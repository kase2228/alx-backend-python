#!/usr/bin/env python3
"""
concat.py

This module provides a simple function to concatenate two strings.
"""


def concat(str1: str, str2: str) -> str:
    """
    Concatenates two strings and returns the result.

    Parameters:
    str1 (str): The first string.
    str2 (str): The second string.

    Returns:
    str: The concatenated result of str1 and str2.

    Example:
    >>> concat("Hello, ", "World!")
    'Hello, World!'
    """
    return str1 + str2
