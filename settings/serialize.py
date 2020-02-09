from functools import singledispatch
from settings.models import *
from typequery import GenericMethod

serialize = GenericMethod('serialize')

@serialize.of(bool)
@serialize.of(type(None))
@serialize.of(int)
@serialize.of(float)
@serialize.of(str)
def serialize(value, **kwargs):
    return value







