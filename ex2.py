dct = dict()

for i in range(10, -6, -1):
    dct[i] = i**i

for i in dct.items():
    print(i)