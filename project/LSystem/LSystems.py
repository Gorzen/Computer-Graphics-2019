try:
    from .Symbol import Rules
    from .Symbol import Symbol
except:
    from Symbol import Rules
    from Symbol import Symbol
import numpy as np
import math

slope_angle_limit = math.pi / 2

min_phi = math.pi / 2 - slope_angle_limit
max_phi = math.pi / 2 + slope_angle_limit

class LSystem():
    def __init__(self, rules, p0 = (0.0, 0.0, 0.0, 0.0)):
        self.rules = rules
        self.p0 = p0

    def expandOnce(self, symbols):
        s = []
        for symbol in symbols:
            print("ExpandOnce: " + str(symbol))
            s += self.rules.expandSymbol(symbol)
            print("Return ExpandOnce: " + str(s))
        return s

    def expand(self, symbols, num_iters):
        s = symbols.copy()
        for i in range(num_iters):
            print("Expand: " + str(s))
            s = self.expandOnce(s)

        return s

    def compute_symbols(self, symbols):
        theta = 0.0
        phi = math.pi / 2
        p = self.p0
        interpolation_n = 8

        list_pos = [p]

        for s in symbols:
            if s.str == "+":
                theta += s.angle
            elif s.str == "-":
                theta -= s.angle
            elif s.str == " +++ ":
                for i in range(1, interpolation_n + 1):
                    p = (s.length * math.cos(theta + i*s.angle/interpolation_n) * math.sin(phi) + p[0],
                     s.length * math.sin(theta + i*s.angle/interpolation_n) * math.sin(phi) + p[1],
                     s.length * math.cos(phi) + p[2], p[3])
                    list_pos.append(p)
                theta += s.angle
            elif s.str == " --- ":
                for i in range(1, interpolation_n + 1):
                    p = (s.length * math.cos(theta - i*s.angle/interpolation_n) * math.sin(phi) + p[0],
                     s.length * math.sin(theta - i*s.angle/interpolation_n) * math.sin(phi) + p[1],
                     s.length * math.cos(phi) + p[2], p[3])
                    list_pos.append(p)
                theta -= s.angle
            elif s.str == " UP ":
                phi -= s.angle
                if phi < min_phi:
                    phi = min_phi
            elif s.str == " DOWN ":
                phi += s.angle
                if phi > max_phi:
                    phi = max_phi
            elif "TWIST" in s.str:
                step = math.pi / s.length
                if "SEMI" not in s.str:
                    step *= 2
                if "v" in s.str:
                    step *= -1
                for i in range(s.length):
                    p = (math.cos(theta) * math.sin(phi) + p[0], math.sin(theta) * math.sin(phi) + p[1], math.cos(phi) + p[2], p[3] + step)
                    list_pos.append(p)
            else:
                p = (s.length * math.cos(theta) * math.sin(phi) + p[0], s.length * math.sin(theta) * math.sin(phi) + p[1], s.length * math.cos(phi) + p[2], p[3])
                list_pos.append(p)

        return list_pos
