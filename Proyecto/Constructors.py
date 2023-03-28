class Constructor:
    def __init__(self, name, team_id, nationality, pilots, puntos):
        self.name=name
        self.team_id=team_id
        self.nationality=nationality
        self.pilots= pilots
        self.puntos=puntos

    def mostrar(self):
        return f"Name: {self.name}\nTeam ID: {self.team_id}\nNationality: {self.nationality}\nPilots: {self.pilots}\n"
    
    #esta funcion busca los constructores por el pais
    def buscarconstructor(self, pais):
        if self.nationality==pais:
            print(f'{self.name}')
    
    def buscarpilotos(self, constructor):
        if self.team_id==constructor:
            print(f'{self.pilots}')
