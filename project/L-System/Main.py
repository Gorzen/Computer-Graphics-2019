from LSystems import LSystem
from Symbol import Symbol
from Symbol import Rules
import math
import sys

f = Symbol("F")
p = Symbol("+")
m = Symbol("-")

rules = Rules({f : [f, f, p, f, m, m]})

lsystem = LSystem(rules, math.pi / 2, 1, (0.0, 0.0))

symbols = lsystem.expand([f], 3)

for symbol in symbols:
    sys.stdout.write(str(symbol))

sys.stdout.flush()
print('\n')

pos = lsystem.compute_symbols(symbols)

for p in pos:
    print(p)
