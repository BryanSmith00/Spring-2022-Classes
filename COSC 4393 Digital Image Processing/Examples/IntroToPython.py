import numpy as np
import cv2
from math import *

def main():
    y = np.array([1,3,2])
    print('y: ', y)
    print("Shape: ", y.shape)

    matrix = np.matrix("1 2; 3 4")
    print(matrix)
    print(matrix.shape)

    #np.array.reshape()
    #np.zeroes((3,4), dtype=int)
    #np.arange(0,16,3)
    #numpy operations are element wise

    #Loading an image
    #lenna = cv2.imread("Git.png") #Give path to the image
    #Color

    lenna = cv2.imread("Git.png", 0) #Greyscale image

    #Create a window to display image
    cv2.namedWindow("Lenna", cv2.WINDOW_AUTOSIZE)

    #Shows the image lenna in the Lenna window
    cv2.imshow("Lenna", lenna)

    #Wait forever until a key is pressed
    # if you pass a number like 10 it waits 10 seconds
    cv2.waitKey(0)

    cv2.destroyWindow("Lenna")

    print("The shape of the image is: ", lenna.shape)


def create_black_image():
    black_image = np.zeros((300,300), np.uint8)
    return black_image

def create_white_image():
    white_image = np.zeros((300,300), np.uint8)*255
    return white_image 

def create_white_box_black_backgroun():
    box = np.zeros((100,100), np.uint8)
    shape = box.shape


        
if __name__ == "__main__":
    main()
