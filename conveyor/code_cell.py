class Cell:
    def __init__(self, idx, source):
        self.state = dict()
        self.output = dict()
        self.idx = idx
        self.source = source

    def __str__(self):
        res = ""
        res += "Code cell " + str(self.idx) + "\n"
        res += "=============================\n"
        res += self.source
        res += "\n=============================\n"
        res += self.output["stdout"]
        res += str(self.output["result"])
        res += "\n\n" 
        return res
