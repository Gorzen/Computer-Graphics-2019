from .LSystems import LSystem
from .Symbol import Symbol
from .Symbol import Rules
import math

def get_points():
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
    smooth_p = Symbol(" +++ ")
    smooth_m = Symbol(" --- ")

    loop = [track, p, track, track, track, p, track, track, track, p, track, track, track, p, track, track, track, p, track, track, track, p, track, track, track, p, track, track, track, p, track, track]

    loop_s = [t_s, smooth_p, t_s, t_s, t_s, smooth_p, t_s, t_s, t_s, smooth_p, t_s, t_s, t_s, smooth_p, t_s, t_s, t_s, smooth_p, t_s, t_s, t_s, smooth_p, t_s, t_s, t_s, smooth_p, t_s, t_s, t_s, smooth_p, t_s, t_s]

    fun_twist = [u, p, straight, p, straight, p, straight, p, straight, p, straight, p, straight, p, straight, p, straight, p, straight, p, straight, p, straight, p, straight, straight, straight, d, straight, d, straight, m, straight, m, straight, m, straight, m, straight, m, straight, m, straight, m, straight, m, straight, m, straight, m, straight, m, straight, m, straight, p, straight, straight, straight, p, straight, straight, straight]

    fun_twist_samer = [u, p, straight, p, straight, p, straight, p, straight, p, straight, p, straight, p, straight, p, straight, p, straight, p, straight, p, straight, p, straight, straight, p, straight, p, straight, p, straight, p, straight, p, straight, p, straight, p, straight, p, straight, p, straight, p, straight, p, straight, p, straight, straight, d, straight, d, straight, m, straight, m, straight, m, straight, m, straight, m, straight, m, straight, m, straight, m, straight, m, straight, m, straight, m, straight, m, straight, p, straight, straight, straight, p, straight, straight, straight]


    rules = Rules({right : [straight, smooth_p, straight],
                    looping : [straight, u, straight, u, straight, u, straight, u, m, m, m, m, straight, d, straight, d, straight, d, straight, d, straight, d, straight, d, straight, d, straight, d, p, p, p, p, straight, u, straight, u, straight, u, straight, u, straight],
                    f : [f, p, m, u, f],
                    track : [track, track, u, track, track, d, track, track, d, track, track, u],
                    t_s :   [[0.1428, [t_s, p, t_s, m]],
                            [0.1428, [t_s, m, t_s, p]],
                            [0.1428, [t_s, smooth_m, t_s, smooth_p]],
                            [0.1428, [t_s, straight]],
                            [0.1428, [straight, t_s]],
                            [0.1428, [smooth_m, smooth_m, u, smooth_m, smooth_m, smooth_m, d, d, smooth_m, smooth_m, smooth_m]],
                            [0.1432, [t_s, straight, looping, straight, t_s]]]})

    lsystem = LSystem(rules, math.pi / 4, math.pi / 8, 1, (0.0, 0.0, 0.0))

    symbols = lsystem.expand(fun_twist, 3)

    pos = lsystem.compute_symbols(symbols)

    return pos
