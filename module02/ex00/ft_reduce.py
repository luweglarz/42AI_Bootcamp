from functools import reduce

def ft_reduce(function_to_apply, iterable):
    """
    Apply function of two arguments cumulatively.
    Args:
        function_to_apply: a function taking an iterable.
        iterable: an iterable object (list, tuple, iterator).
    Returns:
        A value, of same type of elements in the iterable parameter.
        None if the iterable can not be used by the function.
    """
    try:
        iterable = iter(iterable)
    except TypeError:
        print(iterable, "isn't an iterator")
        return None
    return reduce(function_to_apply, iterable)
