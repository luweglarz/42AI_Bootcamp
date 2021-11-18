from ImageProcessor import ImageProcessor

def main():
    imgproc = ImageProcessor()
    arr = imgproc.load("./42AI.png")
    imgproc.display(arr)
    print(arr)


if __name__ == "__main__":
    main()