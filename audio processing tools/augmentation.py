import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import librosa
import matplotlib.pyplot as plt
import os
import cv2
import IPython.display as ipd
import scipy

EPS = 1e-8


def get_spectrogram(wav):
    D = librosa.stft(wav, n_fft=480, hop_length=160,
                     win_length=480, window='hamming')
    spect, phase = librosa.magphase(D)
    return spect


def time_shifting(wav):
    start_ = int(np.random.uniform(-4800, 4800))
    print('time shift: ', start_)
    if start_ >= 0:
        wav_time_shift = np.r_[wav[start_:], np.random.uniform(-0.001, 0.001, start_)]
    else:
        wav_time_shift = np.r_[np.random.uniform(-0.001, 0.001, -start_), wav[:start_]]
    return wav_time_shift


def speed_tuning(wav):
    speed_rate = np.random.uniform(0.7, 1.3)
    wav_speed_tune = cv2.resize(wav, (1, int(len(wav) * speed_rate))).squeeze()
    print('speed rate: %.3f' % speed_rate, '(lower is faster)')
    print('wav length: ', wav_speed_tune.shape[0])
    return wav_speed_tune


def volume_tuning(wav):
    wav_with_bg = wav * np.random.uniform(0.8, 1.2)
    return wav_with_bg


def main(file_path):
    file_path = file_path
    wav, sr = librosa.load(file_path, sr=None, dtype=np.float32)
    wav = time_shifting(wav)
    wav = speed_tuning(wav)
    wav = volume_tuning(wav)
    return wav,sr


if __name__ == '__main__':
    data_path = os.listdir(r"C:\Users\Administrator\Downloads\chxb\chxb2")
    for i in data_path:
        temp0 = i
        temp = temp0.split(".wav")[0]
        temp = temp.split("_")

        for j in range(1, 10):
            #print("i="+i)
            wav, sr = main(file_path=r"C:\Users\Administrator\Downloads\chxb\chxb2"+"\\"+i)
            wav = np.int16(wav*32768)
            print(wav)
            scipy.io.wavfile.write(r"C:\Users\Administrator\Downloads\chxb\chxb_augmentation"+"\\"+ temp[0]+"_"+temp[1]+"_"+str(int(temp[2])+9+j)+".wav", sr, wav)
            # print(r"C:\Users\Administrator\Downloads\chxb\chxb_augmentation"+"\\"+ temp[0]+"_"+temp[1]+"_"+str(int(temp[2])+9+j)+".wav", sr, wav)

    # print(wav.shape, wav.max(), wav.min())




