import numpy as np
import matplotlib.pyplot as plt
import struct
import cv2


def read_bmp(filename):
    try:
        with open(filename, 'rb') as f:
            print("Reading " + filename)

            bm = f.read(2)
            if bm != b'BM':
                raise ValueError('File not BMP')

            bites = f.read(4)
            # Trash
            f.read(12)

            width = struct.unpack('i', f.read(4))[0]
            height = struct.unpack('i', f.read(4))[0]

            # Trash
            f.read(2)

            pixelBits = struct.unpack('h', f.read(2))[0]

            # Trash
            f.read(24)

            # Size of pixel control
            if pixelBits % 4 != 0:
                raise ValueError('Pixels not right size')

            # How many empty bits
            trash = width % 4

            # 3D field for data
            bgr = np.zeros((height, width, 3))

            # Load
            for i in range(height-1, 0, -1):  # From height to zero (reversed)
                for j in range(0, width):  # From zero to max length od line
                    for k in range(0, 3):  # Read every time 3 bits
                        bgr[i][j][k] = struct.unpack('b', f.read(1))[0]
                f.read(trash)  # Delete empty bits

            # Convert to uint8
            bgr = bgr.astype('uint8')

            # Convert data into RGB
            RGB = cv2.cvtColor(bgr, cv2.COLOR_BGR2RGB)

            # Plot data into label
            #plt.plot(data, 'RGB')
            plt.figure(1)  # Number of plot
            plt.title('RGB')  # Name of plot
            plt.imshow(RGB)  # Add data into plot
            plt.show()  # Draw graph

            # Gray
            gray = cv2.cvtColor(RGB, cv2.COLOR_RGB2GRAY)


            plt.figure(2)
            plt.title('Gray')
            plt.imshow(gray, cmap='gray')
            plt.show()

            # Convert data into HSV
            hsv = cv2.cvtColor(RGB, cv2.COLOR_RGB2HSV)
            H, S, V = cv2.split(hsv)


            plt.figure(3)

            plt.subplot(221)
            plt.title("RGB")
            plt.imshow(RGB)

            plt.subplot(222)
            plt.title("H")
            plt.imshow(H)
            plt.colorbar()

            plt.subplot(223)
            plt.title("S")
            plt.imshow(S)
            plt.colorbar()

            plt.subplot(224)
            plt.title("V")
            plt.imshow(V)
            plt.colorbar()

            plt.show()

            # Convert data into YCRCB
            YCRCB = cv2.cvtColor(RGB, cv2.COLOR_BGR2YCR_CB)
            Y, Cr, Cb = cv2.split(YCRCB)

            plt.figure(4)

            plt.subplot(221)
            plt.title("RGB")
            plt.imshow(RGB)

            plt.subplot(222)
            plt.title("Y")
            plt.imshow(Y, cmap = 'gray')
            plt.colorbar()

            plt.subplot(223)
            plt.title("Cb")
            plt.imshow(Cb)
            plt.colorbar()

            plt.subplot(224)
            plt.title("Cr")
            plt.imshow(Cr)
            plt.colorbar()

            plt.show()

    except Exception as error:
        print('ERROR: ' + error.__str__())

    return None


def read_jpg_only_red(filename):
    try:
        jpg = cv2.imread(filename)
        original = cv2.cvtColor(jpg, cv2.COLOR_BGR2RGB)
        red_img = cv2.cvtColor(jpg, cv2.COLOR_BGR2RGB)
        white = np.ones(3)*255
        current = np.zeros(3)

        for i in range(0,red_img.shape[0]):
            for j in range(0,red_img.shape[1]):
                current = red_img[i][j]
                if np.sum(current) != 0:
                    tmp = current[0]/np.sum(current)
                    if tmp < 0.5:  #red
                        red_img[i][j] = white

        plt.figure(5)

        plt.subplot(121)
        plt.title('Original')
        plt.imshow(original)

        plt.subplot(122)
        plt.title('Red part')
        plt.imshow(red_img)

        plt.show()

    except Exception as error:
        print('ERROR: ' + error.__str__())

    return None


if __name__ == '__main__':
    read_bmp('cv03_objekty1.bmp')
    read_jpg_only_red('cv03_red_object.jpg')