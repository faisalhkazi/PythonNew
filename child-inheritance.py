from oops import calculator


class ChildImpl(calculator):
    num2 = 200

    def __init__(self):
        calculator.__init__(self, 5, 52)

    def getCompleteData(self):
        return self.num + self.num2 + self.summation()

obj = ChildImpl()
print(obj.getCompleteData())