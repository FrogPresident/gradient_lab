class Tensor:

    def __init__(self, value=0, next_node=None, operation=None, operation_object=None,):
        if next_node is None:
            next_node = []
        self.value = value
        int()
        self.next_node = next_node
        self.operation = operation
        self.Operation_Object = operation_object

    def __add__(self, other):
        return Tensor(self.value + other.value, next_node=[self, other], operation="+")

    def __sub__(self, other):
        return Tensor(self.value - other.value, next_node=[self, other], operation="-")

    def __mul__(self, other):
        return Tensor(self.value * other.value, next_node=[self, other], operation="*")

    def __pow__(self, power, modulo=None):
        return Tensor(self.value ** power, next_node=[self, power], operation="**")

    def __str__(self):
        return f'{self.value}'

    def __repr__(self):
        return str(self)



