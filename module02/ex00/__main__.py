from ft_map import ft_map
from ft_filter import ft_filter
from ft_reduce import ft_reduce

def square(nb):
    return nb ** 2

def check_odd(nb):
    if nb % 2 != 0:
        return True
    return False

def multi(nb1, nb2):
    return nb1 * nb2

def main():
    test = [1, 2, 3]
    print(list(ft_map(square, test)))
    print(list(ft_filter(check_odd, test)))
    print(ft_reduce(multi, test))


if __name__ == "__main__":
    main()