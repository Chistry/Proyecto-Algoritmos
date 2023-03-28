import requests
import random
from Pilots import Pilots
from Constructors import Constructor
from Race import Race
from Circuits import Circuits
from Cliente import Cliente
from Restaurants import Restaurants
from Producto_VIP import Producto_VIP
from Alimento import Alimento
from Bebida import Bebida
from Ventas import Ventas

#esta funcion sirve para ordenar los 10 numeros mas grandes
def my_sorted(lst):
    n = len(lst)
    for i in range(n):
        for j in range(0, n-i-1):
            if lst[j] < lst[j+1]:  # cambia el signo de comparación para ordenar de manera descendente
                lst[j], lst[j+1] = lst[j+1], lst[j]
    return lst[:10]

#comprueba si un numero es ondulado
def ondulado(n):
    n = str(n)
    for i in range(len(n)):
        if i % 2 == 0 and n[i] != n[0]:
            return False
        elif i % 2 != 0 and n[i] != n[1]:
            return False
    return True

def es_perfecto(num):
    suma_divisores = 0
    for divisor in range(1, num):
        if num % divisor == 0:
            suma_divisores += divisor
    if suma_divisores == num:
        return True
    else:
        return False

class App:
    def __init__(self):
        url_pilotos= "https://raw.githubusercontent.com/Algorimtos-y-Programacion-2223-2/api-proyecto/main/drivers.json"
        r_pilots= requests.get(url_pilotos)
        self.info_pilots= r_pilots.json()
        self.pilotos= []

        url_constructores= "https://raw.githubusercontent.com/Algorimtos-y-Programacion-2223-2/api-proyecto/main/constructors.json"
        r_constructors= requests.get(url_constructores)
        self.info_constructors= r_constructors.json()
        self.constructores= []
        self.consID=[]
        self.nacionalidades=[]
        
        url_carreras= "https://raw.githubusercontent.com/Algorimtos-y-Programacion-2223-2/api-proyecto/main/races.json"
        r_race= requests.get(url_carreras)
        self.info_race= r_race.json()
        self.carreras= []
        self.circuitos= []
        self.paises=[]
        self.meses=[]
        self.podium=[]

        self.clientes=[]
        self.restaurantes=[]
        self.productos=[]
        self.prices=[]
        self.validacion=False
        self.ventas_restaurants=[]
        
    def organizar(self):
        equipos=[]
        for i in self.info_pilots:
            self.pilotos.append(Pilots(i['firstName'], i['lastName'], i['dateOfBirth'], i['nationality'], i['permanentNumber'], i['team'], 0))
            equipos.append([i['id'], i['team']])
        
        constructores={
            "williams":[],
            "aston_martin":[],
            "alfa":[],
            "alphatauri":[],
            "alpine":[],
            "mercedes":[],
            "haas":[],
            "ferrari":[],
            "mclaren":[],
            "red_bull":[],
        }
        for i in self.info_constructors:
            for j in equipos:
                if j[1]==i['id']:
                    if j[1]=="williams":
                        constructores["williams"].append(j[0])
                    elif j[1]=="aston_martin":
                        constructores["aston_martin"].append(j[0])
                    elif j[1]=="alfa":
                        constructores["alfa"].append(j[0])
                    elif j[1]=="alphatauri":
                        constructores["alphatauri"].append(j[0])
                    elif j[1]=="alpine":
                        constructores["alpine"].append(j[0])
                    elif j[1]=="mercedes":
                        constructores["mercedes"].append(j[0])
                    elif j[1]=="haas":
                        constructores["haas"].append(j[0])
                    elif j[1]=="ferrari":
                        constructores["ferrari"].append(j[0])
                    elif j[1]=="mclaren":
                        constructores["mclaren"].append(j[0])
                    elif j[1]=="red_bull":
                        constructores["red_bull"].append(j[0])
        
        for i in self.info_constructors:
            for key,value in constructores.items():
                if i['id']==key:
                    self.constructores.append(Constructor(i['name'], i['id'], i['nationality'], value, 0))
                    self.nacionalidades.append(i['nationality'])
                    self.consID.append(i['id'])
        
        for j in self.info_race:
            nombres_pilotos=[]
            podium={
                1:[],
                2:[],
                3:[],
                4:[],
                5:[],
                6:[],
                7:[],
                8:[],
                9:[],
                10:[]
            }
            for i in self.pilotos:
                nombres=Pilots.podium(i)
                nombres_pilotos.append(nombres)
            
            random.shuffle(nombres_pilotos)
            
            for posicion in podium:
                if nombres_pilotos:
                    podium[posicion].append(nombres_pilotos.pop(0))
            nombres_restaurantes= []
            


            self.carreras.append(Race(j["name"], j["round"], j["date"], j["circuit"]["name"], podium))
            self.circuitos.append(Circuits(j["circuit"]["name"], j["circuit"]["location"]["country"], j["circuit"]["location"]["locality"], j["circuit"]["location"]["lat"], j["circuit"]["location"]["long"], {
                "general": [j['map']['general'][0],j['map']['general'][1]],
                "vip": [j['map']['vip'][0],j['map']['vip'][1]]
            }))
            self.paises.append(j["circuit"]["location"]["country"])
            self.meses.append(j["date"][5:7])
            self.podium.append(podium)
            #RESTAURANTES:
            for x in j["restaurants"]:
                self.restaurantes.append(Restaurants(x["name"], j["circuit"]["name"], x["items"]))


    def busqueda(self):
        
        print("\nWelcome to the F1 Search Engine\n")
        repetidor=True
        while repetidor:
            try:
                option = int(input("Please choose an option from the menu:\n1 - Search constructors by country (nationality)\n2 - Search drivers by constructor\n3 - Search races by circuit country\n4 - Search all races happening in a month)\n5 - Winners Podium\n6 - Salir\n(Choose an option (1/2/3/4/5/6): \n"))
                if option >= 1 and option <= 6:
                    repetidor=False
                else:
                    raise ValueError
            except ValueError:
                print('\nEnter a correct value\n')

        #buscar constructor por nacionalidad
        if option == 1:
            repetidor=True
            while repetidor:
                repetidor1=True
                while repetidor1:
                    pais = input("\nEnter the nationality of the constructor you wish to search for: ").capitalize()
                    for i in self.nacionalidades:
                        if i!=pais:
                            alternativa=False
                        elif i==pais:
                            repetidor1=False
                            alternativa=True
                            break
                    if alternativa==True:
                        pass
                    elif alternativa==False:
                        print('Enter a correct value')
                    
                
                for i in self.constructores:
                    Constructor.buscarconstructor(i, pais)
                repetidor1=True
                while repetidor1:
                    try:
                        pregunta=int(input('\nTry again?\n1 - Yes\n2 - No\n'))
                        if pregunta >= 1 and pregunta <=2:
                            repetidor1=False
                        else:
                            raise ValueError
                    except ValueError:
                        print('Enter a correct value')
                if pregunta==1:
                    pass
                elif pregunta==2:
                    repetidor=False




        elif option == 2:
            print(self.consID)
            repetidor=True
            while repetidor:
                repetidor1=True
                while repetidor1:
                    constructor = input("Enter the name of the constructor ID to search the pilots: ").lower()
                    for i in self.consID:
                        if i!=constructor:
                            alternativa=False
                        elif i==constructor:
                            repetidor1=False
                            alternativa=True
                            break
                    if alternativa==True:
                        pass
                    elif alternativa==False:
                        print('Enter a correct value')
                for i in self.constructores:
                    Constructor.buscarpilotos(i, constructor)
                repetidor1=True
                while repetidor1:
                    try:
                        pregunta=int(input('\nTry again?\n1 - Yes\n2 - No\n'))
                        if pregunta >= 1 and pregunta <=2:
                            repetidor1=False
                        else:
                            raise ValueError
                    except ValueError:
                        print('Enter a correct value')
                if pregunta==1:
                    pass
                elif pregunta==2:
                    repetidor=False
            
            

        elif option == 3:
            repetidor=True
            while repetidor:
                repetidor1=True
                while repetidor1:
                    country = input("Enter the country of the circuit you wish to search for races in there: ").capitalize()
                    if country == 'Usa' or country == 'United states' or country == 'United states of america' or country == 'America' or country == 'Us':
                        country='USA'
                    elif country == 'Uk' or country == 'United kingdom':
                        country='UK'
                    elif country == 'Uae' or country== 'United arab emirates':
                        country='UAE'
                    for i in self.paises:
                        if i!=country:
                            alternativa=False
                        elif i==country:
                            repetidor1=False
                            alternativa=True
                            break
                    if alternativa==True:
                        pass
                    elif alternativa==False:
                        print('Enter a correct value')
                for i in self.circuitos:
                    va_circuito=Circuits.buscarcarrera(i, country)
                    if va_circuito==None:
                        pass
                    else:
                        for i in self.carreras:
                            Race.buscarraces(i, va_circuito)
                repetidor1=True
                while repetidor1:
                    try:
                        pregunta=int(input('\nTry again?\n1 - Yes\n2 - No\n'))
                        if pregunta >= 1 and pregunta <=2:
                            repetidor1=False
                        else:
                            raise ValueError
                    except ValueError:
                        print('Enter a correct value')
                if pregunta==1:
                    pass
                elif pregunta==2:
                    repetidor=False
            

        elif option == 4:
            print(self.meses)
            repetidor=True
            while repetidor:
                repetidor1=True
                while repetidor1:
                    month = int(input("Enter the month (in numerical format) you wish to search for: "))
                    if month>=1 and month<=12:
                        if month>=1 and month<=9:
                            month='0'+str(month)
                        else:
                            month=str(month)
                        if month=='01' or month=='02' or month=='12':
                            print('It wont be races this month\n')
                    
                    for i in self.meses:
                        if i!=month:
                            alternativa=False
                        elif i==month:
                            repetidor1=False
                            alternativa=True
                            break
                    if alternativa==True:
                        pass
                    elif alternativa==False:
                        print('Enter a correct value')
                    
                
                for i in self.carreras:
                    Race.buscarracesconfechas(i, month)
                repetidor1=True
                while repetidor1:
                    try:
                        pregunta=int(input('\nTry again?\n1 - Yes\n2 - No\n'))
                        if pregunta >= 1 and pregunta <=2:
                            repetidor1=False
                        else:
                            raise ValueError
                    except ValueError:
                        print('Enter a correct value')
                if pregunta==1:
                    pass
                elif pregunta==2:
                    repetidor=False
        
        elif option == 5:
            puntos_pilotos=[]
            puntos_maximos=[]
            puntos_constructores=[]
            for i in self.podium:
                for j in i:
                    if j==1:
                        points=25
                    elif j ==2:
                        points=18
                    elif j ==3:
                        points=15
                    elif j ==4:
                        points=12
                    elif j ==5:
                        points=10
                    elif j ==6:
                        points=8
                    elif j ==7:
                        points=6
                    elif j ==8:
                        points=4
                    elif j ==9:
                        points=2
                    elif j ==10:
                        points=1
                    else:
                        points=0

                    for objeto in self.pilotos:
                        Pilots.comparapiloto(objeto, i[j], points)
                    
            for i in self.pilotos:
                puntos_pilotos.append(Pilots.punto(i))
            for i in puntos_pilotos:
                puntos_maximos.append(i[1])
            
            print('\n🏆🏆🏆PILOTS PODIUM🏆🏆🏆\n')
            puntos_maximos=my_sorted(puntos_maximos)
            
            nombres_impresos = []
            contador=0
            
            for i in puntos_maximos:
                for j in puntos_pilotos:
                    if i == j[1]:
                        if j[0] not in [piloto[0] for piloto in nombres_impresos]:
                            nombres_impresos.append([j[0], i])
                            contador += 1
                            if contador > 10:
                                break
            contador=0
            for i in nombres_impresos:
                contador+=1
                if contador >10:
                    pass
                else:
                    print(f'{contador} - {i[0]}: {i[1]} points!')
            
            print('\n🏆🏆🏆CONSTRUCTORS PODIUM🏆🏆🏆\n')
            equipos = {}
            for i in self.pilotos:
                for j in puntos_pilotos:
                    puntos = Pilots.buscar_teamsganadores(i, j[0], j[1])
                    if puntos is not None:
                        equipo = puntos[0]
                        puntos = puntos[1]
                        if equipo in equipos:
                            equipos[equipo] += puntos
                        else:
                            equipos[equipo] = puntos

            resultados_ordenados = sorted(equipos.items(), key=lambda x: x[1], reverse=True)

            for idx, (equipo, puntos) in enumerate(resultados_ordenados[:10]):
                print(f"{idx+1} - {equipo}: {puntos} points!")

        elif option == 6:
            pass
    
    def gestion_entradas(self):
        repetidor0=True
        while repetidor0:
            repetidor=True
            while repetidor:
                try:
                    nombre= input('What is your name?: ')
                    cedula= int(input('What is your ID?: '))
                    edad= int(input('What is your age?: '))
                    ronda= int(input("Give me the round's numer of the race, if you don't know the number the system could show you.\n1-See races\n2-Put the round race's number\n"))
                    #validar
                    if ronda != 1 and ronda !=2:
                        raise ValueError
                    if ronda == 1:
                        for i in self.carreras:
                            print(Race.mostrar_sinpodium(i))
                        ronda= int(input("Give me the number of the round of races you want to see?: "))
                        if ronda >=1 and ronda<=23:
                            pass
                        else: 
                            raise ValueError
                        ronda=str(ronda)
                    elif ronda ==2:
                        ronda= int(input("Give me the number of the round of races you want to see?: "))
                        if ronda >=1 and ronda<=23:
                            pass
                        else: 
                            raise ValueError
                        ronda=str(ronda)
                    tipo_ticket= int(input("What type of ticket do you want?: \n1-General\n2-VIP\n"))
                    if tipo_ticket != 1 and tipo_ticket !=2:
                        raise ValueError
                    repetidor=False
                except ValueError:
                    print('Put a valid input')
            
            for i in self.carreras:
                carrera=Race.buscarcarrerasporronda(i,ronda)
                if carrera == True:
                    carrera=i
                    break
                elif carrera ==False:
                    carrera='no agarro'

            
            circuito= Race.circuito(carrera)
            
            #comparar cicuito(Race) y cicuito(Circuits) para obtener la capacidad de la carrera
            for i in self.circuitos:
                capacidad=Circuits.mostrarcapacidad(i,circuito)
                if capacidad != None:
                    break
            
            if tipo_ticket== 1:
                tipo_ticket="GENERAL"
                fila= capacidad['general'][0]
                columna= capacidad['general'][1]
            else:
                tipo_ticket="VIP"
                fila= capacidad['vip'][0]
                columna= capacidad['vip'][1]

            # rondas_lista=[]
            # lineas_txt=[]
            # seats= "Seats.txt"
            # with open(seats,'r') as texto:
            

            #     #esto es para limpiar la lista 
            #     for linea in texto:
            #         txt_lista=list(linea)
            #         for i in txt_lista:
            #             if i == '[' or i == ',' or i == ' ' or i == "'" or i ==']' or i == ' ' or i == '=':
            #                 txt_lista.remove(i)
            #         for i in txt_lista:
            #             if i == ' ' or i ==',' or i == '[':
            #                 txt_lista.remove(i)
            #         for i in txt_lista:
            #             if i ==' ' or i == '\n' or i==']':
            #                 txt_lista.remove(i)
            #         for i in range(len(txt_lista)):
            #             if txt_lista[i].isdigit():
            #                 txt_lista[i] = int(txt_lista[i])
            #         rondas_lista.append([txt_lista[0], txt_lista[1]])
            #         lineas_txt.append(txt_lista)
            # for i in range(len(lineas_txt)):
            #     for j in range(len(lineas_txt[i])):
            #         if lineas_txt[i][j] == "1" and j < len(lineas_txt[i]) - 1:
            #             if lineas_txt[i][j+1] == "0":
            #                 lineas_txt[i][j] = "10"
            #                 del lineas_txt[i][j+1]
            #         elif lineas_txt[i][j] == "1" and j < len(lineas_txt[i]) - 1:
            #             if lineas_txt[i][j+1] == "1":
            #                 lineas_txt[i][j] = "11"
            #                 del lineas_txt[i][j+1]
            # lineas_txt = [[str(elem) for elem in sublista] for sublista in lineas_txt]
            
            # for i in range(len(lineas_txt)):
            #     for j in range(len(lineas_txt[i])):
            #         if j > 10 and j+1 < len(lineas_txt[i]):
            #             num = lineas_txt[i][j] + lineas_txt[i][j+1]
            #             lineas_txt[i][j] = num
            #             del lineas_txt[i][j+1]

            # print(lineas_txt)
            
            # if ronda == rondas_lista[0]:
            #     if rondas_lista[1]=='G':
            #         x=1
            #     elif rondas_lista[1]=='V':
            #         x=2
            #     agregar=False
            # elif ronda != rondas_lista[0] or txt_lista is None:
            asientos=[]
            print("What seat do you want?: ")
            puestos=0
            
            # print(txt_lista)
            # for i in range(1,fila+1):
            #     for j in range(1, columna+1):
            #         puestos +=1
            #         print(puestos, end='\t')
            #         asientos.append(puestos)
            #     print('')
            # agregar=True
            repetidor1=True
            seats=[]
            while repetidor1:
                repetidor2=True
                while repetidor2:
                    try:
                        print("What seat do you want?: ")
                        puestos=0
                        # print(txt_lista)
                        for i in range(1,fila+1):
                            for j in range(1, columna+1):
                                puestos +=1
                                print(puestos, end='\t')
                                asientos.append(puestos)
                            print('')

                        asiento= int(input('Answer: '))
                        seats.append(asiento)
                        if asiento >= asientos[0] and asiento <= asientos[-1]:
                            repetidor2=False
                        else:
                            raise ValueError
                    except ValueError:
                        print('Choose an available seat.')
                try:
                    pregunta=int(input('\nWhat do you want to do?\n1 - Add another seat\n2 - Exit\n'))
                    if pregunta >= 1 and pregunta <=2:
                        if pregunta==1:
                            pass
                        elif pregunta == 2:
                            repetidor1=False
                    else:
                        raise ValueError
                except ValueError:
                    print('Put a valid input')

            code=[9,8,7,6,5,4,3,2,1,0,'!','@']
            random.shuffle(code)
            #si se repite algun codigo se mezclan los carateres de la contrasenia 
            if self.clientes==[]:
                pass
            else:
                repetidor3= True
                while repetidor3:
                    for i in self.clientes:
                        prueba= Cliente.codigo(i, code)
                        if prueba == True:
                            random.shuffle(code)
                            break
                        elif prueba == False:
                            repetidor3=False


            separador = ''
            code = separador.join(str(elem) for elem in code)
            #si se repite algun codigo se mezclan los carateres de la contrasenia 
            if self.clientes==[]:
                pass
            else:
                repetidor3= True
                while repetidor3:
                    for i in self.clientes:
                        prueba= Cliente.codigo(i, code)
                        if prueba == True:
                            for i in code:
                                code=list(code)
                            random.shuffle(code)
                            separador = ''
                            code = separador.join(str(elem) for elem in code)
                            break
                        elif prueba == False:
                            repetidor3=False

            if tipo_ticket == 'GENERAL':
                subtotal=150*len(seats)
                precio=150*len(seats)
                iva=precio*0.16
                precio=precio+iva
                if ondulado(cedula) == True:
                    print('YOU WON A 50% DISCOUNT IN YOUR TICKETs :D!\n')
                    descuento=precio/2
                    precio= descuento
                else:
                    descuento="Does not aply"
            elif tipo_ticket == 'VIP':
                subtotal=340*len(seats)
                precio=340*len(seats)
                iva=precio*0.16
                precio=precio+iva
                if ondulado(cedula) == True:
                    print('YOU WON A 50% DISCOUNT IN YOUR TICKETs :D!\n')
                    descuento=precio/2
                    precio= descuento
                else:
                    descuento="Does not aply"
            
            print('*************BILL*************')
            print('Seats:')
            for i in seats:
                if tipo_ticket=="GENERAL":
                    print(f"{ronda}G{i}")
                elif tipo_ticket=="VIP":
                    print(f"{ronda}V{i}")
            print(f'Subtotal: {subtotal}\nIVA: {iva}\nDiscount: {descuento}\nTOTAL: {precio}')
            repetidor1=True
            
            while repetidor1:
                try:
                    pregunta=int(input('\nDo you want to make the purchase?\n1 - Yes\n2 - No\n'))
                    if pregunta >= 1 and pregunta <=2:
                        if pregunta==1:
                            self.clientes.append(Cliente(nombre, cedula, edad, carrera, tipo_ticket, seats ,code, precio))
                            print(f'If you want to cancel the purchase you will need this code: {code}')
                            print('\nSUCCESFUL PAYMENT, ENJOY THE RACE!\n')
                            repetidor1=False
                        elif pregunta == 2:
                            repetidor1=False
                    else:
                        raise ValueError
                except ValueError:
                    print('Put a valid input')
            repetidor1=True
            while repetidor1:
                try:
                    pregunta=int(input('\nDo you want to make another purchase?\n1 - Yes\n2 - No\n'))
                    if pregunta >= 1 and pregunta <=2:
                        if pregunta==1:
                            repetidor1=False
                        elif pregunta == 2:
                            repetidor0=False
                            repetidor1=False
                    else:
                        raise ValueError
                except ValueError:
                    print('Put a valid input')

            
            # for i in asientos:
            #     if i == asiento:
            #         asientos[i-1]="X"

            
                            
            #         # if linea== asientos:
            #             # print('\nHolaaaa\n')
            #             # agregar=True
            #         # else:
            #             # agregar=False
            # texto.close()

            # if tipo_ticket=="GENERAL":
            #     asintos_tipo=f"{ronda}G={asientos}"
            # elif tipo_ticket=="VIP":
            #     asintos_tipo=f"{ronda}V={asientos}"
            
            
            # #esto agrega a seats los asientos
            # if agregar==True:
            #     seats= "Seats.txt"
            #     with open(seats,'a') as archivo:
            #         archivo.writelines('\n')
            #         archivo.writelines(asintos_tipo)
                    
            #     archivo.close()

    def asistencia_carreras(self):
        print("Welcome to the race attendance management module!")
        contraseñas_usadas=[]
        if self.clientes == []:
            print('There are no registered customers')
        else:
            repetidor=True
            while repetidor:
                codigo= input('To access the ticket data insert the code that was given to the client after the purchase:\n')
                if contraseñas_usadas==[]:
                    invalid=False
                    pass
                else:
                    for i in contraseñas_usadas:
                        if i == codigo:
                            print('Invalid ticket, that password has already been used.')
                            invalid=True
                            break
                        else:
                            invalid=False
                if invalid==False:
                    for i in self.clientes:
                        prueba=Cliente.codigo(i,codigo)
                        if prueba == True:
                            print('Approved client')
                            contraseñas_usadas.append(codigo)
                            falso=False
                            break
                        elif prueba == False:
                            falso=True
                    if falso == True:
                        print('Invalid password, there is a possibility that your ticket is fake, if you think so, contact customer service to see if there are any tickets available or if not, try again.')

                repetidor1=True
                while repetidor1:
                    try:
                        pregunta=int(input('\nDo you want to register the attendance of another client?\n1 - Yes\n2 - No\n'))
                        if pregunta >= 1 and pregunta <=2:
                            if pregunta==1:
                                repetidor1=False
                            elif pregunta == 2:
                                repetidor1=False
                                repetidor=False
                        else:
                            raise ValueError
                    except ValueError:
                        print('Put a valid input')
    
    def gestion_restaurantes(self):
        # vips=[]
        # if self.clientes==[]:
        #     print('There are no clients')
        # else:
        #     for i in self.clientes:
        #         VIP=Cliente.compraba_vip(i)
        #         if VIP == True:
        #             vips.append(i)

            # if vips == []:
            #     print('There are no VIP clients')
            # else:
            if self.validacion==False:
                for i in self.info_race:
                    for j in i["restaurants"]:
                        for x in j["items"]:
                            if x['type'].split(':')[0]=='food':
                                precio= float(x['price'])
                                iva=precio*0.16
                                precio= precio+iva
                                self.prices.append(precio)
                                self.productos.append(Alimento(x["name"], x['type'].split(':')[0], precio, x['type'].split(':')[1]))
                            elif x['type'].split(':')[0]=='drink':
                                precio= float(x['price'])
                                iva=precio*0.16
                                precio= precio+iva
                                self.prices.append(precio)
                                self.productos.append(Bebida(x["name"], x['type'].split(':')[0], precio, x['type'].split(':')[1]))
                self.validacion=True
            repetidor=True
            while repetidor:
                try:
                    pregunta=int(input('\nHow do you want to search for the product?:\n1-By name\n2-By type\n3-By price range\n4-Exit\n'))
                    if pregunta >= 1 and pregunta <=4:
                        if pregunta==2:
                            repetidor1=True
                            while repetidor1:
                                try:
                                    pregunta_tipo=int(input('What kind of product do you want?:\n1-Food\n2-Drink\n'))
                                    if pregunta_tipo >= 1 and pregunta_tipo <=2:
                                        if pregunta_tipo==1:
                                            for i in self.productos:
                                                if isinstance(i, Alimento):
                                                    print(Alimento.mostrar_alimento(i))
                                                    repetidor1=False
                                        elif pregunta_tipo == 2:
                                            for i in self.productos:
                                                if isinstance(i, Bebida):
                                                    print(Bebida.mostrar_bebida(i))
                                                    repetidor1=False
                                    else:
                                        raise ValueError
                                except ValueError:
                                    print('Put a valid input')
                        elif pregunta == 1:
                            nombre_producto=input('What is the name of the product you are looking for?: ').lower()
                            for i in self.productos:
                                if isinstance(i, Bebida):
                                    nombre_bebida= Bebida.buscar_nombre(i, nombre_producto)
                                    if nombre_bebida == True:
                                        print(Bebida.mostrar_bebida(i))
                                elif isinstance(i, Alimento):
                                    nombre_bebida= Alimento.buscar_nombre(i, nombre_producto)
                                    if nombre_bebida == True:
                                        print(Alimento.mostrar_alimento(i))
                        elif pregunta == 3:
                            precios={
                                '≤100':[],
                                '≤500':[],
                                '≤999':[],
                                '≥1000':[]
                                }
                            for i in self.prices:
                                if i <= 100:
                                    precios['≤100'].append(i)
                                elif i <= 500:
                                    precios['≤500'].append(i)
                                elif i <= 999:
                                    precios['≤999'].append(i)
                                elif i >= 1000:
                                    precios['≥1000'].append(i)
                            try:
                                rango_producto= int(input('What price range do you prefer?: \n1-Less than or equal to 100$\n2-less than or equal to 500$\n3-less than or equal to 999$\n4-Greater than or equal to $100\n'))
                                if rango_producto>=1 and rango_producto <=4:
                                    for i in self.productos:
                                        if rango_producto == 1:
                                            if isinstance(i, Bebida):
                                                for j in precios['≤100']:
                                                    return_precio=Bebida.ver_precio(i,j)
                                                    if return_precio == True:
                                                        print(Bebida.mostrar_bebida(i))
                                            if isinstance(i, Alimento):
                                                for j in precios['≤100']:
                                                    return_precio=Alimento.ver_precio(i,j)
                                                    if return_precio == True:
                                                        print(Alimento.mostrar_alimento(i))
                                        elif rango_producto == 2:
                                            if isinstance(i, Bebida):
                                                for j in precios['≤500']:
                                                    return_precio=Bebida.ver_precio(i,j)
                                                    if return_precio == True:
                                                        print(Bebida.mostrar_bebida(i))
                                            if isinstance(i, Alimento):
                                                for j in precios['≤500']:
                                                    return_precio=Alimento.ver_precio(i,j)
                                                    if return_precio == True:
                                                        print(Alimento.mostrar_alimento(i))
                                        elif rango_producto == 3:
                                            if isinstance(i, Bebida):
                                                for j in precios['≤999']:
                                                    return_precio=Bebida.ver_precio(i,j)
                                                    if return_precio == True:
                                                        print(Bebida.mostrar_bebida(i))
                                            if isinstance(i, Alimento):
                                                for j in precios['≤999']:
                                                    return_precio=Alimento.ver_precio(i,j)
                                                    if return_precio == True:
                                                        print(Alimento.mostrar_alimento(i))
                                        elif rango_producto == 4:
                                            if isinstance(i, Bebida):
                                                for j in precios['≥1000']:
                                                    return_precio=Bebida.ver_precio(i,j)
                                                    if return_precio == True:
                                                        print(Bebida.mostrar_bebida(i))
                                            if isinstance(i, Alimento):
                                                for j in precios['≥1000']:
                                                    return_precio=Alimento.ver_precio(i,j)
                                                    if return_precio == True:
                                                        print(Alimento.mostrar_alimento(i))
                                        
                                else:
                                    raise ValueError
                            except ValueError:
                                print('Put a valid input')
                        elif pregunta == 4:
                            repetidor=False
                    else:
                        raise ValueError
                except ValueError:
                    print('Put a valid input')
            
    
    def venta_restaurantes(self):
        if self.validacion==False:
            for i in self.info_race:
                for j in i["restaurants"]:
                    for x in j["items"]:
                        if x['type'].split(':')[0]=='food':
                            precio= float(x['price'])
                            iva=precio*0.16
                            precio= precio+iva
                            self.prices.append(precio)
                            self.productos.append(Alimento(x["name"], x['type'].split(':')[0], precio, x['type'].split(':')[1]))
                        elif x['type'].split(':')[0]=='drink':
                            precio= float(x['price'])
                            iva=precio*0.16
                            precio= precio+iva
                            self.prices.append(precio)
                            self.productos.append(Bebida(x["name"], x['type'].split(':')[0], precio, x['type'].split(':')[1]))
            self.validacion=True
        repetidor0=True
        while repetidor0:
            vips=[]
            if self.clientes==[]:
                print('There are no clients')
                repetidor0=False
            else:
                for i in self.clientes:
                    VIP=Cliente.compraba_vip(i)
                    if VIP == True:
                        vips.append(i)

                if vips == []:
                    print('There are no VIP clients')
                else:
                    repetidor=True
                    print('Welcome to the restaurant sales modules')
                    while repetidor:
                        try:
                            cedula=int(input('Give me your ID to place an order: '))
                        except ValueError:
                            print('Please put a valid input')
                            repetidor0=False
                        for i in vips:
                            aprobacion= Cliente.validar_cedula(i, cedula)
                            if aprobacion==True:
                                cliente=i
                                break
                            else:
                                print('Your ID was not found in the system, try again or contact customer service.')
                                repetidor=False
                                repetidor0=False
                        repetidor1=True
                        pedido=[]

                        while repetidor1:
                            try:
                                comidas=input('What food or drink do you want to order?: ').lower()
                                for i in self.productos:
                                    validacion= Producto_VIP.validar_nombre(i,comidas)
                                    if validacion==True:
                                        pedido.append(i)
                                        break
                                
                                if validacion != True:
                                    raise ValueError
                                if pedido == []:
                                    pass
                                else:
                                    for i in pedido:
                                        if isinstance(i, Bebida):
                                            edad= Cliente.edad(cliente)
                                            if edad < 18:
                                                if Bebida.bebida_alcoholica(i) == True:
                                                    print('Underage detected, you can not buy alcoholic beverages')
                                                    pedido.remove(i)
                            except ValueError:
                                print('We do not offer this dish or maybe there was a typing error. If what you ordered is on the menu, try again.')
                            try:
                                pregunta=int(input('Do you want to order something else?\n1-Yes\n2-No\n'))
                                if pregunta >= 1 and pregunta<=2:
                                    if pregunta ==1:
                                        pass
                                    elif pregunta==2:
                                        repetidor1=False
                                else: 
                                    raise ValueError
                            except ValueError:
                                print('Insert a valid input')
                        if pedido == []:
                            print("you didn't order anything to eat, try again")
                            break
                        else:
                            total=0
                            subtotal=0
                            descuento=0
                            costos=0
                            for i in pedido:
                                subtotal+= Producto_VIP.precio(i)
                            costos=subtotal
        
                            if es_perfecto(cedula) == True:
                                descuento=costos*0.15
                                costos= costos- descuento
                            else:
                                descuento='n/a'
                            total= costos
                        
                        repetidor1=True
                        while repetidor1:
                            try:
                                pregunta=int(input('\nDo you want to confirm the purchase??\n1 - Yes\n2 - No\n'))
                                if pregunta >= 1 and pregunta <=2:
                                    if pregunta==1:
                                        self.ventas_restaurants.append(Ventas(cedula, pedido, total))
                                        print('Successful payment!')
                                        print('****************Bill****************')
                                        print(f'ID:{cedula}\nSubtotal:{subtotal}\nDescuento:{descuento}\nTOTAL:{total}\n')
                                        repetidor0=False
                                        repetidor=False
                                        repetidor1=False
                                        
                                        
                                    elif pregunta == 2:
                                        repetidor0=False
                                        repetidor=False
                                        repetidor1=False
                                        
                                else:
                                    raise ValueError
                            except ValueError:
                                print('Put a valid input')




