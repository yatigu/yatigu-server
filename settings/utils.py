import functools
from flask import request


def api(f):
    @functools.wraps(f)
    def deco(self, *args, **kwargs):
        if request.method in ['GET', 'DELETE']:
            data = request.args.to_dict()
        elif request.method in ['POST', 'PUT']:
            data = request.form
        else:
            data = {}
        return f(self, data, *args, **kwargs)
    return deco
