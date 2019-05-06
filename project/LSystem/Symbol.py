import random

class Symbol:
    def __init__(self, str, stochastic = False):
        self.str = str
        self.stochastic = stochastic

    def __str__(self):
        return self.str

class Rules:
    def __init__(self, rules):
        self.rules = rules

    def add(self, symbol, expansion):
        self.rules.update({symbol : expansion})

    def expandSymbol(self, symbol):
        if symbol.stochastic:
            return self.expandSymbolStochastic(symbol)
        else:
            return self.rules.get(symbol, [symbol])

    def expandSymbolStochastic(self, symbol):
        expansions = self.rules.get(symbol, [symbol])

        print(expansions)

        if expansions == [symbol]:
            return expansions
        else:
            prob = random.uniform(0, 1)
            total = 0.0

            for expansion in expansions:
                print(expansion)
                if expansion[0] + total >= prob:
                    return expansion[1]
                else:
                    total += expansion[0]

            raise ValueError

    def length(self):
        return len(self.rules)
