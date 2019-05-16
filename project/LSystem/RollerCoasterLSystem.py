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
    #fun_twist = [u, p, f1, p, f1, p, f1, p, f1, p, f1, p, f1, p, f1, p, f1, d, ts_0_0, d, f1, m, f1, m, f1, m, f1, m, f1, m, f1, m, f1, m, f1, m, f1]
    #fun_twist_samer = [u, p, f1, p, f1, p, f1, p, f1, p, f1, p, f1, p, f1, p, f1, p, f1, p, f1, p, f1, p, f1, f1, p, f1, p, f1, p, f1, p, f1, p, f1, p, f1, p, f1, p, f1, p, f1, p, f1, p, f1, p, f1, f1, d, f1, d, f1, m, f1, m, f1, m, f1, m, f1, m, f1, m, f1, m, f1, m, f1, m, f1, m, f1, m, f1, m, f1, p, f1, f1, f1, p, f1, f1, f1]


    # ALL SYMBOLS
    ## Straight symbols
    f1 = Symbol("F", length = 1)
    f2 = Symbol("F", length = 2)
    f3 = Symbol("F", length = 3)
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
    loop_ts_s_u_8 = [f2, u, f5, p, f5, p, d, ts_0_0, d, p, f5, p, f5, u, ts_0_0, f2, u, f5, p, f5, p, d, ts_0_0, d, p, f5, p, f5, u, ts_0_0]

    ## Expansion rules
    looping = [f1, u, f1, u, f1, u, f1, u, m, m, m, m, f1, d, f1, d, f1, d, f1, d, f1, d, f1, d, f1, d, f1, d, p, p, p, p, f1, u, f1, u, f1, u, f1, u, f1]
    up_turn = [p, p, u, f10, d, m, m, ts_0_0, m, m, d, f10, u, p, p]
    down_turn = [p, p, d, f10, u, m, m, ts_0_0, m, m, u, f10, d, p, p]
    square_p = [p, f1, p, p, f1, m, ts_0_0, m, m, ts_0_0, m, m, ts_0_0, m, f1, p, p, f1, p]
    square_m = [m, f1, m, m, f1, p, ts_0_0, p, p, ts_0_0, p, p, ts_0_0, p, f1, m, m, f1, m]
    small_square_p = [p, p, ts_0_0, m, m, ts_0_0, m, m, ts_0_0, p, p]
    small_square_m = [m, m, ts_0_0, p, p, ts_0_0, p, p, ts_0_0, m, m]
    final_turn_p = [p3, f3, m3, f2, m3, f3, p3]
    final_turn_m = [m3, f3, p3, f2, p3, f3, m3]
    final_slope = [u3, f3, d3, f2, d3, f3, u3]
    nothing = [ts_0_0]
    fun_twist = [u, p, f1, p, f1, p, f1, p, f1, p, f1, p, f1, p, f1, p, f1, d, ts_0_0, d, f1, m, f1, m, f1, m, f1, m, f1, m, f1, m, f1, m, f1, m]
    fun_twist_2 = [u, p, f1, p, f1, p, f1, p, f1, p, f1, p, f1, p, f1, p, f1, p, f1, p, f1, p, f1, p, f1, p, f1, p, f1, p, f1, p, f1, d, ts_0_0, d, f1, m, f1, m, f1, m, f1, m, f1, m, f1, m, f1, m, f1, m, f1, m, f1, m, f1, m, f1, m, f1, m, f1, m, f1, m, f1, m]

    rules = Rules({ts_0_0 : [[0.1, up_turn],
                            [0.1, down_turn],
                            [0.075, looping],
                            [0.05, square_p],
                            [0.05, square_m],
                            [0.1, small_square_p],
                            [0.1, small_square_m],
                            [0.05, final_turn_p],
        					[0.05, final_turn_m],
                            [0.05, final_slope],
        					[0.05, [twist_p_5]],
                            [0.05, [twist_m_5]],
                            [0.05, [semi_twist_p]],
                            [0.05, [semi_twist_m]],
                            [0.075, nothing]]})

    start = fun_twist_2

    lsystem = LSystem(rules)
    symbols = lsystem.expand(start, iterations)
    pos = lsystem.compute_symbols(symbols)
    #pos = lsystem.twist_points(pos)
    return pos

print(get_points(0))
