class PlResult:
    def __init__(self, list_=None):
        if list_:
            self.li = list_
        else:
            self.li = list()

    def __getattr__(self, method):
        return getattr(self.li, method)

    def __len__(self):
        return len(self.li)

    def __getitem__(self, item):
        return self.li[item]

    def __str__(self):
        return str(self.li)