import wave
import numpy as np

wav_obj = wave.open('test.wav', 'rb')

sample_freq = wav_obj.getframerate()
n_samples = wav_obj.getnframes()
print(n_samples)

t_audio = n_samples / sample_freq


n_channels = wav_obj.getnchannels()

signal_wave = wav_obj.readframes(n_samples)

signal_array = np.frombuffer(signal_wave, dtype=np.int16)


