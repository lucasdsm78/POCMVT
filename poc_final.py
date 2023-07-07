import pyaudio
import numpy as np
import time
from scipy import signal
from music21 import converter, instrument, note, stream, environment
import os
from gen_score import *

# setup
CHUNK = 1024  # sample per block
FORMAT = pyaudio.paInt16  # sample format
CHANNELS = 1  # canal nb(mono)
RATE = 44100  # sample frequency (Hz)
THRESHOLD = 0.1  # intensity threshold, to detect notes
RECORD_DURATION=10

def process_audio(data):
    # convert data in numpy array
    audio_data = np.frombuffer(data, dtype=np.int16)

    # apply fourier formula to get a spectrum
    frequencies, intensities = signal.periodogram(audio_data, RATE)

    # get dominante frequency
    max_intensity_idx = np.argmax(intensities)
    dominant_frequency = frequencies[max_intensity_idx]

    # check if frequency is over intensity threshold 
    if intensities[max_intensity_idx] > THRESHOLD:
        return (dominant_frequency, intensities[max_intensity_idx])

    return None


def capture_audio():
    p = pyaudio.PyAudio()
    stream = p.open(
        format=FORMAT,
        channels=CHANNELS,
        rate=RATE,
        input=True,
        frames_per_buffer=CHUNK
    )

    print("Enregistrement audio en cours...")

    notes_lily = []
    start_time = time.time()

    while True:
        data = stream.read(CHUNK)
        pitch = process_audio(data)
        notes_lily.append((pitch[0], round(time.time()*1000), pitch[1]))

        # Arrêter l'enregistrement après 10 secondes
        if time.time() - start_time >= RECORD_DURATION:
            break

    stream.stop_stream()
    stream.close()
    p.terminate()

    return notes_lily


def cleanage_frequency_array(freq_arr):
    counter_freq = 0
    last_freq = (None, 0)
    cleaned_arr = []
    i = 0
    while i< len(freq_arr):
        current_freq = freq_arr[i]
        if(last_freq[0] != current_freq[0]):
            if counter_freq>5:
                cleaned_arr.append(last_freq)
            
            last_freq = current_freq 
            counter_freq = 0
        else:
            counter_freq +=1

        i+=1
    cleaned_arr.append(last_freq)

    return cleaned_arr


if( __name__ == "__main__" ):
    # captur audio and get frequency detected
    captured_notes = capture_audio()

    generate_score(cleanage_frequency_array(captured_notes))
