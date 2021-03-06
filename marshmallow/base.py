# -*- coding: utf-8 -*-
"""Abstract base classes.

These are necessary to avoid circular imports between core.py and fields.py.
"""
import copy


class FieldABC(object):
    """Abstract base class from which all Field classes inherit.
    """
    parent = None
    name = None

    def _format(self, value):
        raise NotImplementedError

    def _serialize(self, value, key, obj):
        raise NotImplementedError

    def _deserialize(self, value):
        raise NotImplementedError

    def __deepcopy__(self, memo):
        ret = copy.copy(self)
        return ret

    def __repr__(self):
        return '<{0} Field>'.format(self.__class__.__name__)

    __str__ = __repr__


class SchemaABC(object):
    """Abstract base class from which all Schemas inherit."""

    def dump(self, obj):
        raise NotImplementedError

    def dumps(self, obj, *args, **kwargs):
        raise NotImplementedError

    def load(self, data):
        raise NotImplementedError

    def loads(self, data):
        raise NotImplementedError
