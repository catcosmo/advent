f = open('5_1.txt', 'r')
jump_instructions = []
current = 0
jumps_count = 0

for row in f:
    jump_instructions.append(row)

jump_instructions = map(int, jump_instructions)

while (current >= 0 & current < len(jump_instructions)):
    jump_instructions[current] += 1
    current = current + jump_instructions[current] - 1
    jumps_count +=1

print jumps_count