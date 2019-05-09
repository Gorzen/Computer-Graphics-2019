try:
    from .LSystems import LSystem
    from .Symbol import Symbol
    from .Symbol import Rules
except:
    from LSystems import LSystem
    from Symbol import Rules
    from Symbol import Symbol
import math

def get_points(iterations):
    straight = Symbol(" straight ", length = 1)
    right = Symbol(" right ")
    f = Symbol("F", length = 1)
    track = Symbol(" track ", length = 1)
    looping = Symbol(" looping ")
    slope = Symbol(" slope ")

    t_s = Symbol(" track stochastic ", stochastic = True)
    t_s_2 = Symbol(" ss ", stochastic = True)

    p = Symbol("+", angle = math.pi/4)
    m = Symbol("-", angle = math.pi/4)
    u = Symbol(" UP ", angle = math.pi/8)
    d = Symbol(" DOWN ", angle = math.pi/8)
    smooth_p = Symbol(" +++ ", length = 1, angle = math.pi/2)
    smooth_m = Symbol(" --- ", length = 1, angle = math.pi/2)

    loop_1 = [straight, p, straight, p, straight, p, straight, p, straight, p, straight, p, straight, p, straight]

    loop = [track, p, track, track, track, p, track, track, track, p, track, track, track, p, track, track, track, p, track, track, track, p, track, track, track, p, track, track, track, p, track, track]

    loop_s = [t_s, smooth_p, t_s, t_s, t_s, smooth_p, t_s, t_s, t_s, smooth_p, t_s, t_s, t_s, smooth_p, t_s, t_s, t_s, smooth_p, t_s, t_s, t_s, smooth_p, t_s, t_s, t_s, smooth_p, t_s, t_s, t_s, smooth_p, t_s, t_s]

    fun_twist = [u, p, straight, p, straight, p, straight, p, straight, p, straight, p, straight, p, straight, p, straight, p, straight, p, straight, p, straight, p, straight, straight, straight, d, straight, d, straight, m, straight, m, straight, m, straight, m, straight, m, straight, m, straight, m, straight, m, straight, m, straight, m, straight, m, straight, m, straight, p, straight, straight, straight, p, straight, straight, straight]

    fun_twist_samer = [u, p, straight, p, straight, p, straight, p, straight, p, straight, p, straight, p, straight, p, straight, p, straight, p, straight, p, straight, p, straight, straight, p, straight, p, straight, p, straight, p, straight, p, straight, p, straight, p, straight, p, straight, p, straight, p, straight, p, straight, p, straight, straight, d, straight, d, straight, m, straight, m, straight, m, straight, m, straight, m, straight, m, straight, m, straight, m, straight, m, straight, m, straight, m, straight, m, straight, p, straight, straight, straight, p, straight, straight, straight]

    rules = Rules({right : [straight, smooth_p, straight],
                    looping : [straight, u, straight, u, straight, u, straight, u, m, m, m, m, straight, d, straight, d, straight, d, straight, d, straight, d, straight, d, straight, d, straight, d, p, p, p, p, straight, u, straight, u, straight, u, straight, u, straight],
                    f : [f, p, m, u, f],
                    slope : [track, track, u, track, track, d, track, track, d, track, track, u],
                    t_s_2 : [[0.25, [p, p, u, straight, straight, straight, straight, d, m, m, t_s_2, m, m, d, straight, straight, straight, straight, u, p, p]],
                            [0.25, [t_s_2]],
                            [0.25, [p, p, t_s_2, m, m, t_s_2, m, m, t_s_2, p, p]],
                            [0.25, [m, m, t_s_2, p, p, t_s_2, p, p, t_s_2, m, m]]],
                    t_s :   [[0.1428, [t_s, p, t_s, m]],
                            [0.1428, [t_s, m, t_s, p]],
                            [0.1428, [t_s, smooth_m, t_s, smooth_p]],
                            [0.1428, [t_s, straight]],
                            [0.1428, [straight, t_s]],
                            [0.1428, [smooth_m, smooth_m, u, smooth_m, smooth_m, smooth_m, d, d, smooth_m, smooth_m, smooth_m]],
                            [0.1432, [t_s, straight, looping, straight, t_s]]]})

    lsystem = LSystem(rules, (0.0, 0.0, 0.0))

    #symbols = lsystem.expand([p, p, straight, m, m, straight, m, m, straight, p, p], 3)
    symbols = lsystem.expand([t_s_2], iterations)

    pos = lsystem.compute_symbols(symbols)

    return pos
