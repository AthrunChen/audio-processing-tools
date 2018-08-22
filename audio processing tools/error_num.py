import sys
def count_word(in_file,key_word):
    num = 0
    for line in open(in_file):
        words = line.strip().split(" ")
        for word in words:
            if word == key_word:
                num += 1
            else:
                pass
    print("误唤醒次数：" + str(num))
    return num


if __name__ == '__main__':
    count_word(sys.argv[1], sys.argv[2])   # [1]log文件目录 [2]关键字

