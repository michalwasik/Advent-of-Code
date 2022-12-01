data = open('puzzle/12.in').read().splitlines()
num_data = []
for moons in data:
    coords = moons[1:-1].split(',')
    row = []
    for dim in coords:
        dim = int(dim.strip().split('=')[1])
        row.append(dim)
    num_data.append(row)

vel = []
for _ in range(4):
    vel.append([0, 0, 0])

for _ in range(1000):
    for moon_idx, moon in enumerate(num_data):
        for dim_idx, pos in enumerate(moon):
            value = 0
            another_moons = list(range(4))
            another_moons.remove(moon_idx)
            for x in another_moons:
                if pos > num_data[x][dim_idx]:
                    value -= 1
                if pos < num_data[x][dim_idx]:
                    value += 1
            vel[moon_idx][dim_idx] += value
    for x in range(4):
        for y in range(3):
            num_data[x][y] += vel[x][y]
result = 0
for z in range(4):
    moon_sum = sum([abs(ele) for ele in num_data[z]])
    vel_sum = sum([abs(ele) for ele in vel[z]])
    result += moon_sum * vel_sum

# print(result)
