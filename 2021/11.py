from typing import Generator

content = open('puzzle/11.in').read().splitlines()
data = []
for line in content:
    new_line = []
    for char in line:
        new_line.append(int(char))
    data.append(new_line)
lights_up = 0
DELTAS = [
    (-1, -1), (-1, 0), (-1, 1),
    (0, -1),           (0, 1),
    (1, -1),  (1, 0),  (1, 1),
]
Cord = tuple[int, int]


def lights_neig(light: Cord) -> Generator[Cord, None, None]:
    for y_delta, x_delta in DELTAS:
        if 0 <= (new_y := light[0] + y_delta) < 10 and 0 <= (new_x := light[1] + x_delta) < 10:
            yield new_y, new_x


#   import numpy
# octopuses = numpy.array(octopuses) + 1

def lightsup(octopuses, lightened, light_num: int, first=True, repeat=False):
    if first:
        lightened = set()
        octopuses = [[x + 1 for x in y] for y in octopuses]
    for row_id, row in enumerate(octopuses):
        for oct_id, oct in enumerate(row):
            if oct >= 10 and (row_id, oct_id) not in lightened:
                repeat = True
                lightened.add((row_id, oct_id))
                for coord in lights_neig((row_id, oct_id)):
                    octopuses[coord[0]][coord[1]] += 1
    if repeat:
        return lightsup(octopuses, lightened, first=False, repeat=False, light_num=light_num)
    else:

        for row_id, row in enumerate(octopuses):
            for oct_id, oct in enumerate(row):
                if oct > 9:
                    light_num += 1
                    octopuses[row_id][oct_id] = 0
        return octopuses, light_num


step = 0
while True:
    light_num_b4 = lights_up
    data, lights_up = lightsup(data, set(), light_num=lights_up, first=True, repeat=False)
    step += 1
    if step == 100:
        print(lights_up)
    if lights_up - light_num_b4 == 100:
        print(step)
        break
