# -*- coding: utf-8 -*-

from .interfaces import IFactory
from grokker import validator, Directive, ArgsDirective
from zope.interface import classImplements
from zope.interface.interface import InterfaceClass
from zope.interface.interfaces import IInterface
from zope.schema import getFieldsInOrder
from zope.schema.fieldproperty import FieldProperty
from zope.schema.interfaces import IField


class Fields(object):

    def __init__(self, *ifaces):
        fields = []
        for iface in ifaces:
            if isinstance(iface, InterfaceClass):
                for name, field in getFieldsInOrder(iface):
                    fields.append((name, field))
            elif IField.providedBy(iface):
                name = iface.__name__
                if not name:
                    raise ValueError(
                        "Field has no name")
                fields.append((name, iface))

        seq = []
        byname = {}
        for name, field in fields:
            name = field.__name__
            if name in byname:
                raise ValueError("Duplicate name", name)
            seq.append(field)
            byname[name] = field

        self.__Fields_seq__ = seq
        self.__Fields_byname__ = byname

    def __len__(self):
        return len(self.__Fields_seq__)

    def __iter__(self):
        return iter(self.__Fields_seq__)

    def __getitem__(self, name):
        return self.__Fields_byname__[name]

    def get(self, name, default=None):
        return self.__Fields_byname__.get(name, default)


def schema_validator(directive_name, *ifaces):
    for iface in ifaces:
        if not IInterface.providedBy(iface):
            raise validator.GrokkerValidationError(
                "%s directive can only use interface classes. "
                "%s is not an interface class. " % (directive_name, iface))


def factory_validator(directive_name, factory):
    if factory and not IFactory.implementedBy(factory):
        raise validator.GrokkerValidationError(
            "%s directive can only use classes that implement IFactory. "
            "%s is not a valid factory. " % (directive_name, factory))


def schema_set_policy(obj, name, value):

    formfields = Fields(*value)
    for field in formfields:
        fname = field.__name__
        if not hasattr(obj, fname):
            setattr(obj, fname, FieldProperty(field))

    classImplements(obj, *value)
    setattr(obj, name, value)


schema = ArgsDirective(
    'schema', 'cromlech.content', set_policy=schema_set_policy,
    validator=schema_validator)

factory = Directive(
    'factory', 'cromlech.content', validator=factory_validator)
