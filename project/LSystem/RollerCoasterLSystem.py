try:
    from .LSystems import LSystem
    from .Symbol import Symbol
    from .Symbol import Rules
except:
    from LSystems import LSystem
    from Symbol import Rules
    from Symbol import Symbol
import math

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
ts_p = Symbol(" ss ", length = 5, stochastic = True)
ts_m = Symbol(" ss ", length = 5, stochastic = True)
ts_squares_p = Symbol(" ss ", length = 5, stochastic = True)
ts_squares_m = Symbol(" ss ", length = 5, stochastic = True)

## Turning symbols, theta and phi
p = Symbol("+", angle = math.pi/4)
p3 = Symbol("+", angle = math.pi/3)
p6 = Symbol("+", angle = math.pi/6)
m = Symbol("-", angle = math.pi/4)
m3 = Symbol("-", angle = math.pi/3)
m6 = Symbol("-", angle = math.pi/6)
u = Symbol(" UP ", angle = math.pi/8)
u3 = Symbol(" UP ", angle = math.pi/3)
d = Symbol(" DOWN ", angle = math.pi/8)
d3 = Symbol(" DOWN ", angle = math.pi/3)

end = Symbol(" END ", length = 10)

# RULES
## Starting loops
loop_ts_s_u = [u, f5, p, f5, p, d, ts_0_0, u, p, f5, d, d, p, f5, p, u, ts_0_0, d, p, f5, p, f5]
loop_ts_s_u_8 = [f2, u, f5, p, f5, p, d, ts_0_0, d, p, f5, p, f5, u, ts_0_0, f2, u, f5, p, f5, p, d, ts_0_0, d, p, f5, p, f5, u, ts_0_0]
loop_ts_s_u_oct_preserve_twist = [u, f3, d, p, ts_0_0, u, f3, d, p, ts_0_0, d, p, f3, u, ts_0_0, d, p, f3, u, f3, ts_0_0, f2, u, f3, p, d, ts_0_0, u, f3, p, d, ts_0_0, p, d, f3, u, ts_0_0, p, d, f3, u, end]

## Expansion rules
looping = [f1, f1, p6, f1, f1, u, f1, u, f1, u, f1, u, m, m, m, m, f1, d, f1, d, f1, d, f1, d, f1, d, f1, d, f1, d, f1, d, p, p, p, p, m6, f1, u, f1, u, f1, u, p6, f1, u, m6, f2]
up_turn_p = [p, p, u, f10, d, m, m, ts_0_0, m, m, d, f10, u, p, p]
up_turn_m = [m, m, u, f10, d, p, p, ts_0_0, p, p, d, f10, u, m, m]
down_turn_p = [p, p, d, f10, u, m, m, ts_0_0, m, m, u, f10, d, p, p]
down_turn_m = [m, m, d, f10, u, p, p, ts_0_0, p, p, u, f10, d, m, m]
square_p = [p, f1, p, p, f1, m, ts_m, f2, m, m, ts_p, m, m, f2, ts_p, m, f1, p, p, f1, p]
square_m = [m, f1, m, m, f1, p, ts_p, f2, p, p, ts_m, p, p, f2, ts_m, p, f1, m, m, f1, m]
small_square_p = [p, p, ts_m, f2, m, m, ts_p, m, m, f2, ts_p, p, p]
small_square_m = [m, m, ts_p, f2, p, p, ts_p, p, p, f2, ts_p, m, m]
final_turn_p = [p3, f3, m3, f2, m3, f3, p3]
final_turn_m = [m3, f3, p3, f2, p3, f3, m3]
final_slope = [u3, f3, d3, f2, d3, f3, u3]
nothing = [ts_0_0]
fun_twist_p = [u, p, f1, p, f1, p, f1, p, f1, p, f1, p, f1, p, f1, p, f1, d, ts_0_0, d, f1, p, f1, p, f1, p, f1, p, f1, p, f1, p, f1, p, f1, p, u]
fun_twist_m = [u, m, f1, m, f1, m, f1, m, f1, m, f1, m, f1, m, f1, m, f1, d, ts_0_0, d, f1, m, f1, m, f1, m, f1, m, f1, m, f1, m, f1, m, f1, m, u]
fun_twist_2_p = [u, p, f1, p, f1, p, f1, p, f1, p, f1, p, f1, p, f1, p, f1, p, f1, p, f1, p, f1, p, f1, p, f1, p, f1, p, f1, p, f1, d, ts_0_0, d, f1, p, f1, p, f1, p, f1, p, f1, p, f1, p, f1, p, f1, p, f1, p, f1, p, f1, p, f1, p, f1, p, f1, p, f1, p, f1, p, u]
fun_twist_2_m = [u, m, f1, m, f1, m, f1, m, f1, m, f1, m, f1, m, f1, m, f1, m, f1, m, f1, m, f1, m, f1, m, f1, m, f1, m, f1, m, f1, d, ts_0_0, d, f1, m, f1, m, f1, m, f1, m, f1, m, f1, m, f1, m, f1, m, f1, m, f1, m, f1, m, f1, m, f1, m, f1, m, f1, m, f1, m, u]

rules = Rules({ts_0_0 : [[0.35, [ts_p]],
                        [0.35, [ts_m]],
                        [0.15, [ts_squares_p]],
                        [0.15, [ts_squares_m]]],
                ts_p : [[0.15, up_turn_p],
                        [0.15, down_turn_p],
                        [0.05, looping],
                        [0.2, fun_twist_p],
                        [0.075, fun_twist_2_p],
                        [0.075, final_turn_p],
                        [0.075, final_slope],
                        [0.04, [twist_p_5]],
                        [0.04, [twist_m_5]],
                        [0.06, [semi_twist_p]],
                        [0.06, [semi_twist_m]],
                        [0.025, nothing]],
                ts_m : [[0.15, up_turn_m],
                        [0.15, down_turn_m],
                        [0.05, looping],
                        [0.2, fun_twist_m],
                        [0.075, fun_twist_2_m],
                        [0.075, final_turn_m],
                        [0.075, final_slope],
                        [0.04, [twist_p_5]],
                        [0.04, [twist_m_5]],
                        [0.06, [semi_twist_p]],
                        [0.06, [semi_twist_m]],
                        [0.025, nothing]],
                ts_squares_p : [[0.5, square_p],
                        [0.5, small_square_p]],
                ts_squares_m : [[0.5, square_m],
                        [0.5, small_square_m]]})

start = loop_ts_s_u_oct_preserve_twist

lsystem = LSystem(rules)

def get_points(iterations):
    symbols = lsystem.expand(start, iterations)
    pos = lsystem.compute_symbols(symbols)
    twisted_pos = lsystem.twist_points(pos)

    return (symbols, pos, twisted_pos)

def one_iteration(symbols):
    symbols = lsystem.expand(symbols, 1)
    pos = lsystem.compute_symbols(symbols)
    twisted_pos = lsystem.twist_points(pos)

    return (symbols, pos, twisted_pos)
