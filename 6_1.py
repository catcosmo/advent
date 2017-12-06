f = open('test.txt', 'r')
bank_states = set()
count = 0

bank_state_str = f.read()
bank_state = bank_state_str.split()
bank_state = map(int, bank_state)

# check if state has appeared yet
while bank_state_str not in bank_states:
    # find max block, and its index
    max_block = max(bank_state)
    index = bank_state.index(max_block)
    # iterate over list and increment blocks by one until max_block is distributed
    for i in range(index,index+max_block+1):
        bank_state[i%len(bank_state)-1] += 1

    # create str and add last bank_state to set
    bank_state_str = str(bank_state)
    bank_states.add(bank_state_str)
    count += 1

    print bank_state_str
