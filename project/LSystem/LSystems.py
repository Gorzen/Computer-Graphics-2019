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
        interpolation_n = 8

        list_pos = [p]

        for s in symbols:
            if s.str == "+":
                theta += s.angle
            elif s.str == "-":
                theta -= s.angle
            elif s.str == " UP ":
                phi -= s.angle
                if phi < min_phi:
                    phi = min_phi
            elif s.str == " DOWN ":
                phi += s.angle
                if phi > max_phi:
                    phi = max_phi
            elif s.str == " END ":
                twist = p[3]
                step = int(abs(twist) // (math.pi / 2))

                for i in range(step):
                    sign = twist / abs(twist)

                    p = (s.length / (step + 1) * math.cos(theta) * math.sin(phi) + p[0], s.length / (step + 1) * math.sin(theta) * math.sin(phi) + p[1], s.length / (step + 1) * math.cos(phi) + p[2], p[3] - sign * math.pi / 2)
                    list_pos.append(p)

                p = (0, 0, 0, 0)
                list_pos.append(p)


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

    def compute_velocity(self, list_pos):
        speed_list = []
        min_speed = 1
        g = 0.2
        friction = 0.8
        previous_pos = list_pos[0]
        previous_speed = 0
        for i, pos in enumerate(list_pos[1:]):
            h = pos[2] - previous_pos[2]
            previous_pos = pos
            if h < 0:
                speed = 0
            else:
                speed = math.sqrt(2*g*h) - friction + previous_speed

            speed = max(speed, min_speed)
            speed_list.append(speed)
            previous_speed = speed

        return speed_list

    def twist_points(self, list_pos):
        speed_list = self.compute_velocity(list_pos)
        previous_pos = list_pos[0]

        twisted_list_pos = [previous_pos]

        for i, pos in enumerate(list_pos[1:-1]):
            next_pos = list_pos[i + 2]

            vec1 = np.array(pos[0:2]) - np.array(previous_pos[0:2])
            vec2 = np.array(next_pos[0:2]) - np.array(pos[0:2])

            alpha = compute_angle(vec1, vec2)

            print('alpha: {}'.format(alpha))

            if abs(alpha) != 0:
                alpha *= speed_list[i]
                new_pos = (pos[0], pos[1], pos[2], pos[3] - alpha)
            else:
                new_pos = (pos[0], pos[1], pos[2], pos[3])

            previous_pos = new_pos
            twisted_list_pos.append(new_pos)

        return twisted_list_pos

def compute_angle(x, y):
    dot = x[0] * y[0] + x[1] * y[1]
    cross = x[0] * y[1] - x[1] * y[0]

    dot = 1 if dot > 1 else dot
    dot = -1 if dot < -1 else dot

    cross = 1 if cross > 1 else cross
    cross = -1 if cross < -1 else cross

    #alpha = +- alpha
    alpha = math.atan2(dot, cross)

    if alpha > math.pi / 2:
        alpha = alpha - math.pi

    return alpha
