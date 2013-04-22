# -*- coding: utf-8 -*-

from zope.interface import Interface, Attribute


class IFactory(Interface):
    """A factory is responsible for creating other components."""

    title = Attribute("The factory title.")

    description = Attribute("A brief description of the factory.")

    def __call__(*args, **kw):
        """Return an instance of the object we're a factory for.
        """

    def getInterfaces():
        """Get the interfaces implemented by the factory

        Returns an iterable of the interface(s) that objects created by
        this factory will provide. If the interfaces can't be resolved
        an empty iterable or None is returned instead.
        """
