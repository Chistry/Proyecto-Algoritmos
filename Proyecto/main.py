from App import App

def main():
    print('WELCOME TO F1\nWait a second...')
    app=App()
    app.organizar()
    repetidor=True
    while repetidor:
        try:
            pregunta=int(input('\nWhat do you want to do?:\n1-Buy tickets\n2-Enter race attendance management\n3-Food management\n4-Restaurant purchasing management\n5-EXIT\n'))
            if pregunta == 1:
                app.gestion_entradas()
            elif pregunta ==2:
                app.asistencia_carreras()
            elif pregunta == 3:
                app.gestion_restaurantes()
            elif pregunta ==4:
                app.venta_restaurantes()
            elif pregunta ==5:
                repetidor=False
        except ValueError:
            print('Insert a valid value')

#695@23140!87
main()