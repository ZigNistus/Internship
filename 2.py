def sort():
    a = [1, 4, 6]
    b = [11, 33, 22]
    c_zip = zip(b, a)
    c = [x for _, x in sorted(c_zip)]
    print(c)

if __name__ == '__main__':
    sort()