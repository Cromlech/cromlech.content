# -*- coding: utf-8 -*-

from zope.interface import Interface, Attribute
from zope.schema import Object


class IFactory(Interface):
    """A factory is responsible for creating other components."""

    title = Attribute("The factory title.")

    description = Attribute("A brief description of the factory.")

    component = Attribute("The factored component")

    def __call__(*args, **kw):
        """Return an instance of the object we're a factory for.
        """

    def getInterfaces():
        """Get the interfaces implemented by the factory

        Returns an iterable of the interface(s) that objects created by
        this factory will provide. If the interfaces can't be resolved
        an empty iterable or None is returned instead.
        """


class IAdding(Interface):
    """Defines an abstraction layer for a creation mechanism, the 'Adding'.
    """
    def add(component):
        """Adds the component in the context.
        """


class IFactoryAdding(IAdding):
    """An IFactoryAdding extends an IAdding by adding the notion of Factory.
    """
    factory = Object(
        missing_value=None,
        title=u"The factory generating the content.",
        schema=IFactory)
