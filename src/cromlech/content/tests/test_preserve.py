# -*- coding: utf-8 -*-

from cromlech.content import schema
from zope.interface import Interface
from zope.schema import Choice


class IViking(Interface):
    """Defines a Norseman
    """
    rank = Choice(
        title="Rank of the viking warrior",
        default="Jarl",
        values=["Bondi", "Hersir", "Jarl", "Einherjar"])


@schema(IViking)
class Ynglingar(object):
    pass


@schema(IViking)
class JomsWarrior(object):
    rank = "Bondi"



class Slave(JomsWarrior):
    rank = "Thraell"


def test_preserve():
    """
    A `cromlech.content` content type can provide values described in the
    schema at the class level. These values are thus preserved::
    """
    harfagri = Ynglingar()
    assert harfagri.rank == "Jarl"

    gormsson = JomsWarrior()
    assert gormsson.rank == "Bondi"

    gunnar = Slave()
    assert gunnar.rank == "Thraell"
