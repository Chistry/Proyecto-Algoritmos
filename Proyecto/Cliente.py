from Race import Race

class Cliente:
    def __init__(self, name, client_id, age, race, type_ticket, asiento, code, costo):
        self.name=name
        self.client_id=client_id
        self.age=age
        self.race=race
        self.type_ticket=type_ticket
        self.asiento=asiento
        self.code=code
        self.costo=costo
    
    def mostrar(self):
        return f"Name:{self.name}\nID:{self.client_id}\nAge:{self.age}\n{Race.mostrar(self.race)}\nTicket's type:{self.type_ticket}\n"
        
    def codigo(self,codigo_prueba):
        if self.code == codigo_prueba:
            return True
        else:
            return False
        
    def compraba_vip(self):
        if self.type_ticket == "VIP":
            return True
        else:
            return False
        
    def mostrar_circuito(self):
        return Race.mostrarcircuito(self.race)
    
    def validar_cedula(self, cedula):
        if self.client_id == cedula:
            return True
        
    def edad(self):
        return self.age