file = open('puzzle/02.in', 'r')
content = file.read().splitlines()

valid1 = 0
valid2 = 0

for line in content:
    password = line.split(':')[1][1:]
    letter = line.split(':')[0][-1]
    dash_index = line.index('-')
# part 1
    sup = int(line.split(':')[0][dash_index+1:-2])
    inf = int(line.split(':')[0][:dash_index])
    if inf <= password.count(letter) <= sup:
        valid1 += 1
# part 2
    if (line[sup] == letter) ^ (line[inf] == letter):
        valid2 += 1
print(valid1, valid2)
