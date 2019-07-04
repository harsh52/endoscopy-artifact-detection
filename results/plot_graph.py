import matplotlib.pyplot as plt
import numpy as np

x,y = np.loadtxt('map.csv', unpack=True, delimiter=',')

plt.plot(x,y, marker='o')

plt.xlabel ('iteration')
plt.ylabel ('mAP')
plt.title('iteration v/s mAP curve in %')
plt.savefig('iteration_mAP_curve.png')
plt.show()


