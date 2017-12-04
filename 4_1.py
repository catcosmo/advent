f = open('4_1.txt', 'r')
seen = set()
invalid = False
invalidCount = 0
count = 0

for row in f:
    list = row.split()
    for item in list:
        if item not in seen:
            seen.add(item)
        else:
            invalid = True
    if invalid:
        invalid = False
    else:
        count += 1
    seen.clear()

print count



