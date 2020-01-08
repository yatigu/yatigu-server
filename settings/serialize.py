from functools import singledispatch
from settings.models import *


@singledispatch
def serialize(x):
    return x


@serialize.register(User)
def serialize(user):
    result = {
        'user_phone': user.user_phone,
        'user_pw': user.user_pw,
        'user_status': user.user_status,
    }
    return result
