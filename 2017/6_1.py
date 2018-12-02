f = open('6_1.txt', 'r')
bank_states = set()
count = 0

bank_state_str = f.read()
bank_state = bank_state_str.split()
bank_state = map(int, bank_state)

# check if state has appeared yet
while bank_state_str not in bank_states:
    bank_states.add(bank_state_str)
# find max block, and its index
    max_block = max(bank_state)
    index = bank_state.index(max_block)
    print 'bank', bank_state, 'index', index, 'max_block', max_block, 'str', bank_state_str
    # distribute to all blocks
    start = index +1
    stop = start + max_block
    bank_state[index] = 0
    for i in range(start, stop):
        bank_state[i % len(bank_state)] += 1

    # create str and add last bank_state to set
    #print bank_state
    bank_state_str = str(bank_state)
    count += 1


    print count
