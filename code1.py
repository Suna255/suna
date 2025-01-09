import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
def buat_papan_catur(n):
    papan_catur=np.zeros((n, n),dtype=int)
    papan_catur[1::2, ::2]=1
    papan_catur[::2, 1::2]=1
    return papan_catur
n=8
papan= buat_papan_catur(n)
plt.matshow(papan,cmap='gray')
plt.xticks([])
plt.yticks([])
plt.show()