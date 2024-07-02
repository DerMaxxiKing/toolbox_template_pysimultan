

class ExampleClass1:
    def __init__(self, *args, **kwargs):
        self.attr1 = 1
        self.attr2 = 2
        self.attr3 = 0

    def add(self):
        self.attr3 = self.attr1 + self.attr2
