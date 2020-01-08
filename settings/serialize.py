from functools import singledispatch
from settings.models import *


@singledispatch
def serialize(x):
    return x


@serialize.register(User)
def serialize(user):
    result = {
        'user_id': user.user_id,
        'user_pw': user.user_pw,
        'user_name': user.user_name,
    }
    return result
