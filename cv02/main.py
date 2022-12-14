import numpy as np
import matplotlib.pyplot as plt
import struct


def read_vaw(filename):
    try:
        with open(filename, 'rb') as f:
            print("Reading " + filename)

            # It is RIFF?
            # riff 1-4B
            riff = f.read(4)
            if riff != b'RIFF':
                raise ValueError('File not RIFF')

            # How many bits to end of header
            # A1 5-8B
            A1 = struct.unpack('i', f.read(4))[0]

            # It is WAVE?
            # wawe - 9-12B
            wave = f.read(4)
            if wave != b'WAVE':
                raise ValueError('File not WAVE')

            # Trash
            # 13-22B
            f.read(4)
            struct.unpack('i', f.read(4))[0]
            struct.unpack('h', f.read(2))[0]

            # Number of channels
            # 23-24B
            C = struct.unpack('h', f.read(2))[0]

            # Sampling rate
            # 25-28B
            VF = struct.unpack('i', f.read(4))[0]

            # Trash
            # PB, VB - 29-34B
            struct.unpack('i', f.read(4))[0]
            struct.unpack('h', f.read(2))[0]

            # Size of sample in bytes
            # VV 35-36B
            VV = int(struct.unpack('h', f.read(2))[0])

            # Trash
            # data 37-40B
            f.read(4)

            # How many steps to end of file
            # 41-44B
            A2 = struct.unpack('i', f.read(4))[0]

            # Size of sample in bits
            size = 'b'
            VV /= 8
            if VV == 1:
                size = 'b'
            elif VV == 2:
                size = 'h'
            elif VV == 3:
                size = 'i'

            # Read signal
            SIG = []
            for i in range(0, C):
                SIG.append([])
            for i in range(0, int((A2/C)/VV)):
                for j in range(0, C):
                    SIG[j].append(struct.unpack(size, f.read(int(VV)))[0])
            t = np.arange(int((A2/C)/VV)).astype(float)/VF

            plt.figure(1)
            for i in range(0, C):
                plt.subplot(2, 2, i+1)
                plt.plot(t, SIG[i])  # Add data into plot
            plt.xlabel('t[s]')  # Name x label
            plt.ylabel('A[-]')  # Name y label
            plt.show()  # Draw graph

    except Exception as error:
        print('ERROR: ' + error.__str__())

    return None

if __name__ == '__main__':
    read_vaw("cv02_wav_01.wav")
    read_vaw("cv02_wav_02.wav")
    read_vaw("cv02_wav_03.wav")
    read_vaw("cv02_wav_04.wav")
    read_vaw("cv02_wav_05.wav")
    read_vaw("cv02_wav_06.wav")
