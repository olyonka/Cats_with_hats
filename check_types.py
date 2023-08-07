from functools import wraps


def check_types(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        sig = func.__annotations__
        bound_args = func.__code__.co_varnames[:func.__code__.co_argcount]

        # Check arguments
        for arg_name, arg_value in zip(bound_args, args):
            if arg_name in sig and not isinstance(arg_value, sig[arg_name]):
                raise TypeError(f"Argument {arg_name} must be {sig[arg_name].__name__}, not {type(arg_value).__name__}")

        # Check return value
        result = func(*args, **kwargs)
        if 'return' in sig and not isinstance(result, sig['return']):
            raise TypeError(f"Return value must be {sig['return'].__name__}, not {type(result).__name__}")

        return result

    return wrapper


@check_types
def add(a: int, b: int) -> int:
    return a + b


result = add(1, 2)
print(result)

try:
    add("1", "2")
except TypeError as e:
    print(e)