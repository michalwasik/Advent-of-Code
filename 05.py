file = open('puzzle/05.in', 'r')
airplane = file.read().splitlines()

# part 1
seats = []
for seat in airplane:
    row = [0, 127]
    column = [0, 7]
    for letter in seat:
        if letter in ['F', 'B']:
            next_row_len = (row[1]-row[0]+1)/2
            if letter == 'F':
                row[1] -= next_row_len
            else:
                row[0] += next_row_len

        else:
            next_column_len = (column[1]-column[0]+1)/2
            if letter == 'L':
                column[1] -= next_column_len
            else:
                column[0] += next_column_len
    row_nr = int(row[0])
    column_nr = int(column[0])
    seats.append((row_nr, column_nr))
ids = [seat[0]*8 + seat[1] for seat in seats]
print(max(ids))

# part 2
neighbors = []
for num in range(1, 128):
    seats_taken = []
    for seat in seats:
        if seat[0] == num:
            seats_taken.append(seat)
    if len(seats_taken) == 7:
        neighbors = seats_taken
my_column = 0
my_row = neighbors[0][0]
for num in range(0, 8):
    if (my_row, num) not in neighbors:
        my_column = num
print(my_row*8+my_column)
