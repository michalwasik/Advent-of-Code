file = open('puzzle/02.in').read().splitlines()
# part 1
depth = 0
horizontal = 0
for word in file:
    if 'down' in word:
        depth += int(word.split(' ')[1])
    elif 'up' in word:
        depth -= int(word.split(' ')[1])
    else:
        horizontal += int(word.split(' ')[1])

print(depth * horizontal)

# part 2
depth = 0
horizontal = 0
aim = 0

for word in file:
    if 'down' in word:
        aim += int(word.split(' ')[1])
    elif 'up' in word:
        aim -= int(word.split(' ')[1])
    else:
        horizontal += int(word.split(' ')[1])
        depth += aim * int(word.split(' ')[1])

print(depth * horizontal)