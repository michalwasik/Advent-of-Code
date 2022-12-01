file = open('puzzle/07.in', 'r')
content = file.read().splitlines()

# part 1
matryoshka = {'shiny gold'}
bf_length = 0
while bf_length != len(matryoshka):
    bf_length = len(matryoshka)
    for expression in content:
        contained_colors = set()
        for sentence in expression.split('contain')[1].split(','):
            contained_colors.add(sentence[3:sentence.index('bag') - 1])
        if set.intersection(matryoshka, contained_colors) != set():
            matryoshka.add(expression.split('contain')[0][:-6])
matryoshka.remove('shiny gold')
print(len(matryoshka))

# part 2
parents = {}
for expression in content:
    if expression.split('bags')[0][:-1] not in matryoshka:
        if expression.split('contain ')[1] == 'no other bags.':
            parents[expression.split('bags')[0][:-1]] = 0
        else:
            inside = expression.split('contain')[1].split(',')
            value = []
            for bag in inside:
                value.extend([bag[1], bag[3:bag.index('bag')-1]])
            parents[expression.split('bags')[0][:-1]] = value
int_parents = {}
for bag in parents:
    if isinstance(parents[bag], int):
        int_parents[bag] = parents[bag]

while int_parents != parents:
    for color in parents:
        if color not in int_parents:
            for bag in range(1, len(parents[color]), 2):
                if parents[color][bag] not in int_parents:
                    break
            else:
                value = 0
                for bag in range(0, len(parents[color]), 2):
                    value += int(parents[color][bag])*(1 + parents[parents[color][bag+1]])
                parents[color] = int_parents[color] = value
print(parents['shiny gold'])
