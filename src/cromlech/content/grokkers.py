# -*- coding: utf-8 -*-

from .directives import factory, schema
from crom import name, registry
from cromlech.content import Factory, IFactory
from grokker import grokker, directive


@grokker
@directive(factory)
@directive(registry)
@directive(schema)
@directive(name)
def factored_component(scanner, pyname, obj, registry,
                       factory=Factory, name=None, schema=None):

    if name is None:
        name = '%s.%s' % (obj.__module__, obj.__name__)

    factoring = factory(obj, interfaces=schema)

    def register():
        registry.register(tuple(), IFactory, name, factoring)

    scanner.config.action(
        discriminator=('factory', (), IFactory, name, registry),
        callable=register
        )
