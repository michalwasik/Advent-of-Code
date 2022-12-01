file = open('puzzle/10.in', 'r')
content = file.read().splitlines()
adapters = sorted(list(map(int, content)))

# part 1
charging_outlet = 0
diff_3 = 1
diff_1 = 0

for number in adapters:
    if number-charging_outlet > 3:
        break
    else:
        if number-charging_outlet == 1:
            diff_1 += 1
        elif number-charging_outlet == 3:
            diff_3 += 1
        charging_outlet += number - charging_outlet
print(diff_3*diff_1)

# part 2


def charging(n, numbers, lookup = {}):
    if n == numbers[-1] or n == numbers[-2]:
        lookup[n] = 1
    if n not in lookup:
        lookup[n] = 0
        for x in range(1, 4):
            if n+x in numbers:
                lookup[n] += charging(n+x, numbers)
    return lookup[n]


adapters.extend([max(adapters)+3, 0])
adapters.sort()
print(charging(0, adapters))
