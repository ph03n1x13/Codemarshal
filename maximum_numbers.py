'''
1. finding the nth highest and lowest number from an unsorted list/array
only using variables and changing the order of array .........
2. using the same technique we can find the second highest number also
[+]problem statement:https://algo.codemarshal.org/problems/556b5a1e9c5e850300c49cac
'''

import random
import time


def highest_value(lst):
    '''assume the first index is the highest [we won't sort or change values of indexes]'''
    highest = lst[0]
    start = time.time()
    for index in xrange(1, len(lst)):  # tweaking the insertion sort
        if lst[index] > highest:
            highest = lst[index]
    end = time.time()
    print 'total time %d sec' %(end -start)
    return highest

'''
if the first value highest then the
second value will be the second highest. Assuming this, we only update
the highest and second highest values. note: this is a buggy approach if
[h , a, b, c... s_h] this algo fails to calculate...
'''


def second_highest(lst):
    '''
    buggy approach
    '''
    hi = lst[0]
    sec_hi = lst[1]
    for idx in xrange(1, len(lst)):
        if lst[idx] > hi:  # we're missing another condition here
            sec_hi = hi
            hi = lst[idx]
    return sec_hi

"""
so here is the right approach
           h    s_h
           100  -5  20  30  40
            |
            |__________if the first value is highest then the
                       second value will be the second highest
                           h        s_h
                           100  -5  20  30  40
                           h            s_h
                           100   -5 20  30   40
                           h                 s_h
                           100   -5 20  30   40
                                |
                                |____elseif present value > second highest
                                     present value will be the second highest
                                     keep updating the second highest value

"""


def second_highest_value(lst):
    '''
    code for finding 1st and 2nd highest values
    without sorting an array tweaking insertion sort
    '''
    h = lst[0]
    s_h = lst[1]
    for idx in xrange(1, len(lst)):  # tweaking insertion sort
        if lst[idx] > h:
            s_h = h      # nb: intellisense says name 's_h' from outer scope
                         # shadowing name defined outer scope
            h = lst[idx]
        elif lst[idx] > s_h:
            s_h = lst[idx]  # focusing on the second highest value and updating it
                            # as the highest value is not changed in these iterations
    return h, s_h  # returning a tuple of hi and sec_hi value

'''
Codes for nth lowest will be the reverse of the same method...............

'''

tst = random.sample(xrange(-100, 100), 5)
print 'unsorted list %s' %tst
(h, s_h) = second_highest_value(tst)
print 'highest : %d 2nd highest : %d'  % (h, s_h)
