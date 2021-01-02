#  Copyright (c) 2020 by Frank Huang. You may edit this code and distribute the software freely.

from dotenv import load_dotenv
import librosa
import librosa.display
import numpy as np
import matplotlib.pyplot as plt
from utils.logging import write
import os

"""
Init and global config variables
"""
load_dotenv()

MEL_DB_DISTANCE_THRESHOLD = int(os.getenv('MEL_DB_DISTANCE_THRESHOLD'))
n_fft = int(os.getenv('N_FFT'))
n_mels = int(os.getenv('N_MELS'))
hop_length = int(os.getenv('HOP_LENGTH'))




def loadTarget():
    y, sr = librosa.load('../res/rickroll.mp3') # we are gonna be called from temp/ dir
    song, _ = librosa.effects.trim(y)
    return song, sr

def _load(path):
    y, sr = librosa.load(path)
    song, _ = librosa.effects.trim(y)
    return song, sr

def isRickRoll(path):
    orig, osr = loadTarget()
    write('meldetect', 'Loaded original', True)
    song, sr = _load(path)
    write('meldetect', 'Loaded candidate', True)

    # Generate power mel spectrogram for each song, then convert to db using librosa, with ref=np.max (Code for obtaining spectrogram
    # from https://towardsdatascience.com/getting-to-know-the-mel-spectrogram-31bca3e2d9d0)
    So = librosa.feature.melspectrogram(orig, sr=osr, n_fft=n_fft, n_mels=n_mels, hop_length=hop_length)
    Sc = librosa.feature.melspectrogram(song, sr=sr, n_fft=n_fft, n_mels=n_mels, hop_length=hop_length)

    So_DB = librosa.power_to_db(So, ref=np.max)
    Sc_DB = librosa.power_to_db(Sc, ref=np.max)
    SC_DB_o = Sc_DB
    ## DEBUG



    # Now flatten the arrays...
    So_DB = So_DB.flatten()
    Sc_DB = Sc_DB.flatten()

    # Pad each with zeroes as necessary, but keep track of which array is which... (necessary for np.linalg.norm(orig - candidate))
    if So_DB.shape != Sc_DB.shape:
        if Sc_DB.shape < So_DB.shape:
            So_DB = np.resize(So_DB, Sc_DB.shape)
        else:
            Sc_DB = np.resize(Sc_DB, So_DB.shape)
    else:
        pass
    # if np.linalg.norm(So_DB - Sc_DB) <= MEL_DB_DISTANCE_THRESHOLD:
    #     print(f"${np.linalg.norm(So_DB - Sc_DB)} <= ${MEL_DB_DISTANCE_THRESHOLD}")
    # else:
    #     print(f"${np.linalg.norm(So_DB - Sc_DB)} > ${MEL_DB_DISTANCE_THRESHOLD}")
    return np.linalg.norm(So_DB - Sc_DB) <= MEL_DB_DISTANCE_THRESHOLD  # Song is similar enough to Rick Astley's

