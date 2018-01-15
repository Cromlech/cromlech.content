"""

Initialisation
==============

  >>> import crom
  >>> from crom.testing import setup, teardown
  >>> from . import test_simple

  >>> setup()
  >>> crom.configure(cromlech.content, test_simple)

Schema
======

This content is getting a base interface and a base schema.
It means that the attributes are set by default on the content type.
Of course, the basic fields validations are respected.

  >>> mongo = Dummy()
  >>> IDummySchema.providedBy(mongo)
  True
  >>> mongo.title
  ''
  >>> mongo.title = b'a vast bowl of pus'
  Traceback (most recent call last):
  ...
  zope.schema._bootstrapinterfaces.WrongType: (b'a vast bowl of pus', <class 'str'>, 'title')

  >>> mongo.title = 'Oh... it makes me mad... mad!'
  >>> mongo.title
  'Oh... it makes me mad... mad!'


Factory
=======

In order to get an abstract and generic way to handle the content types,
`cromlech.content` provides a factory system that permits to instanciate your
objects.

Further, if no factory is explicitly declared, one is automatically generated
and registered, using the package path and class name as an identifier.

  >>> from cromlech.content import IFactory
  >>> myfactory = IFactory.component(
  ...     name='cromlech.content.tests.test_simple.Dummy')

  >>> myfactory.component
  <class 'cromlech.content.tests.test_simple.Dummy'>

  >>> print(list(myfactory.getInterfaces()))
  [<InterfaceClass cromlech.content.tests.test_simple.IDummySchema>]

The factory describes the generated content::

  >>> print(str(myfactory))
  <Factory for <class 'cromlech.content.tests.test_simple.Dummy'>>

  >>> from zope.interface.verify import verifyObject
  >>> verifyObject(IFactory, myfactory)
  True


Cleaning
========

  >>> teardown()


"""

import cromlech.content
from zope.schema import TextLine
from zope.interface import Interface


class IDummySchema(Interface):
    title = TextLine(
        title="Title",
        required=True,
        default='')


@cromlech.content.schema(IDummySchema)
@cromlech.content.factored_component
class Dummy(object):
    """A very simple content
    """
    pass
