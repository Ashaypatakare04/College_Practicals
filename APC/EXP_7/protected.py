class Demo:
    def __init__(self, name, id, branch):
        print("Constructor is called!")
        self._name = name
        self._id = id
        self._branch = branch

    def _info(self):
        print("Name:", self._name, "\nRoll NO.:", self._id)

    def branch(self):
        print("Branch:", self._branch)

    def __del__(self):
        print("Destructor is called!")


obj = Demo("ABC", 56, "CSE")

obj.branch()
obj._info()
