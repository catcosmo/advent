f = open('test.txt', 'r')
str = f.read()

#for testing
#str = "12341234"

first = str[0]
sum = 0
next = ""
ln = len(str)

for i in range (0, ln):
    current = str[0]
    next = str[ln/2]
    if current == next:
        sum += int(current)
        print i+1, current, next, sum, str
    str = str[1:]
    str += current

print "length", ln
print 'sum', sum
#print str
