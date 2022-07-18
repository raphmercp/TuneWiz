from chunk import Chunk
import sys

import pyaudio
import struct
import numpy as np
import matplotlib.pyplot as plt

FORMAT = pyaudio.paInt16
CHUNK = 1024 * 4
CHANNELS = 1
RATE = 44100

def get_file_name_from_args() -> str:
    """Return the file name based on the user-provided architecture."""
    try:
        arch_name = sys.argv[1]
        file_name = f"Contents-{arch_name}.gz"
        return file_name
    except IndexError:
        print("You must provide a file name as an argument. Exiting.")
        sys.exit(1)

def main():
    audio_file = get_file_name_from_args()

    p = pyaudio.PyAudio()

    stream = p.open(
        format=FORMAT,
        channels=CHANNELS,
        rate=RATE,
        input=True,
        output=True,
        frames_per_buffer=Chunk
    )

    data = stream.read(CHUNK)
    data


if __name__ == "__main__":
    main()