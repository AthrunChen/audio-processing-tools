# regular wav to the same length

# 1. stretch to the same length   1.5s
# 2. find the max

import os
import librosa
import sys
from pydub import AudioSegment





def duration_regular(filename,dst_duration=1500.0):
  y, sr = librosa.load(filename,sr=16000)
  duration = librosa.get_duration(y=y,sr=sr)
  speed = (float(duration*1000))/float(dst_duration)
  y_stretch = librosa.effects.time_stretch(y, speed)
  librosa.output.write_wav(filename,y_stretch, sr=sr)
  #librosa.output.write_wav('./testxx.wav',y_stretch, sr)
  


if __name__ == '__main__':
  #duration_regular(sys.argv[1],dst_duration=1500.0)
  for filepath,pathname,filenames in os.walk('../mydata/other/'):
    for filename in filenames:
      duration_regular(os.path.join(filepath,filename),dst_duration=1500.0)
      print (filename)
