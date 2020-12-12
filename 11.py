from copy import deepcopy

file = open('puzzle/11.in', 'r')
content = file.read().splitlines()
# part 1


def rotation(room):
    output = deepcopy(room)
    for row in range(1, len(room)-1):
        for seat in range(1, len(room[row])-1):
            if room[row][seat] != '.':
                adjacent = []
                for adj_seat in range(seat-1, seat +2):
                    neighbors = [room[row-1][adj_seat], room[row+1][adj_seat]]
                    adjacent += neighbors
                adjacent += [room[row][seat-1], room[row][seat+1]]

                if room[row][seat] == 'L' and adjacent.count('#') == 0:
                    output[row][seat] = '#'
                elif room[row][seat] == '#' and adjacent.count('#') >= 4:
                    output[row][seat] = 'L'
    return output


area = []
for row in range(len(content)):
    if row == 0:
        area.extend([['.'] * (len(content[row])+2), ['.'] + list(content[row]) + ['.']])
    elif row == len(content)-1:
        area.extend([['.'] + list(content[row]) + ['.'], ['.'] * (len(content[row]) + 2)])
    else:
        area.append(['.'] + list(content[row]) + ['.'])
area_c = deepcopy(area)
print(area)
before = []
while before != area:
    before = area
    area = rotation(area)
occupied = 0
for row in area:
    occupied += row.count('#')
print(occupied)

# part 2


def new_rotation(room):
    output = deepcopy(room)
    for row in range(1, len(room)-1):
        for seat in range(1, len(room[row])-1):
            if room[row][seat] != '.':
                neighbors = []
                for above_neighbour in range(seat-1, seat+2):
                    if seat-above_neighbour > 0:
                        ngh_row = row
                        ngh_seat = seat
                        ngh = ['.']
                        while ngh_seat > 0 and ngh_row > 0 and ngh == ['.']:
                            ngh_row -= 1
                            ngh_seat -= 1
                            ngh = list(room[ngh_row][ngh_seat])
                        neighbors += ngh
                    elif seat - above_neighbour < 0:
                        ngh_row = row
                        ngh_seat = seat
                        ngh = ['.']
                        while ngh_seat < len(room[row])-1 and ngh_row > 0 and ngh == ['.']:
                            ngh_row -= 1
                            ngh_seat += 1
                            ngh = list(room[ngh_row][ngh_seat])
                        neighbors += ngh
                    else:
                        ngh_row = row
                        ngh_seat = seat
                        ngh = ['.']
                        while ngh_row > 0 and ngh == ['.']:
                            ngh_row -= 1
                            ngh = list(room[ngh_row][ngh_seat])
                        neighbors += ngh
                for under_neighbour in range(seat-1, seat+2):
                    if seat-under_neighbour > 0:
                        ngh_row = row
                        ngh_seat = seat
                        ngh = ['.']
                        while ngh_seat > 0 and ngh_row < len(room)-1 and ngh == ['.']:
                            ngh_row += 1
                            ngh_seat -= 1
                            ngh = list(room[ngh_row][ngh_seat])
                        neighbors += ngh
                    elif seat - under_neighbour < 0:
                        ngh_row = row
                        ngh_seat = seat
                        ngh = ['.']
                        while ngh_seat < len(room[row])-1 and ngh_row < len(room)-1 and ngh == ['.']:
                            ngh_row += 1
                            ngh_seat += 1
                            ngh = list(room[ngh_row][ngh_seat])
                        neighbors += ngh
                    else:
                        ngh_row = row
                        ngh_seat = seat
                        ngh = ['.']
                        while ngh_row < len(room)-1 and ngh == ['.']:
                            ngh_row += 1
                            ngh = list(room[ngh_row][ngh_seat])
                        neighbors += ngh

                ngh_row = row
                ngh_seat = seat
                ngh = ['.']
                while ngh_seat > 0 and ngh == ['.']:
                    ngh_seat -= 1
                    ngh = list(room[ngh_row][ngh_seat])
                neighbors += ngh
                ngh_row = row
                ngh_seat = seat
                ngh = ['.']
                while ngh_seat < len(room[row])-1 and ngh == ['.']:
                    ngh_seat += 1
                    ngh = list(room[ngh_row][ngh_seat])
                neighbors += ngh
                if room[row][seat] == 'L' and neighbors.count('#') == 0:
                    output[row][seat] = '#'
                elif room[row][seat] == '#' and neighbors.count('#') >= 5:
                    output[row][seat] = 'L'
    return output

before = []
while before != area_c:
    before = area_c
    area_c = new_rotation(area_c)
occupied_v2 = 0
for row in area_c:
    occupied_v2 += row.count('#')
print(occupied_v2)
