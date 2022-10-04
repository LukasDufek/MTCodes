import numpy as np
import matplotlib.pyplot as plt
import struct

with open('cv01_dobryden.wav', 'rb') as f:
 #head
 data = f.read(4)
 print(data)
 A1 = struct.unpack('i', f.read(4))[0]
 print(A1)
 #print(f)


 f.read(16)
 VF = struct.unpack('i', f.read(4))[0]
 print(VF)


 f.read(12)
 A2 = struct.unpack('i', f.read(4))[0]
 print(A2)


 #data
 SIG = np.zeros(A2)
 for i in range(0, A2):
  SIG[i] = struct.unpack('B', f.read(1))[0]


t = np.arange(A2).astype(float)/VF
plt.plot(t, SIG)
plt.xlabel('t[s]')
plt.ylabel('A[-]')
plt.show()

