import pyaudio
import numpy as np
import time
from scipy import signal
from music21 import converter, instrument, note, stream, environment
import os

# Configuration des paramètres
CHUNK = 1024  # Nombre d'échantillons par bloc
FORMAT = pyaudio.paInt16  # Format d'échantillonnage
CHANNELS = 1  # Nombre de canaux (mono)
RATE = 44100  # Fréquence d'échantillonnage (Hz)
THRESHOLD = 0.1  # Seuil d'intensité pour détecter les notes
NOTES = {
    261.63: "C",
    293.66: "D",
    329.63: "E",
    349.23: "F",
    392.00: "G",
    440.00: "A",
    493.88: "B"
}


def get_pitch_frequency(freq):
    closest_note = min(NOTES.keys(), key=lambda x: abs(x - freq))
    return closest_note


def process_audio(data):
    # Convertir les données en un tableau numpy
    audio_data = np.frombuffer(data, dtype=np.int16)

    # Appliquer la transformée de Fourier pour obtenir le spectre
    frequencies, intensities = signal.periodogram(audio_data, RATE)

    # Trouver la fréquence dominante
    max_intensity_idx = np.argmax(intensities)
    dominant_frequency = frequencies[max_intensity_idx]

    # Vérifier si la fréquence est supérieure au seuil d'intensité
    if intensities[max_intensity_idx] > THRESHOLD:
        pitch_frequency = get_pitch_frequency(dominant_frequency)
        return pitch_frequency

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

    notes = []
    start_time = time.time()

    while True:
        data = stream.read(CHUNK)
        pitch = process_audio(data)

        if pitch is not None:
            timestamp = time.time() - start_time
            note_name = NOTES[pitch]
            note_obj = note.Note(note_name)
            note_obj.duration = note.Duration(timestamp)
            notes.append(note_obj)

        # Arrêter l'enregistrement après 10 secondes
        if time.time() - start_time >= 10:
            break

    stream.stop_stream()
    stream.close()
    p.terminate()

    return notes


def generate_midi(notes):
    midi_stream = stream.Stream()
    midi_stream.append(instrument.Piano())

    for note_obj in notes:
        midi_stream.append(note_obj)

    midi_stream.write("midi", "output.mid")


def generate_sheet_music(notes):
    sheet_music_stream = stream.Stream()

    for note_obj in notes:
        sheet_music_stream.append(note_obj)

    sheet_music_stream.write('lily.pdf', fp='output.pdf')


# Capture de l'audio et traitement des notes
captured_notes = capture_audio()

# Génération du fichier MIDI
generate_midi(captured_notes)

# Génération de la partition au format PDF
generate_sheet_music(captured_notes)
