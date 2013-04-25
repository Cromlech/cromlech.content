# -*- coding: utf-8 -*-

from cromlech.content import schema
from zope.interface import Interface
from zope.schema import Choice


class IViking(Interface):
    """Defines a Norseman
    """
    rank = Choice(
        title=u"Rank of the viking warrior",
        default=u"Jarl",
        values=[u"Bondi", u"Hersir", u"Jarl", u"Einherjar"])


@schema(IViking)
class Ynglingar(object):
    pass


@schema(IViking)
class JomsWarrior(object):
    rank = u"Bondi"



class Slave(JomsWarrior):
    rank = u"Thraell"


def test_preserve():
    """
    A `cromlech.content` content type can provide values described in the
    schema at the class level. These values are thus preserved::
    """
    harfagri = Ynglingar()
    assert harfagri.rank == u'Jarl'

    gormsson = JomsWarrior()
    assert gormsson.rank == u'Bondi'

    gunnar = Slave()
    assert gunnar.rank == u"Thraell"
