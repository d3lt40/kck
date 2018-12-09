import numpy as np
import matplotlib.pyplot as plt
##Można to funkcjyjką ładnie rozwalić i tylko zmieniać parametry przy
#kolejnych wywołaniach, ah.

def sygnal(f, A, t, label):
    sygnal = A*np.sin(2*np.pi*f*t)
    plt.plot(t, sygnal, label = '')

sygnal(3, 1, np.linspace(0, 1, 256), 'A = 1')
sygnal(3, 5, np.linspace(0, 1, 256), 'A = 5')
sygnal(3, 10, np.linspace(0, 1, 256), 'A = 10')

plt.xlabel("Czas [s]")
plt.ylabel("Wartość funkcji [-]")
plt.legend()

plt.show()

f = 1
A = 1
t = np.linspace(0, 1, 256)
sygnal = A*np.sin(2*np.pi*f*t)

plt.plot(t, sygnal, label='f = 1')

f = 2
A = 1
t = np.linspace(0, 1, 256)
sygnal = A*np.sin(2*np.pi*f*t)

plt.plot(t, sygnal, label='f = 2')

f = 3
A = 1
t = np.linspace(0, 1, 256)
sygnal = A*np.sin(2*np.pi*f*t)

plt.plot(t, sygnal, label='f = 3')

plt.xlabel("Czas [s]")
plt.ylabel("Wartość funkcji [-]")
plt.legend()
plt.show()

f = 1
A = 1
t = np.linspace(0, 1, 256)
sygnal = A*np.sin(2*np.pi*f*t+np.pi/2)

plt.plot(t, sygnal, label='φ = π/2')

f = 1
A = 1
t = np.linspace(0, 1, 256)
sygnal = A*np.sin(2*np.pi*f*t+np.pi)

plt.plot(t, sygnal, label='φ = π')

f = 1
A = 1
t = np.linspace(0, 1, 256)
sygnal = A*np.sin(2*np.pi*f*t+3*np.pi/2)

plt.plot(t, sygnal, label='φ = 3π/2')

plt.xlabel("Czas [s]")
plt.ylabel("Wartość funkcji [-]")
plt.legend()
plt.show()


f = 3
t = np.linspace(0, 1, 210)
sygnal = np.sin(2*np.pi*f*t)
plt.plot(t, sygnal, label='f=210')

t = np.linspace(0, 1, 14)
sygnal = np.sin(2*np.pi*f*t)
plt.plot(t, sygnal, label='f=14')

t = np.linspace(0, 1, 35)
sygnal = np.sin(2*np.pi*f*t)
plt.plot(t, sygnal, 'r', label='f=35')

plt.xlabel("Czas [s]")
plt.ylabel("Wartość funkcji [-]")
plt.legend()
plt.show()
