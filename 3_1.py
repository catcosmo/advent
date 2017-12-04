rank = 0
quadEdge = 1
quadSize = 1
quadStart = 1
total = 1
input = 289326 #result 34


# 1. calculate distance from center to spiral ring
while total < input:
    #calculate size of next spiral ring
    quadSize = ((quadEdge+2)+quadEdge)*2
    #define new quadedge length
    quadEdge = quadEdge + 2
    #calculate starting nunber for current quad
    quadStart = total+1
    #calculate total number of numbers in spiral so far
    total += quadSize
    #increment rank
    rank += 1

# 2. calculate  distance from middle of quadEdge to input
# write the spiral quad in which the input lies in a list
quad = range(quadStart,quadStart+quadSize)
# find out what position in the list the input has
indexInput = quad.index(input)
# find four middle points
jump = quadEdge-1
mid1 = quadStart + jump/2-1
mid2 = mid1 + jump
mid3 = mid2 + jump
mid4 = mid3 + jump
midPoints = [mid1, mid2, mid3, mid4]
print midPoints
# find middle point nearest value & calculate distance
distance = input
for point in midPoints:
    newDistance = input - point
    if newDistance > 0 & newDistance < distance:
        distance = newDistance

# 3. add rank and distance
manhattenDistance = rank + distance
print manhattenDistance