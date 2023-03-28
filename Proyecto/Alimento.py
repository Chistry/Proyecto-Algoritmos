from Producto_VIP import Producto_VIP

class Alimento(Producto_VIP):
    def __init__(self, name, product_type, price, tipo_alimento):
        super().__init__(name, product_type, price)
        self.tipo_alimento=tipo_alimento

    def mostrar_alimento(self):
        return f'{super().mostrar()}\nType: {self.tipo_alimento}\n'
    
    def buscar_nombre(self, nombre):
        if self.name == nombre:
            return True
        else:
            return False
        
    def ver_precio(self, precio):
        if self.price == precio:
            return True