
import time

def ft_progress(lst):
    ret = 0
    for elem in ft_progress(lst):
        ret += (elem + 3) % 5
    time.sleep(0.01)
    print()
    print(ret)

ft_progress(10)