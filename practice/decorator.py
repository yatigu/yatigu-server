import functools


def deco(f):
    @functools.wraps(f)
    def ddeco(*args, **kwargs):
        print(args)
        return f(args[0].get('name'))
    return ddeco

data = {
        'name': 'yeonsoo'
    }
@deco
def test_func(data):
    print(data)

test_func(data)
