
import random

class Pilots:
    def __init__(self, name, lastname, birthday, nationality, number, team, puntos):
        self.name=name
        self.lastname=lastname
        self.birthday=birthday
        self.nationality=nationality
        self.number=number
        self.team=team
        self.puntos=puntos
        self.nombres=[]
    
    def mostrar(self):
        return f'\nName: {self.name} {self.lastname}\nBirth date: {self.birthday}\nPilot nationality: {self.nationality}\nNumber: {self.number}'
    
    def podium(self):
        return f'{self.name} {self.lastname}'
    
    def comparapiloto(self, piloto, puntos):
        if piloto==[f'{self.name} {self.lastname}']:
            self.puntos+=puntos

    def punto(self):
        return [self.lastname,self.puntos]
    
    def buscar_teamsganadores(self, piloto, puntos):
        if piloto == self.lastname:
            return (self.team, puntos)

    
