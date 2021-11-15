def what_are_the_vars(*args, **kwarg):
    """
    Create an object of the class ObjectC, fill it with the values passedin arguments
    and return the object.
    Args:
        *args & **kwarg
    Returns:
        An object of the class ObjectC 
    """
    obj = ObjectC()
    if len(args) == 0:
        setattr(obj, "_", None)
        return obj
    for idx, value in enumerate(args):
        setattr(obj, f"var_{idx}", value)
    for key, value in kwarg.items():
        setattr(obj, key, value)
    return obj

class ObjectC(object):
    def __init__(self):
        pass

def doom_printer(obj):
    if obj is None:
        print("Error")
        print("end")
        return
    for attr in dir(obj):
        if attr[0] != "_":
            value = getattr(obj, attr)
            print("{}: {}".format(attr,value))
    print("end")

if __name__ == "__main__":
    obj = what_are_the_vars(7)
    doom_printer(obj)
    obj = what_are_the_vars("ft_lol", "Hi")
    doom_printer(obj)
    obj = what_are_the_vars()
    doom_printer(obj)
    obj = what_are_the_vars(12, "Yes", [0, 0, 0], a=10, hello="world")
    doom_printer(obj)
    obj = what_are_the_vars(42, a=10, hello="world")
    doom_printer(obj)
