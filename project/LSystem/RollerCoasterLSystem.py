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
    f1 = Symbol("F", length = 1)
    f2 = Symbol("F", length = 2)
    f5 = Symbol("F", length = 5)
    f10 = Symbol("F", length = 10)

    right = Symbol(" right ")
    track = Symbol(" track ")
    looping = Symbol(" looping ")
    slope = Symbol(" slope ")

    t_s = Symbol(" track stochastic ", stochastic = True)
    ts_0_0 = Symbol(" ss ", length = 5, stochastic = True)
    nasty_0_0 = Symbol(" nasty ")

    p = Symbol("+", angle = math.pi/4)
    p3 = Symbol("+", angle = math.pi/3)
    m = Symbol("-", angle = math.pi/4)
    m3 = Symbol("-", angle = math.pi/3)
    u = Symbol(" UP ", angle = math.pi/8)
    u3 = Symbol(" UP ", angle = math.pi/3)
    d = Symbol(" DOWN ", angle = math.pi/8)
    d3 = Symbol(" DOWN ", angle = math.pi/3)
    smooth_p = Symbol(" +++ ", angle = math.pi/2)
    smooth_m = Symbol(" --- ", angle = math.pi/2)

    loop_1 = [f1, p, f1, p, f1, p, f1, p, f1, p, f1, p, f1, p, f1]

    loop_ts_s = [f5, p, f5, p, ts_0_0, p, f5, p, f5, p, ts_0_0, p, f5, p, f5]

    loop_ts_s_u = [u, f5, p, f5, p, d, ts_0_0, u, p, f5, d, d, p, f5, p, u, ts_0_0, d, p, f5, p, f5]

    loop = [track, p, track, track, track, p, track, track, track, p, track, track, track, p, track, track, track, p, track, track, track, p, track, track, track, p, track, track, track, p, track, track]

    loop_s = [t_s, smooth_p, t_s, t_s, t_s, smooth_p, t_s, t_s, t_s, smooth_p, t_s, t_s, t_s, smooth_p, t_s, t_s, t_s, smooth_p, t_s, t_s, t_s, smooth_p, t_s, t_s, t_s, smooth_p, t_s, t_s, t_s, smooth_p, t_s, t_s]

    fun_twist = [u, p, f1, p, f1, p, f1, p, f1, p, f1, p, f1, p, f1, p, f1, p, f1, p, f1, p, f1, p, f1, f1, f1, d, f1, d, f1, m, f1, m, f1, m, f1, m, f1, m, f1, m, f1, m, f1, m, f1, m, f1, m, f1, m, f1, m, f1, p, f1, f1, f1, p, f1, f1, f1]

    fun_twist_samer = [u, p, f1, p, f1, p, f1, p, f1, p, f1, p, f1, p, f1, p, f1, p, f1, p, f1, p, f1, p, f1, f1, p, f1, p, f1, p, f1, p, f1, p, f1, p, f1, p, f1, p, f1, p, f1, p, f1, p, f1, p, f1, f1, d, f1, d, f1, m, f1, m, f1, m, f1, m, f1, m, f1, m, f1, m, f1, m, f1, m, f1, m, f1, m, f1, m, f1, p, f1, f1, f1, p, f1, f1, f1]

    smol_virage = [u, f2, p, f2, p, f2, p, f2, p, f2, d, p, f2, p, f2, d, f1, p, f2, m, f2, m, f2, m, f2, u, m, f2, m, f2, m, f2, m, f2, f1]

    rules = Rules({right : [f1, smooth_p, f1],
                    looping : [f1, u, f1, u, f1, u, f1, u, m, m, m, m, f1, d, f1, d, f1, d, f1, d, f1, d, f1, d, f1, d, f1, d, p, p, p, p, f1, u, f1, u, f1, u, f1, u, f1],
                    slope : [track, track, u, track, track, d, track, track, d, track, track, u],
                    ts_0_0 : [[0.1, [p, p, u, f10, d, m, m, ts_0_0, m, m, d, f10, u, p, p]],
                            [0.1, [p, p, d, f10, u, m, m, ts_0_0, m, m, u, f10, d, p, p]],
                            [0.075, [f1, u, f1, u, f1, u, f1, u, m, m, m, m, f1, d, f1, d, f1, d, f1, d, f1, d, f1, d, f1, d, f1, d, p, p, p, p, f1, u, f1, u, f1, u, f1, u, ts_0_0]],
                            [0.05, [p, f1, p, p, f1, p, f1, m, f1, m, ts_0_0, m, f1, m, f1, ts_0_0, f1, m, f1, f1, m, ts_0_0, m, f1, m, f1, p, f1, p, p, p]],
                            [0.15, [p, p, ts_0_0, m, m, ts_0_0, m, m, ts_0_0, p, p]],
                            [0.15, [m, m, ts_0_0, p, p, ts_0_0, p, p, ts_0_0, m, m]],
                            [0.075, [p3, f1, f1, f1, f1, m3, f1, m3, f1, f1, f1, f1, p3]],
        					[0.075, [m3, f1, f1, f1, f1, p3, f1, p3, f1, f1, f1, f1, m3]],
        					[0.15, [ts_0_0]],
                            [0.075, [u3, f1, f1, f1, f1, d3, f1, d3, f1, f1, f1, f1, u3]]],
                    nasty_0_0 : [p, f1, p, p, f1, p, f1, m, f1, m, ts_0_0, m, f1, m, f1, f1, f1, m, f1, f1, m, f1, m, f1, m, f1, p, f1, p, p, p],
                    t_s :   [[0.1428, [t_s, p, t_s, m]],
                            [0.1428, [t_s, m, t_s, p]],
                            [0.1428, [t_s, smooth_m, t_s, smooth_p]],
                            [0.1428, [t_s, f1]],
                            [0.1428, [f1, t_s]],
                            [0.1428, [smooth_m, smooth_m, u, smooth_m, smooth_m, smooth_m, d, d, smooth_m, smooth_m, smooth_m]],
                            [0.1432, [t_s, f1, looping, f1, t_s]]]})

    lsystem = LSystem(rules, (0.0, 0.0, 0.0))

    #symbols = lsystem.expand([p, p, f1, m, m, f1, m, m, f1, p, p], 3)
    symbols = lsystem.expand(loop_ts_s_u, iterations)

    pos = lsystem.compute_symbols(symbols)

    return pos

print(get_points(1))
