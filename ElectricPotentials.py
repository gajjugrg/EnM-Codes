
import math
import matplotlib.pyplot as plt
import numpy as np




'''Experiment 1'''

z_sq  = np.array([190096, 111556, 297025, 133590.25, 162409, 210681, 183612.25])
dz_sq = np.array([0.5184, 0.2025, 0.5625, 0.49, 0.36, 0.4624, 0.4096])
# '''Experiment 2'''
# z_sq  = np.array([104006.25, 79806.25, 116622.25, 127092.25, 69432.25, 30625, 14520.25])
# dz_sq = np.array([0.36,	0.49, 0.64, 0.4225, 0.81, 0.49, 0.5625])
'''Experiment 2 Brian's Group'''
# z_sq  = np.array([284515.56, 341289.64, 403225, 580644, 790321, 1032256, 1306449])
# dz_sq = np.array([357.21, 353.44, 380.25, 585.64, 660.49, 670.81, 691.69])
m, b = np.polyfit(z_sq, dz_sq, 1)
print(m)
print(b)
print(np.sqrt(np.abs(m)))
print(np.sqrt(b))
print((np.sqrt(np.abs(m))*np.sqrt(b)))
fig, ax = plt.subplots()
plt.plot(z_sq, dz_sq, 'o')
plt.plot(z_sq,  m*z_sq + b, color='navy', alpha = 0.3, label = r'$(d(z))^2= $' + str( round(m, 9)) + '$z^2 + $' + str( round(b, 9)))
ax.yaxis.set_ticks_position('both')
ax.xaxis.set_ticks_position('both')
ax.set_xlabel(r'$z^2 \, \, [mm^2]$')
ax.set_ylabel(r'$(d(z))^2 \,\,[mm^2]$')
ax.set_title(r'$(d(z))^2\, vs. \, z^2$, straightline form $(y = mx + c)$: $ (d(z))^2 = \theta^2 z^2 + d_0^2$')
plt.legend()
fig.tight_layout()
plt.grid()
plt.show()

