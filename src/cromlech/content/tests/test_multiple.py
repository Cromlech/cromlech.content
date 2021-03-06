"""
Multiple schemas example
========================

Sonja The Red is a famous Hero and a Barbarian. She has a certain killing
standard but, all things considered, she's not a savage and she likes fancy
outfits. Two schemas can summarize her killing and fashion tendencies :

  >>> sonja = FemaleBarbarian()
  >>> IBarbarian.providedBy(sonja)
  True
  >>> IFemaleHero.providedBy(sonja)
  True

Sonja is maybe a barbarian, but her Redhair is one of her most priced assets.
So, if defined at the class level, the attribute will not be overriden and
the given value will be used.

  >>> sonja.nickname
  'The Red'

The other attributes of our hero are still set to default.

  >>> sonja.armor
  'metal bikini'

"""
from crom import name
from cromlech.content import schema
from zope.interface import Interface
from zope.schema import TextLine, Int, Choice


class IFemaleHero(Interface):
    """A female hero, noticeable by her armor.
    """
    armor = Choice(
        title="Armor",
        values=['metal bikini', 'leather bikini'],
        default='metal bikini')


class IBarbarian(Interface):
    """A barbarian. Usually only wearing a leather underpants.
    """
    kills = Int(
        title="Kills !",
        default=100)

    nickname = TextLine(
        title="Nickname",
        default="The Barbarian")


@name('female')
@schema(IFemaleHero, IBarbarian)
class FemaleBarbarian(object):
    """A sexy barbarian content
    """
    nickname = "The Red"
