# split a wav file into two wav file
# wtt
from pydub import AudioSegment
import os
import numpy as np 
import sys

def split_wav(path,filename,dst_dir):
  song =AudioSegment.from_wav(os.path.join(path,filename))



  middle = int(len(song)/2)
  split_point = []
  beta = 0.1
  val = 100
  for i, t in enumerate(song):
    val = beta*t + (1-beta)*val




  song1 = song[:middle]
  song2 = song[-middle:]
  filename1 = filename.split('.wav')[0] +'1' +'.wav'
  filename2 = filename.split('.wav')[0] +'2' +'.wav'
  song1.export(os.path.join(dst_dir,filename1),format='wav')
  song2.export(os.path.join(dst_dir,filename2),format='wav')
  print(filename2)



  
   

if __name__=="__main__":
  # if len(sys.argv) != 3:
  #   print("usage: python split_wav.py base_dir  dst_dir ")
  #   sys.exit()
  # else:
  #   base_dir = sys.argv[1]
  #   dst_dir = sys.argv[2]
  #   for path,pathname,filenames in os.walk(base_dir):
  #     for filename in filenames:
  #       split_wav(path,filename,dst_dir)

  split_wav(r"C:\Users\Administrator\Downloads\chxb\datacleaning","0lgqh1rv_nohash_0.wav",r"C:\Users\Administrator\Downloads\chxb\datacleaning_output")


