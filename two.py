f = open('twoIn.txt', 'r')
sum = 0

for row in f:
    list = row.split()
    list = map(int, list)
    sum += max(list)-min(list)

print sum