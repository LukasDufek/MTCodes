# import the necessary packages
import numpy as np
import cv2
import matplotlib.pyplot as plt


def hough(filename):

    image = cv2.imread(filename)
    output = image.copy()
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 5, 40, minRadius=25, maxRadius=50)
    if circles is not None:
        circles = np.round(circles[0, :]).astype("int")
        for (x, y, r) in circles:
            cv2.circle(output, (x, y), r, (0, 255, 0), 4)
            cv2.rectangle(output, (x - 5, y - 5), (x + 5, y + 5), (0, 128, 255), -1)
    rgb = cv2.cvtColor(gray, cv2.COLOR_GRAY2RGB)
    rgb = cv2.putText(rgb, str(len(circles)), (80,150), cv2.FONT_HERSHEY_SIMPLEX, 5, (0,0,255), 2, cv2.LINE_AA)
    cv2.imshow('test', rgb)
    cv2.waitKey(0)

    print(len(circles))

def erode_img(img):
    img_grayscale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # normalise to 0,1
    img_grayscale = np.array(img_grayscale) / 255

    # preparation for erosion
    anchor = np.ones((len(img_grayscale), len(img_grayscale[0])), np.uint8)
    kernel = np.ones((3, 3), np.uint8)

    # erosion
    counter = 0
    while np.sum(img_grayscale) > 1:
        img_grayscale = cv2.erode(img_grayscale, kernel, anchor, (-1, -1), 1)
        counter += 1
    position = np.where(img_grayscale == 1)

    return position[1][0], position[0][0], counter, img_grayscale


def dilate_img(counter, img):
    kernel = np.ones((3, 3), np.uint8)
    dilated = img
    for i in range(counter):
        dilated = cv2.dilate(dilated, kernel, iterations=1)
    return dilated

def encode():
    # load img
    img = cv2.imread("Cv11_merkers.bmp")

    # shape

    height = img.shape[0]
    width = img.shape[1]
    divide_height = height // 2

    # cut in half
    img1 = img[:divide_height, :]
    img2 = img[divide_height:, :]

    # erosion of img halves
    pos1 = erode_img(img1)
    pos2 = erode_img(img2)

    '''
    print("First half")
    print(f"X: {pos1[0]} Y: {pos1[1]}")
    print("Second half")
    print(f"X: {pos2[0]} Y: {pos2[1]}")
    '''

    # dilatation of img halves
    dil1 = dilate_img(pos1[2], pos1[3])
    dil2 = dilate_img(pos2[2], pos2[3])

    # connect img back to one
    final = np.zeros((img.shape[0], img.shape[1]))
    final[:divide_height, :] = dil1
    final[divide_height:, :] = dil2
    plt.imshow(final, cmap="gray")
    plt.show()


if __name__ == '__main__':
    hough('Cv11_c01.bmp')
    hough('Cv11_c02.bmp')
    hough('Cv11_c03.bmp')
    hough('Cv11_c04.bmp')
    hough('Cv11_c05.bmp')
    hough('Cv11_c06.bmp')

    encode()


