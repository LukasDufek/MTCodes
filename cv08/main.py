import cv2
import matplotlib.pyplot as plt

def funkce():
    cap = cv2.VideoCapture('cv08_video.mp4')
    NFrames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    suma1 =0
    suma2 =0
    sumFinal = 0

    for i in range(1, NFrames):
        ret1 = 'Cv08_vid/a%.3d.bmp' % i

        ret, bgr = cap.read()
        rgb = cv2.cvtColor(bgr, cv2.COLOR_BGR2RGB)

    gray = cv2.cvtColor(bgr, cv2.COLOR_BGR2GRAY).astype(float)
    for x in range(1, len(gray)):
        suma1 += gray[x]

    for y in range(1, len(gray)-1):
        suma2 += gray[y+1]

    sumFinal = abs(suma1 - suma2)
    if abs(suma1-suma2) > 850000:
        return sumFinal, True
    else:
        return sumFinal, False

        """
        plt.imshow(rgb, aspect='auto', extent=[min(t), max(t), vec1.min(), vec1.max()])
        plt.plot(t, vs, linewidth=2, color='r')
        plt.plot(t, vec1, linewidth=2, color='b')
        l = plt.axvline(x=i, linewidth=2, color='g')
        plt.axis([min(t), max(t), min(vec1), max(vec1)])
        pause(0.001)
        """

if __name__ == '__main__':
    funkce()

