import os


def rename_func(path):
    path = path
    count = 1
    for file in os.listdir(path):
        temp = file.split(".")[0]

        os.rename(os.path.join(path, file), os.path.join(path, temp+"000"+ ".wav"))  # 2znvjrax_nohash_2.wav
        print(os.path.join(path, temp+"000"+ ".wav"))


def delete_func(path):
    path = path
    for file in os.listdir(path):
        temp = file.strip(".wav")
        temp = temp.split("_")
        if int(temp[2]) < 10:
            os.remove(os.path.join(path,file))
            print(file+" Deleted!")





if __name__=="__main__":
    # rename_func(r"C:\Users\Administrator\Downloads\chxb\chxb2")
    delete_func(r"C:\Users\Administrator\Downloads\chxb\chxb2")