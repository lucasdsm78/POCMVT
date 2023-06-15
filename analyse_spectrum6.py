import matplotlib.pyplot as plt
import numpy as np
from numpy import dtype
from scipy.io import wavfile

plt.rcParams['figure.dpi'] = 100
plt.rcParams['figure.figsize'] = (9, 7)

sampFreq, sound = wavfile.read('la.wav')

(dtype('int16'), 44100)

sound = sound / 2.0**15

length_in_s = sound.shape[0] / sampFreq
print(length_in_s)

time = np.arange(sound.shape[0]) / sound.shape[0] * length_in_s

signal = sound[:,0]

fft_spectrum = np.fft.rfft(signal)
freq = np.fft.rfftfreq(signal.size, d=1./sampFreq)

fft_spectrum_abs = np.abs(fft_spectrum)

fondamental = (0, 0)
for i,f in enumerate(fft_spectrum_abs):
#for i,f in enumerate(freq):
    """if f < 62 and f > 58:# (1)
        fft_spectrum[i] = 0.0
        print('------ frequency = {} Hz with amplitude {} '.format(np.round(freq[i],1),  np.round(f)))
    #if f < 21 or f > 20000:# (2)
    """
    if f>20 and f<20000:
        #fft_spectrum[i] = 0.0
        if(fondamental[1] < np.round(f)):
            fondamental = (np.round(freq[i],1), np.round(f))
        #print('frequency = {} Hz with amplitude {} '.format(np.round(freq[i],1),  np.round(f)))

print("HERE THE FONDAMENTAL : ", fondamental)

plt.plot(freq[:3000], np.abs(fft_spectrum[:3000]))
plt.xlabel("frequency, Hz")
plt.ylabel("Amplitude, units")
plt.show()