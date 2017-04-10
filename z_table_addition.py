#!/usr/bin/env python3
import math
import sys

z = int(sys.argv[1])

print("""
\\begin{equation*}
\\begin{array}{c|%s}
""" % ("c" * z))
print("+ & %s \\\\" % (" & ".join(map(str, range(z)))))
print("\\hline")
for row in range(z):
    elements = []
    for col in range(z):
        elem = (row + col) % z
        element = str(elem)
        elements.append(element)
    print("%i & %s \\\\" % (row, " & ".join(elements)))
print("""
\end{array}
\end{equation*}
""")
