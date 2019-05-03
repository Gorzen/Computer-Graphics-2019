class Symbol:
    def __init__(self, str):
        self.str = str

    def __str__(self):
        return self.str

class Rules:
    def __init__(self, rules):
        self.rules = rules

    def add(self, symbol, expansion):
        self.rules.update({symbol : expansion})

    def expandSymbol(self, symbol):
        return self.rules.get(symbol, [symbol])

    def length(self):
        return len(self.rules)
