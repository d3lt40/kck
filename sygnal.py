import numpy as np
import matplotlib.pyplot as plt
##Można to funkcjyjką ładnie rozwalić i tylko zmieniać parametry przy
#kolejnych wywołaniach, ah.
f = 3
A = 1
t = np.linspace(0, 1, 256)
sygnal = A*np.sin(2*np.pi*f*t)

plt.plot(t, sygnal, label='A = 1')

f = 3
A = 5
t = np.linspace(0, 1, 256)
sygnal = A*np.sin(2*np.pi*f*t)

plt.plot(t, sygnal, label='A = 5')

f = 3
A = 10
t = np.linspace(0, 1, 256)
sygnal = A*np.sin(2*np.pi*f*t)

plt.plot(t, sygnal, label='A = 10')

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

Amplituda sygnału to zakres wartości jakie przyjmuje sygnał.
Na rys. 1 zaprezentowano 3 sygnały o różnych amplitudachself.
Częstotliwość sygnału mówi o licznie wystąpienia maksymalnej i minimalnej wartości w określonym czasie.
Na rys. 2 zaprezentowano sygnały o różnych częstotliwościach
Przesunięcie fazowe to wartość jaką funkcja przyjmuje dla argumentu t=0.
Na rys. 3 zaprezentowano 3 sygnały o różnych przesunięciach fazowych.
Próbkowanie to reprezentowanie sygnału ciągłego za pomocą wartości nazywanych próbkamiself.
Częstotliwość próbkowania to określenie jak często mierzony jest sygnał.
Na rys. 4 zaprezentowano 3 częstotliwości próbkowania tego samego sygnału. 
