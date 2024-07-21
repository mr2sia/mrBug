import sys

if __name__ == "__main__":
    if len(sys.argv) >2 or  len(sys.argv) <2:
        print("Введите 1 аргумент")
    else:
        with open(sys.argv[1]) as f: a = f.readlines()
        a = [int(i) for i in a]
        m = sorted(a)[len(a) // 2]
        print(sum(abs(v - m) for v in a))