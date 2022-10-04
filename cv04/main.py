import numpy as np
import matplotlib.pyplot as plt
import cv2

def read_bmp():

    np.seterr(divide='ignore', invalid='ignore')

    #------ 1.cast----------
    original_img = cv2.imread('Cv04_porucha1.bmp')
    etalon_img = cv2.imread('Cv04_porucha1_etalon.bmp')

    repaired_img = 255 * original_img.astype(float) / etalon_img.astype(float)
    repaired_img = repaired_img.astype('uint8')

    repaired_img_RGB = cv2.cvtColor(repaired_img, cv2.COLOR_BGR2RGB)

    plt.figure(1)

    plt.subplot(121)
    plt.title('Repaired image')
    plt.imshow(repaired_img_RGB)

    plt.subplot(122)
    plt.title('Original')
    plt.imshow(cv2.cvtColor(original_img, cv2.COLOR_BGR2RGB))
    plt.show()

    #-----------2.cast----------
    original_img2 = cv2.imread('Cv04_porucha2.bmp')
    etalon_img2 = cv2.imread('Cv04_porucha2_etalon.bmp')

    repaired_img2 = (255 * original_img2.astype(float)) / etalon_img2.astype(float)
    repaired_img2 = repaired_img2.astype('uint8')

    repaired_img_RGB2 = cv2.cvtColor(repaired_img2, cv2.COLOR_BGR2RGB)

    plt.figure(2)
    plt.subplot(121)
    plt.title('Repaired image')
    plt.imshow(repaired_img_RGB2)

    plt.subplot(122)
    plt.title('Original')
    plt.imshow(cv2.cvtColor(original_img2, cv2.COLOR_BGR2RGB))
    plt.show()

def histogram():
    rentgen_original_img = cv2.imread('Cv04_rentgen.bmp')

    hist2, bin_edges = np.histogram(rentgen_original_img.flatten(),256,(0,255))
    #height, width = rentgen_original_img.shape[:2]
    #equalized_rentgen_img = np.zeros(rentgen_original_img.shape[:3])

    q = np.zeros(255)

    rentgen_gray = cv2.cvtColor(rentgen_original_img, cv2.COLOR_RGB2GRAY)
    new = np.zeros(rentgen_gray.shape)
    for i in range(0,rentgen_original_img.shape[0]):
        for j in range(0,rentgen_original_img.shape[1]):
            new[i][j] = (255/rentgen_gray.shape[0]*rentgen_gray.shape[1])*sum(hist2[:rentgen_gray[i][j]])

    plt.figure(1)
    plt.subplot(221)
    plt.title('Rentgen Original')
    plt.imshow(rentgen_original_img)

    plt.subplot(222)
    plt.title('Equalized rentgen')
    plt.imshow(new,cmap="gray")
    plt.show()

    # histogram
    plt.figure(2)
    plt.title('Rentgen Original - Histogram')
    plt.hist(rentgen_original_img.ravel(), 256, [0, 256])
    plt.show()


if __name__ == '__main__':
    read_bmp()
    histogram()
