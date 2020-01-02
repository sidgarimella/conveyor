class CodeCell:
    def __init__(self, idx, source):
        self.idx = idx
        self.source = source
        self.state = dict()
        self.output = dict()

    def __str__(self):
        res = ""
        res += "CELL " + str(self.idx) + "\n"
        res += "=============================\n"
        res += self.source
        res += "\n=============================\n"
        return res
