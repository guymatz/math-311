#!/usr/bin/env python3
import math
import sys

z = int(sys.argv[1])

print("""
\\begin{equation*}
\\begin{array}{c|c|c}
\\text{element} & \\text{powers} & \\text{order}
""")
for e in range(1,z):
    powers = []
    for n in range(0,z):
        p = e**n
        element = str(p % z)
        if element not in powers:
            powers.append(element)
    print("\\\\")
    print("\\hline")
    print("%i & \{%s\} & %i" % (e, ", ".join(powers), len(powers)))
    print
print("""
\end{array}
\end{equation*}
""")
