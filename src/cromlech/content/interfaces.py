# -*- coding: utf-8 -*-

from zope.interface import Interface, Attribute
from zope.component.interfaces import IObjectEvent


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


class IObjectCreatedEvent(IObjectEvent):
    """An object has been created.
    The location will usually be ``None`` for this event.
    """


class IObjectCopiedEvent(IObjectCreatedEvent):
    """An object has been copied.
    """
    original = Attribute("The original from which the copy was made")


class IObjectModifiedEvent(IObjectEvent):
    """An object has been modified"""


class IModifications(Interface) :
    """ Marker interface for descriptions of object modifications.
    """


class IAttributes(IModifications) :
    """ Describes the modified attributes of an interface.
    """
    interface = Attribute("The involved interface.")
    attributes = Attribute("A sequence of modified attributes.")


class IObjectAddedEvent(IObjectMovedEvent):
    """An object has been added to a container.
    """
    newParent = Attribute("The new location parent for the object.")
    newName = Attribute("The new location name for the object.")


class IObjectMovedEvent(IObjectAddedEvent):
    """An object has been moved.
    """
    oldParent = Attribute("The old location parent for the object.")
    oldName = Attribute("The old location name for the object.")


class IObjectRemovedEvent(IObjectMovedEvent):
    """An object has been removed from a container.
    """
