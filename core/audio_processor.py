import sounddevice as sd
import numpy as np

def get_audio_level(duration=0.1):
    recording = sd.rec(int(duration * 44100), samplerate=44100, channels=1, dtype='float64')
    sd.wait()
    volume_norm = np.linalg.norm(recording) * 10
    return min(int(volume_norm), 100)  # Limit between 0 and 100
