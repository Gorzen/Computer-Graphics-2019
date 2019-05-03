from .LSystems import LSystem
from .Symbol import Symbol
from .Symbol import Rules
import math

def get_points():
    straight = Symbol(" straight ")
    right = Symbol(" right ")
    f = Symbol("F")
    looping = Symbol(" looping ")

    p = Symbol("+")
    m = Symbol("-")
    u = Symbol(" UP ")
    d = Symbol(" DOWN ")

    rules = Rules({right : [straight, p, straight],
                    looping : [straight, u, straight, u, straight, u, straight, u, m, m, m, m, straight, d, straight, d, straight, d, straight, d, straight, d, straight, d, straight, d, straight, d, p, p, p, p, straight, u, straight, u, straight, u, straight, u, straight],
                    f : [f, p, m, u, f]})

    lsystem = LSystem(rules, math.pi / 4, math.pi / 8, 1, (0.0, 0.0, 0.0))

    symbols = lsystem.expand([straight], 10)

    pos = lsystem.compute_symbols(symbols)

    return pos
