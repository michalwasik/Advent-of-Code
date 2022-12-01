data = open('puzzle/12.in').read().splitlines()
initial_state = data[0][15:]
puzzle = data[2:]
healthy = []
sick = []
for pattern in puzzle:
    if pattern[-1] == '.':
        sick.append(pattern)
    else:
        healthy.append(pattern)
grown_pattern = []
death_pattern = []

for pattern in sick:
    death_pattern.append(pattern[:5])
for pattern in healthy:
    grown_pattern.append(pattern[:5])

ctr_idx = 0
for _ in range(2000):
    plantation = ''
    if '....' + initial_state[:1] in grown_pattern:
        print('..' + initial_state[:3])
        ctr_idx -= 2
        initial_state = '....' + initial_state
    elif '...' + initial_state[:2] in grown_pattern:
        ctr_idx -= 1
        initial_state = '...' + initial_state
    else:
        initial_state = '..' + initial_state
    if initial_state[-5:] != '.....':
        initial_state += '.....'
    for idx in range(len(initial_state) - 4):
        part = initial_state[idx:idx+5]
        if part in grown_pattern:
            plantation += '#'
        else:
            plantation += '.'
    initial_state = plantation
result = 0
last_season = list(initial_state)
for pot_nr, pot in enumerate(last_season, start=ctr_idx):
    if pot == '#':
        result += pot_nr
print(ctr_idx)
print(result)1