file = open('puzzle/03.in', 'r')
content = file.read().splitlines()

anws = 1
movement = [(1, 3), (1, 5), (1, 7), (1, 1), (2, 1)]

for down, right in movement:
    coords = [0, 0]
    trees = 0
    for _ in content:
        if coords[0] < len(content)-down:
            if coords[1] < len(content[0])-right:
                coords[0] += down
                coords[1] += right

            else:
                coords[0] += down
                coords[1] = coords[1] - len(content[0]) + right
            if content[coords[0]][coords[1]] == '#':
                    trees += 1
# part 1
    if(down, right) == (1, 3):
        print(trees)

    anws *= trees
# part 2
print(anws)
