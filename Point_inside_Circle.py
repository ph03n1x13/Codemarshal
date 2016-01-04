'''
Codemarshal problem Point inside Circle..... a simple solution:
the distance between the coordinates of a circle's center (cx, cy) and coordinates of
a given point (px, py)must be less than or equal to the radius. if not , the point (px, py)
 is outside the circle
'''
import math


def point_position(lst):
    cx, cy,                \
    radius,                 \
    px, py = lst[0], lst[1], \
            lst[2],           \
            lst[3], lst[4]

    distance = int(math.sqrt(math.pow((px - cx), 2) + math.pow((py - cy), 2)))
    if radius >= distance:
        return "yes"
    else:
        return "no"


loop = input("loop: ")
output = []
case = 0
for lps in xrange(loop):
    data = map(int, raw_input().split(' '))
    output.append(point_position(data))
    case += 1

for i in xrange(case):
    print "case %d : %s" %(i+1, output[i])
