import math
import sys

with open(sys.argv[2], 'r') as f: lines2 = f.readlines()
with open(sys.argv[1], 'r') as f: lines1 = f.readlines()

if len(lines2) > 100:
    print('Точек в файле с их координатами больше 100')
else:
    xk = float(lines1[0].split(' ')[0])
    yk = float(lines1[0].split(' ')[1])
    r = float(lines1[1])

    for i in lines2:
        x = float(i.split(' ')[0])
        y = float(i.split(' ')[1])
        if (x-xk)**2/r**2 + (y-yk)**2/r**2 <= 1:
            if (x-xk)**2 + (y-yk)**2 == r**2:
                print("0")
            else:
                print("1")
        else:
            print("2")