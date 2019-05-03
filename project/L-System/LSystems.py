from Symbol import Rules
from Symbol import Symbol
import numpy as np
import math

slope_angle_limit = math.pi / 3

min_phi = math.pi / 2 - slope_angle_limit
max_phi = math.pi / 2 + slope_angle_limit

class LSystem():
    def __init__(self, rules, theta_step, phi_step, length, p0):
        assert phi_step >= 0 and theta_step >= 0
        self.rules = rules
        self.theta_step = theta_step
        self.phi_step = phi_step
        self.length = length
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
        theta = 0.0
        phi = math.pi / 2
        p = self.p0

        list_pos = [p]

        for s in symbols:
            if s.str == "+":
                theta += self.theta_step
            elif s.str == "-":
                theta -= self.theta_step
            elif s.str == " UP ":
                phi -= self.phi_step
                if phi < min_phi:
                    phi = min_phi
            elif s.str == " DOWN ":
                phi += self.phi_step
                if phi > max_phi:
                    phi = max_phi
            else:
                p = (self.length * math.cos(theta) * math.sin(phi) + p[0], self.length * math.sin(theta) * math.sin(phi) + p[1], self.length * math.cos(phi) + p[2])
                list_pos.append(p)

        return list_pos
