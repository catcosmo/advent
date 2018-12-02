f = open('test.txt', 'r')

registers ={"a": 0, "b": 0, "c": 0, "d": 0}

for row in f:
    instruction = row.split()
    target_letter = instruction[0]
    operation = instruction[1]
    value = instruction[2]
    first_comp = instruction[4]
    second_comp = instruction[6]
    comparator = instruction[5]

    switch
