data = open('puzzle/04.in').read().splitlines()
date_format = '%Y-%m-%d %H:%M'
watch = []
for line in data:
    puzzle = line.split(']')
    date = puzzle[0][1:]
    command = puzzle[1][1:]
    if command[0] == 'G':
        command = int(command.split(' ')[1][1:])
    else:
        command = command[0]
    converted_date = datetime.strptime(date, date_format)
    watch.append((converted_date, command))
watch.sort(key=lambda x: x[0])
minute = timedelta(minutes=1)
guards_min = {}
guards_asleep = {}
guard = 0
asleep = 0
for item in watch:
    if isinstance(item[1], int):
        guard = item[1]
    elif item[1] == 'f':
        asleep = item[0].minute
    else:
        awake = item[0].minute
        for min in range(asleep, awake):
            if guard not in guards_min:
                guards_min[guard] = {}
            if min not in guards_min[guard]:
                guards_min[guard][min] = 1
            else:
                guards_min[guard][min] += 1
            if guard not in guards_asleep:
                guards_asleep[guard] = 1
            else:
                guards_asleep[guard] += 1

sleepyhead = max(guards_asleep, key=guards_asleep.get)
most_minutes = max(guards_min[sleepyhead], key=guards_min[sleepyhead].get)

print(sleepyhead * most_minutes)

rep_num = 0
most_rep_min = 0
most_rep_guard = 0
for key, value in guards_min.items():
    max_min = max(value, key=value.get)
    if value[max_min] > most_rep_min:
        most_rep_min = value[max_min]
        rep_num = max_min
        most_rep_guard = key

print(most_rep_guard * rep_num)
