import cv2
from numpy import linalg as LA
import numpy as np
from matplotlib import pyplot as plt


def convertImageToMonochromo():
    img = cv2.imread('Cv09_obr.bmp')

    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY).astype(float)
    height = img.shape[0]
    width = img.shape[1]

    B = img[:, :, 0].flatten()
    G = img[:, :, 1].flatten()
    R = img[:, :, 2].flatten()

    ex = np.mean([R, G, B], axis=0)

    W = np.column_stack((R - ex, G - ex, B - ex))

    eig_val, eig_vec = LA.eig(np.cov(W.T))
    eig_p = []

    for i in range(0, len(eig_val)):
        eig_p.append((np.abs(eig_val[i]), eig_vec[:, i]))

    eig_p.sort()
    eig_p.reverse()
    Ep = np.column_stack((eig_p[2][1], eig_p[1][1], eig_p[0][1]))

    E = np.dot(W, Ep)
    k1 = (E.T[0] + ex).reshape(height, width)
    k2 = (E.T[1] + ex).reshape(height, width)
    k3 = (E.T[2] + ex).reshape(height, width)

    # originalni
    plt.subplot(231)
    plt.title("original")
    plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    # prevedeno na gray
    plt.subplot(233)
    plt.title("gray")
    plt.imshow(gray, cmap='gray')
    # prvni komponenta
    plt.subplot(234)
    plt.title("component1")
    plt.imshow(k1, cmap='gray')
    # druha komponenta
    plt.subplot(235)
    plt.title("component2")
    plt.imshow(k2, cmap='gray')
    # treti komponenta
    plt.subplot(236)
    plt.title("component3")
    plt.imshow(k3, cmap='gray')

    plt.show()

if __name__ == '__main__':
    convertImageToMonochromo()



