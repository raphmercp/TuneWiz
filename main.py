import sys
import os

import numpy as np
import matplotlib.pyplot as plt
import wave


import librosa as lr

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

    waveobj = wave.open("JohnMackechnie.wav")

    audio, sfreq = lr.load("JohnMackechnie.wav")

    time = np.arange(0, len(audio)) / sfreq

    # fig, ax = plt.subplots()
    # ax.plot(time, audio)
    # ax.set(xlabel='time (s)', ylabel='Sound Amplitude')
    # plt.show()

    file_path = './JohnMackechnie.wav'
    x, sr = lr.load(file_path)
    onset_frames = lr.onset.onset_detect(x, sr=sr)
    print(len(onset_frames))
    onset_times = lr.frames_to_time(onset_frames)
    # remove extension, .mp3, .wav etc.
    file_name_no_extension, _ = os.path.splitext(file_path)
    output_name = file_name_no_extension + '.beatmap.txt'
    with open(output_name, 'wt') as f:
        f.write('\n'.join(['%.4f' % onset_time for onset_time in onset_times]))




if __name__ == "__main__":
    main()