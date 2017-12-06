f = open('test.txt', 'r')
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
    print 'bank', bank_state, 'index', index
    # distribute to all blocks
    for i in range(0,len(bank_state)):
        distribute_even = max_block%len(bank_state)
        if distribute_even is 0 and i is index:
            bank_state[i]= 0
            bank_state[i] += max_block / (len(bank_state))
        elif distribute_even is 0:
            bank_state[i] += max_block / (len(bank_state))
        else:
            distribute_uneven = max_block / (len(bank_state) - 1)
            if i is index:
                bank_state[i] = 0
                bank_state[i] += max_block % distribute_uneven
            else:
                bank_state[i] += distribute_uneven

    # create str and add last bank_state to set
    print bank_state
    bank_state_str = str(bank_state)
    count += 1

    print count
