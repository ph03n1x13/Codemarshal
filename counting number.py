'''
code for finding the 'highest occurrence' of 'a number' from an unsorted array.....
 almost same as finding the highest number. we'll just update the value of occurrence
 
 [+]problem statement: https://algo.codemarshal.org/problems/556b62679c5e850300c49cb5
'''


def highest_occurrence(lst):
    num = 0
    hi_oc = 0
    for idx in range(len(lst)):  # tweaking insertion sorting

        occurrence = 1  # default occurrence is initially 1 (obviously !)
        tst_num = lst[idx]  # test number is present index

        for tst_idx in xrange(idx+1, len(lst)):
            if lst[tst_idx] != 'x' and lst[tst_idx] == tst_num:
                ''' using x flag to avoid unnecessary iterations '''
                occurrence += 1
                lst[tst_idx] = 'x'
        if occurrence > hi_oc:   # updating occurrences and most frequent value
            hi_oc = occurrence
            num = tst_num
        elif tst_num > num and hi_oc == occurrence:  # iter the hiest value if occ are equal
            hi_oc = occurrence
            num = tst_num
    print lst
    return num, hi_oc

case = input()
l = []
for test in xrange(case):
    test = map(int, raw_input().split(' '))
    output = highest_occurrence(test)
    l.append(output)
for i in xrange(len(l)):
    print 'case %d: ' % (i+1), l[i]


