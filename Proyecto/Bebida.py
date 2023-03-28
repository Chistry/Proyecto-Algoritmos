from Producto_VIP import Producto_VIP

class Bebida(Producto_VIP):
    def __init__(self, name, product_type, price, tipo_bebida):
        super().__init__(name, product_type, price)
        self.tipo_bebida=tipo_bebida

    def mostrar_bebida(self):
        return f'{super().mostrar()}\nType: {self.tipo_bebida}\n'
    
    def buscar_nombre(self, nombre):
        if self.name == nombre:
            return True
        else:
            return False
    
    def ver_precio(self, precio):
        if self.price == precio:
            return True
        
    def bebida_alcoholica(self):
        if self.tipo_bebida == 'alcoholic':
            return True
