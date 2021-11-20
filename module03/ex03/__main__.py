from ColorFilter import ColorFilter
from ImageProcessor import ImageProcessor


def main():
    imgproc = ImageProcessor()
    arr = imgproc.load("./42AI.png")
    arr = ColorFilter.invert(arr)
    arr = ColorFilter.to_celluloid(arr)
    print(arr.shape)
    imgproc.display(arr)
    print(arr)


if __name__ == "__main__":
    main()
