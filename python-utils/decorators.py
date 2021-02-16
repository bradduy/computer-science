import functools

def mimicDecorator(func):

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print('decorator is running')
        result = func(*args, **kwargs)
        return result
    return wrapper


@mimicDecorator
def doSomeThing(x):
    return x*3

result = doSomeThing(3.3)
print(result)
print(doSomeThing.__name__)


def repeat(numTimes):
    def decoratorRepeat(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range (numTimes):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decoratorRepeat

@repeat(numTimes=5)
def greet(name):
    print(f'hello {name}')

greet('Duy')
