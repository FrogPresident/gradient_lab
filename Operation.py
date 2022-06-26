from Tensor import Tensor


class Operation:
    owner = Tensor()

    def backward(self):
        ...


class AddOps(Operation):
    def __init__(self, x, y):
        self.y = y
        self.x = x
