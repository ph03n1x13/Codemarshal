import time
"""
Codemarshal problem upper lower
time : 0.0 sec
mem : 2 KB
"""


def lower_upper_ascii(st):
    """converting case using ASCII values"""
    result = ''
    for letters in xrange(len(st)):
        if ord(st[letters]) >= 97 and  ord(st[letters]) <= 122:
            result += chr(ord(st[letters])-32)  # changing lower ASCII orders into capitals
        else:
            result += st[letters]
    return result


def up_low_swap_ascii(stng):  # using ASCII values
    result = ''
    start = time.time()
    for letters in xrange(len(stng)):
        if ord(stng[letters]) >= 97 and  ord(stng[letters]) <= 122:
            result += chr(ord(stng[letters])-32)
        elif ord(stng[letters]) >= 65 and  ord(stng[letters]) <= 90:
            result += chr(ord(stng[letters])+32)
        else:
            result += stng[letters]
    end = time.time()
    print 'execution time : %d sec' % (end-start)
    return result


def lower_upper(st):  # using standard library
    """converting case using ASCII values"""
    result = ''
    for letters in xrange(len(st)):
        result += st[letters].upper()
    return result


def low_up(st):  # using standard library
    return st.upper()


def up_low(st):    # using standard library
    return st.lower()


tst = raw_input(">>> ")
out = up_low(tst)
print out





