import os


def Folders(path, depth = 0):
    for i in os.listdir(path):
        if os.path.isdir(path + "//" + i) and i[0] != '.' and i[0] != '$':
            print('-'*depth, i)
            if not os.path.isdir(path+i):    # len(os.listdir(path + i)) == 0
                print('-'*depth, i)
            else:
                Folders(path + "//" + i + '//', depth + 1)


Folders("C://skola//")
