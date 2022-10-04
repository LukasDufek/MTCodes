import cv2
import numpy as np
import matplotlib.pyplot as plt

def sum_method(cap):
    NFrames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT)) 
    frames = range(1,NFrames+1)
    sum_data = np.zeros(NFrames)
    cut_data = np.zeros(NFrames)
    last_sum = 0
    treshold = 850000
    for i in range(1, NFrames):
        gray = cv2.cvtColor(cap.read()[1], cv2.COLOR_BGR2GRAY).astype(float)
        sum_value = float(np.sum(gray))
        if last_sum == 0:
            last_sum = sum_value
            sum_data[i-1] = 0
            cut_data[i-1] = 0
        else:
            data = np.abs(sum_value - last_sum)
            if data > treshold:
                last_sum = sum_value
                sum_data[i-1] = data
                cut_data[i-1] = 1
            else:
                last_sum = sum_value
                sum_data[i-1] = data
                cut_data[i-1] = 0
    plt.title("Method #1")
    plt.plot(frames, cut_data*max(sum_data), linewidth=2, color='r')
    plt.plot(frames, sum_data, linewidth=2, color='b')
    plt.axis([min(frames), max(frames), min(sum_data), max(sum_data)])
    plt.show()
    return cut_data, sum_data

def sum_diff(cap, cut_data):
    NFrames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT)) 
    frames = range(1,NFrames+1)
    last_pixel = np.zeros((288,360))
    sum_data = np.zeros(NFrames)
    for i in range(1, NFrames):
        gray = cv2.cvtColor(cap.read()[1], cv2.COLOR_BGR2GRAY).astype(float)
        if np.sum(last_pixel) > 0:
            diff = np.subtract(gray,last_pixel)
        else:
            diff = 0
        sum_diff = np.sum(np.abs(diff))
        last_pixel = gray
        sum_data[i-1] = sum_diff
    plt.title("Method #2")
    plt.plot(frames, cut_data*max(sum_data), linewidth=2, color='r')
    plt.plot(frames, sum_data, linewidth=2, color='b')
    plt.axis([min(frames), max(frames), min(sum_data), max(sum_data)])
    plt.show()

def sum_hist(cap, cut_data):
    NFrames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT)) 
    frames = range(1,NFrames+1)
    last_hist = np.zeros(256)
    sum_data = np.zeros(NFrames)
    for i in range(1, NFrames):
        gray = cv2.cvtColor(cap.read()[1], cv2.COLOR_BGR2GRAY).astype(float)
        hist = np.histogram(gray,len(last_hist),[0,len(last_hist)])[0]
        if np.sum(last_hist) > 0:
            diff = np.subtract(hist, last_hist)
        else:
            diff = 0
        sum_diff = np.sum(np.abs(diff))
        last_hist = hist
        sum_data[i-1] = sum_diff
    plt.title("Method #3")
    plt.plot(frames, cut_data*max(sum_data), linewidth=2, color='r')
    plt.plot(frames, sum_data, linewidth=2, color='b')
    plt.axis([min(frames), max(frames), min(sum_data), max(sum_data)])
    plt.show()

def sum_dct(cap,cut_data):
    NFrames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT)) 
    frames = range(1,NFrames+1)
    last_dct = np.zeros(5)
    sum_data = np.zeros(NFrames)
    for i in range(1, NFrames):
        gray = cv2.cvtColor(cap.read()[1], cv2.COLOR_BGR2GRAY).astype(float)
        dct = cv2.dct(gray) * cv2.dct(gray)
        sorted_dct = np.sort(dct.flatten())
        normalized = np.log(sorted_dct[-5:])
        if np.sum(last_dct) == 0:
            sum_data[i-1] = 0
            last_dct = normalized
        else:
            sum_data[i-1] = np.sum(np.abs(last_dct - normalized))
            last_dct = normalized
    plt.title("Method #4")
    plt.plot(frames, cut_data*max(sum_data), linewidth=2, color='r')
    plt.plot(frames, sum_data, linewidth=2, color='b')
    plt.axis([min(frames), max(frames), min(sum_data), max(sum_data)])
    plt.show()

def real_time(cap, data, cut_data):
    NFrames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT)) 
    frames = range(1,NFrames+1)
    for i in range(1, NFrames):
        ret = 'Cv08_vid/a%.3d.bmp' %i
        bgr = cv2.imread(ret)
        rgb = cv2.cvtColor(bgr, cv2.COLOR_BGR2RGB)
        plt.imshow(rgb, aspect='auto', extent = [min(frames), max(frames), data.min(), data.max()])
        plt.plot(frames, cut_data*max(data), linewidth=2, color='r')
        plt.plot(frames, data, linewidth=2, color='b')
        l = plt.axvline(x=i, linewidth=2, color='g')
        plt.axis([min(frames), max(frames), min(data), max(data)])
        plt.pause(0.001)
        plt.show()



if __name__ == '__main__':
    cut_data, data = sum_method(cv2.VideoCapture('cv08_video.mp4'))
    sum_diff(cv2.VideoCapture('cv08_video.mp4'), cut_data)
    sum_hist(cv2.VideoCapture('cv08_video.mp4'), cut_data)
    sum_dct(cv2.VideoCapture('cv08_video.mp4'), cut_data)
    real_time(cv2.VideoCapture('cv08_video.mp4'), data, cut_data)
    

