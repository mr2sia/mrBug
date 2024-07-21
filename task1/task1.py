import sys

if __name__ == "__main__":
    if len(sys.argv) >3 or  len(sys.argv) <3:
        print("Введите 2 аргумента")
    else:
        n = int(sys.argv[1])
        m = int(sys.argv[2])
        i = 1
        while True:
            print(i, end='')
            i = 1 + (i + m - 2) % n
            if i == 1:
                break
        print()