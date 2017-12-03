f = open('twoIn.txt', 'r')
sum = 0
i = 1
count = 1
stop = False

for row in f:
    list = row.split()
    list = map(int, list)
    list.sort(reverse=True)
    print list
    for value in list:
        while i < len(list):
            current = list[i]
            if value != current:
                if value % current == 0:
                        sum += value / current
                        i = len(list)
                        #stop = True
                else:
                    i += 1
            else:
                i += 1
            if i == len(list):
                i = count
                break

count += 1
print 'sum', sum