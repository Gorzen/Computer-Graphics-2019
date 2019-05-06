from .LSystems import LSystem
from .Symbol import Symbol
from .Symbol import Rules
import math

def get_points():
    #loop = [track, p, track, track, track, p, track, track, track, p, track, track, track, p, track, track, track, p, track, track, track, p, track, track, track, p, track, track, track, p, track, track]

    straight = Symbol(" straight ")
    right = Symbol(" right ")
    f = Symbol("F")
    track = Symbol(" track ")
    looping = Symbol(" looping ")

    t_s = Symbol(" track stochastic ", True)

    p = Symbol("+")
    m = Symbol("-")
    u = Symbol(" UP ")
    d = Symbol(" DOWN ")

    rules = Rules({right : [straight, p, straight],
                    looping : [straight, u, straight, u, straight, u, straight, u, m, m, m, m, straight, d, straight, d, straight, d, straight, d, straight, d, straight, d, straight, d, straight, d, p, p, p, p, straight, u, straight, u, straight, u, straight, u, straight],
                    f : [f, p, m, u, f],
                    track : [track, track, u, track, track, d, track, track, d, track, track, u],
                    t_s :   [[0.5, [t_s, straight, p, straight, t_s]],
                            [0.5, [t_s, straight, m, straight, t_s]]]})

    lsystem = LSystem(rules, math.pi / 4, math.pi / 8, 1, (0.0, 0.0, 0.0))

    symbols = lsystem.expand([t_s], 5)

    pos = lsystem.compute_symbols(symbols)

    return pos
