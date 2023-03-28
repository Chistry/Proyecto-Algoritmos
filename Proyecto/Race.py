class Race:
    def __init__(self, name, race_num, date, circuit, podium) -> None:
        self.name=name
        self.race_num=race_num
        self.date=date
        self.circuit=circuit
        self.podium=podium
    
    def mostrar(self):
        return f'\nName: {self.name} \nRound: {self.race_num}\nDate: {self.date}\nCircuit: {self.circuit}\nPodium:{self.podium}'
    
    #mostrar sin spoilers
    def mostrar_sinpodium(self):
        return f'\nName: {self.name} \nRound: {self.race_num}\nDate: {self.date}\nCircuit: {self.circuit}\n'
    
    def buscarraces(self, circuito):
        if self.circuit==circuito:
            print(f'\nName: {self.name} \nRound: {self.race_num}\nDate: {self.date}\nCircuit: {self.circuit}\nPodium:{self.podium}')
    
    #devolver circuito de la carrera para poder obtenee la capacidad del estadio localizado en el objeto Circuits
    def circuito(self):
        return f'{self.circuit}'
    
    def buscarracesconfechas(self, mes):
        if self.date[5:7]==mes:
            print(f'\nName: {self.name} \nRound: {self.race_num}\nDate: {self.date}\nCircuit: {self.circuit}\nPodium:{self.podium}')

    def buscarcarrerasporronda(self, ronda):
        if self.race_num == ronda:
            return True
        else:
            return False
        
    def mostrarcircuito(self):
        return self.circuit
    