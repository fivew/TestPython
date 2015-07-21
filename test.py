

import sys

import sets


def test(x):
    return x * x

a = [1, 2, 3, 4, 5]

A = map(test, a)

print A

setA = sets.Set(A)
seta = sets.Set(a)

print setA & seta
print setA | seta
print setA - seta
print setA ^ seta

print ord(u"\u2020")
print repr(unichr(2236))
print map(ord, 'fgsd')
print map(chr, [55, 121, 64, 88])
print ''.join(map(chr, range(30, 155)))

print isinstance(seta, sets.BaseSet)
print isinstance("object", basestring)

print '*', "test".ljust(10), '*'
print '*', "test".rjust(10), "*"
print "*", "test".center(10), "*"
print "test".ljust(9, "*"), "test2".rjust(9, "-"), "testt3".center(9, '+')

print "test".strip('t')
print "test".lstrip('t')
print "test".rstrip('t')
print "test".strip("ts")

