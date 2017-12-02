f = open('test.txt', 'r')
sum = 0
i = 1
count = 1
stop = False

for row in f:
    list = row.split()
    list = map(int, list)
    for value in list:
        while i < len(list) & stop == False:
            current = list[i]
            if value != current:
                if current % value == 0:
                        sum += current / value
                        #stop = True
                        i = len(list)
                elif value % current == 0:
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