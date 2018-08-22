import numpy as np
import scipy
import librosa
import os

def reforming_func(filename):
    wav,sr= librosa.load(filename)
    print(type(wav))
    wav = np.int16(wav*32768)
    temp = np.fabs(wav)
    gate = np.sum(temp)/(temp.shape[0])
    print("gate=" + str(gate))
    for j, i in enumerate(temp):
        if i > gate:
            wav[j] = wav[j]*0.4
        print("j="+str(j))
        print("i="+str(i))
    out_temp = filename.split(".")
    out_temp[0] = out_temp[0]+"reformed.wav"
    scipy.io.wavfile.write(out_temp[0], sr, wav)



if __name__=="__main__":
    reforming_func(r"E:\CYFsTool_Workspace\data\noise_100_plus_01.wav")

