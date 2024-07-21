import sys

if __name__ == "__main__":
    if len(sys.argv) >2 or  len(sys.argv) <2:
        print("Введите 1 аргумент")
    else:
        a = [1, 10, 2, 9]
        m = sorted(a)[len(a) // 2]
        print(sum(abs(v - m) for v in a))