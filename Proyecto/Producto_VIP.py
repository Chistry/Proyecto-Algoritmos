class Producto_VIP:
    def __init__(self, name, product_type, price):
        self.name=name
        self.product_type=product_type
        self.price=price

    def mostrar(self):
        return f"Product's name: {self.name}\nType of Product: {self.product_type}\nPrice: {self.price}"
    
    def validar_nombre(self, nombre):
        if self.name==nombre:
            return True
    
    def precio(self):
        return self.price