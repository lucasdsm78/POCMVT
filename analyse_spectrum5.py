import pyaudio
import numpy as np
import matplotlib.pyplot as plt

# Constants for audio analysis
CHUNK_SIZE = 1024  # Number of audio frames per buffer
SAMPLE_RATE = 44100  # Sampling rate of the audio device

# Initialize PyAudio
audio = pyaudio.PyAudio()

# Open a microphone stream
stream = audio.open(format=pyaudio.paInt16,
                    channels=1,
                    rate=SAMPLE_RATE,
                    input=True,
                    frames_per_buffer=CHUNK_SIZE)

# Create a figure and axes for the plot
fig, ax = plt.subplots()

# Create an array to store frequency bins
freq_bins = np.fft.rfftfreq(CHUNK_SIZE, d=1 / SAMPLE_RATE)

# Create a line object for the plot
line, = ax.plot(freq_bins, np.zeros(len(freq_bins)))

# Set the plot limits and labels
ax.set_xlim(0, SAMPLE_RATE / 2)
ax.set_ylim(0, 50)  # Adjust the y-axis limit as needed
ax.set_xlabel('Frequency (Hz)')
ax.set_ylabel('Amplitude')

# Continuously update the plot with new audio data
while True:
    # Read audio data from the stream
    audio_data = np.frombuffer(stream.read(CHUNK_SIZE), dtype=np.int16)

    # Perform fast Fourier transform (FFT) on the audio data
    spectrum = np.abs(np.fft.rfft(audio_data))

    # Update the line object with the new spectrum data
    line.set_ydata(spectrum)

    # Redraw the plot
    fig.canvas.draw()
    plt.pause(0.001)

# Close the stream and terminate PyAudio
stream.stop_stream()
stream.close()
audio.terminate()