def ft_filter(function_to_apply, iterable):
    """
    Filter the result of function apply to all elements of the iterable.
    Args:
        function_to_apply: a function taking an iterable.
        iterable: an iterable object (list, tuple, iterator).
    Returns:
        An iterable.
        None if the iterable can not be used by the function.
    """
    try:
        iterable = iter(iterable)
    except TypeError:
        print(iterable, "isn't an iterator")
        return None
    return filter(function_to_apply, iterable)
