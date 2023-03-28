
class Restaurants:
    def __init__(self, name, circuit, products):
        self.circuit=circuit
        self.name=name
        self.products=products

    def mostrar(self):
        return f'Name:{self.name}\nCircuit:{self.circuit}\nProducts:{self.products}'

