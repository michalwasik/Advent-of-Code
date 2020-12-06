file = open('puzzle/01.in', 'r')
numbers = file.read().splitlines()

# part 1
rest = list([2020 - int(number) for number in numbers])
for number in numbers:
    if int(number) in rest:
        print(int(number)*(2020-int(number)))
        break

# part 2
numbers_part2 = set()
for num1 in numbers:
    rest_2 = list(num2 - int(num1) for num2 in rest)
    for num2 in numbers:
        if int(num2) in rest_2:
            numbers_part2.add(int(num2))
anwser = 1
for fnumber in numbers_part2:
    anwser *= fnumber
print(anwser)
