import os
import shutil



def delete_plus_plus(filename,dst):
    file = os.listdir(filename)
    print(file)
    cash  = []
    for i ,j in enumerate(file):
        temp = j.split(".")
        if temp[1] == "textgrid":
            with open(os.path.join(filename, j), encoding='gb18030',errors='ignore') as f:
                for line in f:
                    print("line="+line)
                    if "++"  in line:
                         shutil.copy(os.path.join(filename, j), dst)
                         shutil.copy(os.path.join(filename, temp[0] + ".wav"), dst)
                         cash.append(j)
    return cash


def delete_plus_plus_pingxiong(filename,dst):
    file = os.listdir(filename)
    print(file)
    cash  = []
    for i ,j in enumerate(file):
        temp = j.split(".")
        if temp[1] == "textgrid":
            with open(os.path.join(filename, j), encoding='gb18030',errors='ignore') as f:
                for line in f:
                    print("line="+line)
                    if "r"""  in line:
                         shutil.copy(os.path.join(filename, j), dst)
                         shutil.copy(os.path.join(filename, temp[0] + ".wav"), dst)
                         cash.append(j)
    return cash











if __name__=="__main__":
    filename  = r"C:\Users\Administrator\Desktop\89_segwave"
    dst = r"C:\Users\Administrator\Desktop\temp"
    cash = delete_plus_plus(filename,dst=dst)
    for i in cash:
        temp = i.split(".")
        os.unlink(os.path.join(filename,i))
        os.unlink(os.path.join(filename, temp[0] + ".wav"))

