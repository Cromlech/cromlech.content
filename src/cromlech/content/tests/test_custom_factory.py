# -*- coding: utf-8 -*-
"""
  >>> import crom
  >>> from crom.testing import setup, teardown
  >>> from . import test_custom_factory as module

  >>> setup()
  >>> crom.configure(cromlech.content, module)

  >>> joe = IFactory.component(
  ...     name='cromlech.content.tests.test_custom_factory.Baguette')
  >>> assert isinstance(joe, BakerJoe)

  >>> assert joe.title == "Joe's bakery"
  >>> assert joe.description == 'I am a totally custom factory.'
  >>> assert list(joe.getInterfaces()) == [IBread]

  >>> joe = IFactory.component(
  ...     name='cromlech.content.tests.test_custom_factory.Baguette')
  >>> assert isinstance(joe, BakerJoe)
  
  >>> teardown()
"""

import cromlech.content
from crom import name
from cromlech.content import Factory, IFactory
from zope.interface import Interface, implementer


class IBread(Interface):
    pass


class ISweet(Interface):
    pass


class BakerJoe(Factory):
    title = "Joe's bakery"
    description = "I am a totally custom factory."


@cromlech.content.factored_component
@cromlech.content.factory(BakerJoe)
@cromlech.content.schema(IBread)
@implementer(IBread)
class Baguette(object):
    """A crusty bread.
    """


@cromlech.content.factored_component
@cromlech.content.factory(BakerJoe)
@implementer(IBread, ISweet)
@name('JoePastry')
class Croissant(object):
    """A crusty bread.
    """
