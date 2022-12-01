file = open('puzzle/08.in', 'r')
content = file.read().splitlines()

# part 1
accumulator_value = 0
instructions_executed = []
instruction_nr = 0
while True:
    if content[instruction_nr].split()[0] == 'acc':
        accumulator_value += int(content[instruction_nr].split()[1])
        instruction_nr += 1
    elif content[instruction_nr].split()[0] == 'jmp':
        instruction_nr += int(content[instruction_nr].split()[1])
    elif content[instruction_nr].split()[0] == 'nop':
        instruction_nr += 1
    if instruction_nr in instructions_executed:
        break
    else:
        instructions_executed.append(instruction_nr)
print(accumulator_value)


# part 2


def program(in_content, in_instruction_nr, in_accumulator_value, in_instructions_executed):
    while True:
        if in_instruction_nr == len(in_content)-1:
            if in_content[in_instruction_nr].split()[0] == 'acc':
                in_accumulator_value += int(in_content[in_instruction_nr].split()[1])
            return in_accumulator_value
        elif in_content[in_instruction_nr].split()[0] == 'acc':
            in_accumulator_value += int(in_content[in_instruction_nr].split()[1])
            in_instruction_nr += 1
        elif in_content[in_instruction_nr].split()[0] == 'jmp':
            in_instruction_nr += int(in_content[in_instruction_nr].split()[1])
        elif in_content[in_instruction_nr].split()[0] == 'nop':
            in_instruction_nr += 1
        if in_instruction_nr in in_instructions_executed:
            return 0
        else:
            in_instructions_executed.append(in_instruction_nr)


accumulator_value = 0
instruction_nr = 0
instructions_executed = []
while True:
    if content[instruction_nr].split()[0] == 'acc':
        accumulator_value += int(content[instruction_nr].split()[1])
        instructions_executed.append(instruction_nr)
        instruction_nr += 1
    elif content[instruction_nr].split()[0] == 'jmp':
        instructions_executed.append(instruction_nr)
        instruction_nr += 1
        inside_program = program(content, instruction_nr, accumulator_value, instructions_executed)
        if inside_program:
            accumulator_value = inside_program
            break
        else:
            instruction_nr -= 1
            instruction_nr += int(content[instruction_nr].split()[1])
    elif content[instruction_nr].split()[0] == 'nop':
        instructions_executed.append(instruction_nr)
        jump = int(content[instruction_nr].split()[1])
        instruction_nr += jump
        inside_program = program(content, instruction_nr, accumulator_value, instructions_executed)
        if inside_program and jump != 0:
            accumulator_value = inside_program
            break
        else:
            instruction_nr -= jump
            instruction_nr += 1
print(accumulator_value)
