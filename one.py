f = open('oneIn.txt', 'r')
str = f.read()

first = str[0]
sum = 0
next = ""

while len(str) > 2:
    current = str[0]
    next = str[1]
    if current == next:
        sum += int(current)
    str = str[1:]
    print next

if next == first:
    sum += int(first)

print sum