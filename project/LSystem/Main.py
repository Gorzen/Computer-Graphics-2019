from LSystems import LSystem
from Symbol import Symbol
from Symbol import Rules
import math
import sys

f = Symbol("F")
p = Symbol("+")
m = Symbol("-")
u = Symbol(" UP ")
d = Symbol(" DOWN ")

rules = Rules({f : [f, p, u, f]})

lsystem = LSystem(rules, (0.0, 0.0, 0.0))

symbols = lsystem.expand([f], 5)

for symbol in symbols:
    sys.stdout.write(str(symbol))

sys.stdout.flush()
print('\n')

pos = lsystem.compute_symbols(symbols)

for p in pos:
    print(p)
