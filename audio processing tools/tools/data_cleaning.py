import scipy
import sys
import os
import librosa
import numpy as np
import shutil
import matplotlib.pyplot as plt
import shutil
from pydub import AudioSegment


def reforming(filename, outfile):
    files = os.listdir(filename)
    gate = 200
    cash = []
    for file in files:
        print(file)
        wav,sr = librosa.load(filename+"\\"+file)
        wav = np.int16(wav * 32768)
        temp1 = np.fabs(wav)
        lenth = temp1.shape[0]
        energy = np.sum(temp1)
        power = energy/lenth
        cash.append(power)
        if power < gate:
            pass
        else:
            amp = 1393/power
            wav = np.int16(amp*wav)
            scipy.io.wavfile.write(outfile+"\\"+file, sr, wav)
            # shutil.copyfile(filename+"\\"+file, outfile+"\\"+file)


def cleaning(filename):
    files = os.listdir(filename)
    gate = 300
    clip_lenth = []
    num = 0
    for file in files:
        print(file)
        wav,sr = librosa.load(filename+"\\"+file)
        wav = np.int16(wav * 32768)
        temp1 = np.fabs(wav)
        lenth = temp1.shape[0]
        energy = np.sum(temp1)
        power = energy/lenth
        if power < gate:
            num=num+1
            os.remove(filename+"\\"+file)
            # shutil.copy(os.path.join(filename, file), r"C:\Users\Administrator\Downloads\chxb\chxb_lowpower")
    print("num = "+str(num))

        # if simple_lenth < 1.6 and simple_lenth > 1.2:
        #     shutil.copy(os.path.join(filename, file),r"C:\Users\Administrator\Downloads\chxb\chxb_temp2")

    # print(clip_lenth)
    # x = np.array(clip_lenth)
    # plt.figure()
    # plt.plot(x)
    # plt.show()


def audio_lenth_get(filename):
    files = os.listdir(filename)
    lenth_list = []
    for file in files:
        sound1 = AudioSegment.from_file(os.path.join(filename, file), format="wav")
        duration_in_milliseconds = len(sound1)
        lenth_list.append(duration_in_milliseconds)
        print(file)
        if 900 < duration_in_milliseconds < 1500:
            shutil.copy(os.path.join(filename, file), r"C:\Users\Administrator\Downloads\chxb\chxb_temp2")





if __name__ == '__main__':
    # reforming(filename=r"C:\Users\Administrator\Downloads\chxb\chxb", outfile=r"C:\Users\Administrator\Downloads\chxb\chxb2")
    cleaning(r"C:\Users\Administrator\Downloads\chxb\chxb_temp2")
    # audio_lenth_get(r"C:\Users\Administrator\Downloads\chxb\chxb")