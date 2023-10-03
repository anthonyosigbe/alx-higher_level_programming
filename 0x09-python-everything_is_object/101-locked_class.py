#!/usr/bin/python3
"""Specifies a class that is locked."""


class LockedClass(object):
    """Restrict the creation of new attributes in LockedClass,
    to only those named 'first_name' for users.
    """
    __slots__ = 'first_name'
