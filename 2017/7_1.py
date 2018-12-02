f = open('test.txt', 'r')
all_programs = set()
all_children = set()

for row in f:
    # get program name
    program = row.split('->')[0].split()[0]
    all_programs.add(program)
    # get children of program
    if '->' in row:
        children = row.split('->')[1].split()
        for child in children:
            child = child.strip(',')
            all_children.add(child)

all_programs_list = list(all_programs)
for program in all_programs:
    if program in all_children:
        all_programs_list.pop(all_programs_list.index(program))

print all_programs_list