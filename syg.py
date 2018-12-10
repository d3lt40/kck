import numpy as np
import matplotlib.pyplot as plt
import aseegg as ag

czestotliwosc1 = 5
czestotliwosc2 = 7
czestotliwosc3 = 3
A1=1
A2=2
A3=3
czas=1
czestP=250
t = np.linspace(0, czas, czas*czestP)
f = np.linspace(0, 256, 3*250)
sygnal=np.concatenate([np.concatenate([np.sin(A1*np.pi*czestotliwosc1*t), np.sin(A2*np.pi*czestotliwosc2*t)]), np.sin(A3*np.pi*czestotliwosc3*t)])
przefiltrowany1=ag.dolnoprzepustowy(sygnal, czestP, 1) #??
przefiltrowany2=ag.pasmowoprzepustowy(sygnal, czestP, 2)
przefiltrowany3=ag.pamowozaporowy(sygnal, czestP, 2)

transformata = ag.FFT(sygnal)

##punkt pierwszy dwawykresy
plt.subplot(2, 1, 1)
plt.plot(t, sygnal)
plt.subplot(2, 1, 2)
plt.stem(f, przefiltrowany1)
plt.xlim([0, 10])
plt.show()

##punkt 2 dwa dwawykresy
plt.subplot(2, 1, 1)
plt.plot(t, sygnal)
plt.subplot(2, 1, 2)
plt.stem(f, przefiltrowany2)
plt.xlim([0, 10])
plt.show()

## punkt 3 dwa dwawykresy
plt.subplot(2, 1, 1)
plt.plot(t, sygnal)
plt.subplot(2, 1, 2)
plt.stem(f, przefiltrowany3)
plt.xlim([0, 10])
plt.show()
