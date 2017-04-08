#!/usr/bin/env python3
import math
import sys

z = int(sys.argv[1])

for e in range(1,z):
    powers = []
    for n in range(0,z):
        p = e**n
        element = str(p % z)
        if element not in powers:
            powers.append(element)
    print("%i | {%s} | %i" % (e, ", ".join(powers), len(powers)))
