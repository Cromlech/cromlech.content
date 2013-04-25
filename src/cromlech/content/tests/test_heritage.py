# -*- coding: utf-8 -*-

from cromlech.content import schema
from zope.interface import Interface
from zope.schema import TextLine


class IMythologicalHero(Interface):
    """A hero that transcended History.
    """
    homecity = TextLine(
        title=u"Name of the home city of the Hero",
        required=True,
        default=u"Babylon")


@schema(IMythologicalHero)
class Hero(object):
    pass


class AssyrianHero(Hero):
    pass


class MesopotamianGod(AssyrianHero):
    pass


def test_inheritage():
    """Test that inheritance keeps schema.
    """
    gilgamesh = MesopotamianGod()
    assert gilgamesh.homecity == u'Babylon'
    assert schema.get(gilgamesh) == (IMythologicalHero,)
