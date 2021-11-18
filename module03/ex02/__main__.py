from ScrapBooker import ScrapBooker
import numpy as np

def main():
    spb = ScrapBooker()
    arr1 = np.arange(0,25).reshape(5,5)
    # 3 is row, 1 is col
    print(spb.crop(arr1, (3,1),(1,0)))
    print()
    arr2 = np.array("A B C D E F G H I".split() * 6).reshape(-1,9)
    print(spb.thin(arr2,3,1))
    print()
    arr3 = np.array([[1, 2, 3],[1, 2, 3],[1, 2, 3]])
    print(spb.juxtapose(arr3, 3, 1))
    print()
    arr4 = np.array([[1, 2, 3],[1, 2, 3],[1, 2, 3]])
    print(spb.mosaic(arr4, (3, 5)))
if __name__ == "__main__":
    main()