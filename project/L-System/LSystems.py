from Symbol import Rules
from Symbol import Symbol
import numpy as np
import math

class LSystem():
    def __init__(self, rules, rotation_angle_deg, distance, p0):
        self.rules = rules
        self.rotation_angle_deg = rotation_angle_deg
        self.distance = distance
        self.p0 = p0

    def expandOnce(self, symbols):
        s = []
        for symbol in symbols:
            s += self.rules.expandSymbol(symbol)
        return s

    def expand(self, symbols, num_iters):
        s = symbols.copy()
        for i in range(num_iters):
            s = self.expandOnce(s)

        return s

    def compute_symbols(self, symbols):
        d = math.pi/2
        p = self.p0

        list_pos = [p]

        for s in symbols:
            if s.str == "+":
                d += self.rotation_angle_deg
            elif s.str == "-":
                d -= self.rotation_angle_deg
            else:
                p0 = p;
                p = (math.cos(d) + p0[0], math.sin(d) + p0[1])
                list_pos.append(p)

        return list_pos
