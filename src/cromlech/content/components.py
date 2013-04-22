"""Factory object
"""
from zope.interface import implementer
from zope.interface import implementedBy
from zope.interface.declarations import Implements
from .interfaces import IFactory


@implementer(IFactory)
class Factory(object):
    """Generic factory implementation.

    The purpose of this implementation is to provide a quick way of creating
    factories for classes, functions and other objects.
    """

    def __init__(self, callable, title='', description='', interfaces=None):
        self._callable = callable
        self.title = title
        self.description = description
        self._interfaces = interfaces

    def __call__(self, *args, **kw):
        return self._callable(*args, **kw)

    def getInterfaces(self):
        if self._interfaces is not None:
            spec = Implements(*self._interfaces)
            spec.__name__ = getattr(self._callable, '__name__', '[callable]')
            return spec
        return implementedBy(self._callable)

    def __repr__(self): #pragma NO COVER
        return '<%s for %s>' % (self.__class__.__name__, repr(self._callable))