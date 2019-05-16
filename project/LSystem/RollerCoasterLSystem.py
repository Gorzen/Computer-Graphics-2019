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
    ### Old parts
    #fun_twist = [u, p, f1, p, f1, p, f1, p, f1, p, f1, p, f1, p, f1, p, f1, p, f1, p, f1, p, f1, p, f1, f1, f1, d, f1, d, f1, m, f1, m, f1, m, f1, m, f1, m, f1, m, f1, m, f1, m, f1, m, f1, m, f1, m, f1, m, f1, p, f1, f1, f1, p, f1, f1, f1]
    #fun_twist_samer = [u, p, f1, p, f1, p, f1, p, f1, p, f1, p, f1, p, f1, p, f1, p, f1, p, f1, p, f1, p, f1, f1, p, f1, p, f1, p, f1, p, f1, p, f1, p, f1, p, f1, p, f1, p, f1, p, f1, p, f1, p, f1, f1, d, f1, d, f1, m, f1, m, f1, m, f1, m, f1, m, f1, m, f1, m, f1, m, f1, m, f1, m, f1, m, f1, m, f1, p, f1, f1, f1, p, f1, f1, f1]


    # ALL SYMBOLS
    ## Straight symbols
    f1 = Symbol("F", length = 1)
    f2 = Symbol("F", length = 2)
    f5 = Symbol("F", length = 5)
    f10 = Symbol("F", length = 10)

    ## Twists
    twist_p_5 = Symbol(" TWIST ^ ", length = 5)
    twist_p_10 = Symbol(" TWIST ^ ", length = 10)
    twist_m_5 = Symbol(" TWIST v ", length = 5)
    twist_m_10 = Symbol(" TWIST v ", length = 10)
    semi_twist_p = Symbol(" SEMI TWIST ^ ", length = 5)
    semi_twist_m = Symbol(" SEMI TWIST  v ", length = 5)

    ## Stochastic track
    ts_0_0 = Symbol(" ss ", length = 5, stochastic = True)

    ## Turning symbols, theta and phi
    p = Symbol("+", angle = math.pi/4)
    p3 = Symbol("+", angle = math.pi/3)
    m = Symbol("-", angle = math.pi/4)
    m3 = Symbol("-", angle = math.pi/3)
    u = Symbol(" UP ", angle = math.pi/8)
    u3 = Symbol(" UP ", angle = math.pi/3)
    d = Symbol(" DOWN ", angle = math.pi/8)
    d3 = Symbol(" DOWN ", angle = math.pi/3)

    # RULES
    ## Starting loops
    loop_ts_s_u = [u, f5, p, f5, p, d, ts_0_0, u, p, f5, d, d, p, f5, p, u, ts_0_0, d, p, f5, p, f5]

    ## Expansion rules
    looping = [f1, u, f1, u, f1, u, f1, u, m, m, m, m, f1, d, f1, d, f1, d, f1, d, f1, d, f1, d, f1, d, f1, d, p, p, p, p, f1, u, f1, u, f1, u, f1, u, f1]
    up_turn = [p, p, u, f10, d, m, m, ts_0_0, m, m, d, f10, u, p, p]
    down_turn = [p, p, d, f10, u, m, m, ts_0_0, m, m, u, f10, d, p, p]
    square_p = [p, p, ts_0_0, m, m, ts_0_0, m, m, ts_0_0, p, p]
    square_m = [m, m, ts_0_0, p, p, ts_0_0, p, p, ts_0_0, m, m]


    rules = Rules({ts_0_0 : [[0.1, up_turn],
                            [0.1, down_turn],
                            [0.075, looping],
                            [0.05, [p, f1, p, p, f1, f1, m, ts_0_0, m, f1, m, ts_0_0, m, f1, m, ts_0_0, m, f1, f1, p, p, f1, p]],
                            [0.15, square_p],
                            [0.15, square_m],
                            [0.075, [p3, f1, f1, f1, m3, f1, f1, m3, f1, f1, f1, p3]],
        					[0.075, [m3, f1, f1, f1, p3, f1, f1, p3, f1, f1, f1, m3]],
        					[0.15, [ts_0_0]],
                            [0.075, [u3, f1, f1, f1, d3, f1, f1, d3, f1, f1, f1, u3]]]})

    start = loop_ts_s_u

    lsystem = LSystem(rules)
    symbols = lsystem.expand(start, iterations)
    pos = lsystem.compute_symbols(symbols)
    return pos

print(get_points(1))
