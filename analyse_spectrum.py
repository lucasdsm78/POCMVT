import pyaudio
import numpy as np
import matplotlib.pyplot as plt

# Set up PyAudio
CHUNK = 1024 # Number of audio samples per frame
FORMAT = pyaudio.paInt16 # Audio format (16-bit integer)
CHANNELS = 1 # Mono audio
RATE = 44100 # Audio sampling rate (Hz)
p = pyaudio.PyAudio()
stream = p.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK)

# Start listening and analyzing
while True:
    # Read audio frame from microphone
    data = stream.read(CHUNK)
    # Convert raw data to NumPy array of floats (-1 to 1 range)
    samples = np.frombuffer(data, dtype=np.int16).astype(np.float32) / 32767.0
    # Perform FFT to obtain frequency spectrum
    spectrum = np.fft.fft(samples)
    freqs = np.fft.fftfreq(samples.size, 1/RATE)
    # Plot frequency spectrum
    plt.clf()
    plt.plot(freqs[:len(freqs)//2], np.abs(spectrum[:len(spectrum)//2]))
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Magnitude')
    plt.ylim((0, 200))
    plt.pause(0.01)