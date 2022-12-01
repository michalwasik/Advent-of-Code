from utils import *             # ints str z liczbami, words str z literami

file = open('puzzle/01.in').read().split('\n')
most = 0
curr = 0
suma = []

for item in file:
    if item == '':
        suma.append(curr)
        if curr > most:
            most = curr
        curr = 0
    else:
        curr += int(item)
print(most)
suma.sort()
result = sum(suma[-3:])
print(result)
