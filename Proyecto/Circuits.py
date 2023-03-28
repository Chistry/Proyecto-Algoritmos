class Circuits:
    def __init__(self, name, country, locality, latitude, longitude, capacidad):
        self.name=name
        self.country=country
        self.locality=locality
        self.latitude=latitude
        self.longitude=longitude
        self.capacidad=capacidad
    def mostrar(self):
        return f'\nName: {self.name}\nCountry: {self.country}\nLocality: {self.locality}\nLatitude: {self.latitude}\nLongitude: {self.longitude}'
    
    def mostrarcapacidad(self, circuito):
        if self.name == circuito:
            return self.capacidad

    def buscarcarrera(self, pais):
        if self.country==pais:
            return self.name