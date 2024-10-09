#Alumno: Francisco Lautaro Coceres
#Division: 115-2
#Parcial 09/10/2024
pacientes = []
def menu():
    opcion = 0
    while opcion != 9:
        print("\n   Bienvenido al Sistema de Gestion de Pacientes   ")
        print("1- Cargar paciente nuevo")
        print("2- Mostrar lista de pacientes")
        print("3- Busqueda de pacientes")
        print("4- Lista por numero de Hist Clinica")
        print("5- paciente con mayor cantidad de días de internacion")
        print("6- Paciente con menor cantidad de días de internacion")
        print("7- Cantidad de pacientes con días de internación mayor a 5 días.")
        print("8- Promedio de dias de internacion total de los pacientes")
        print("9- Salir del Sistema ")
        opcion = int(input('Ingrese una opcion del 1 al 9: ')) 
        match opcion:
                case 1: 
                    cargar_pacientes(pacientes)
                case 2:
                    mostrar_pacientes(pacientes)
                case 3:
                    buscar_pacientes(pacientes)
                case 4:
                    ordenar_pacientes_por_numero()
                case 5:
                    paciente_mayores_dias_internacion(pacientes)
                case 6:
                    paciente_menores_dias_internacion(pacientes)
                case 7:
                    pacientes_mayor_a_5(pacientes)
                case 8:
                    promedio_dias_internado(pacientes)
                case 9:
                    print('Saliendo del menu')
                    break
                case _ :
                    print("Opcion invalida, selleccionar un numero del 1 al 9")
        

def cargar_pacientes(pacientes):
    """Carga nuevos pacientes en el sistema."""
    numero_pacientes = int(input('Ingrese cantidad de pacientes a cargar: '))
    for _ in range(numero_pacientes):
        numero_historia_clinica = int(input('Ingrese el numero de historia clinica del paciente: ') )
        nombre_paciente = str(input('Ingrese el nombre del paciente: '))
        edad_paciente = int(input('Ingrese la edad del paciente: '))
        diagnostico_paciente = str(input('Ingrese el diagnostico del paciente: '))
        cantidad_dias_internacion = int(input('Ingrese cuantos dias lleva internado el paciente: '))
        pacientes.append([numero_historia_clinica, nombre_paciente, edad_paciente, diagnostico_paciente, cantidad_dias_internacion])
    print(f'{numero_pacientes} fueron cargados con exito!')
def mostrar_pacientes(pacientes):
    """Muestra la lista de pacientes registrados en el sistema."""
    if not pacientes:
        print('No se encuentran pacientes registrados en este momento.')
    print('\n  Lista de pacientes   ')
    for paciente in pacientes:
        print(f'Numero de historia clinica, Nombre: {paciente[1]}, Edad: {paciente[2]}, Diagnostico: {paciente[3]}, Dias internado: {paciente[4]}')
        
def buscar_pacientes(pacientes):
    """Busca un paciente por su número de historia clínica."""
    numero_historia_clinica = int(input('ingrese el numero de historia clinica del paciente: '))
    for paciente in pacientes:
        if paciente[0] == numero_historia_clinica:
            print(f'Paciente encontrado, Numero historia clinica: {paciente[0]}, Nombre {paciente[1]}, Edad {paciente[2]}, Diagnostico: {paciente[3]}, Dias Internado: {paciente[4]}')
            return
    print('Paciente no encontrado.')
    
def paciente_mayores_dias_internacion(pacientes):
    """Muestra el paciente con la mayor cantidad de días de internación."""
    paciente_mayores_dias =  pacientes[0]
    if not pacientes:
        print('No se encuentran pacientes registrados en este momento')
    for paciente in pacientes:
        for paciente in pacientes:
            if paciente[4] < paciente_mayores_dias[4]:
                paciente_mayores_dias = paciente
                print(f'El paciente con mas dias internado es: ')
def paciente_menores_dias_internacion(pacientes):
    """Muestra el paciente con la menor cantidad de días de internación."""
    paciente_menos_dias = pacientes[0]
    if not pacientes:
        print('No se encuentran pacientes registrados en este momento')
    for paciente in pacientes:
        if paciente[4] < paciente_menos_dias[4]:
            paciente_menos_dias = paciente
            print(f'El paciente con menos dias internado es {paciente_menos_dias[1]} con {paciente_menos_dias[4]} días.')

def ordenar_pacientes_por_numero(pacientes):
    """Ordena la lista de pacientes por su número de historia clínica."""
    if not pacientes:
        print('No se encuentran pacientes registrados en este momento') 
    if len(pacientes) <= 1:
        return pacientes
    
    pivote = pacientes[-1]
    order_left = []
    order_right = []
    
    for paciente in pacientes[:-1]:
        if paciente[1] <= pivote[1]:
            order_left.append(paciente)
        else:
            order_right.append(paciente)
        return ordenar_pacientes_por_numero(order_left) + [pivote] + ordenar_pacientes_por_numero(order_right)
pacientes_ordenados = ordenar_pacientes_por_numero(pacientes)
print('pacientes ordenados:', pacientes_ordenados)

def pacientes_mayor_a_5(pacientes):
    """Cuenta cuántos pacientes tienen más de 5 días de internación."""
    paciente_mayor_5 = 0
    if not pacientes:
        print('No se encuentran pacientes registrados en este momento')
    for paciente in pacientes:    
        if paciente[4] > 5:
            paciente_mayor_5 += 1
            print(f'la cantidad de pacientes con mas de 5 dias en internacion es de: {paciente_mayor_5}')

def promedio_dias_internado(pacientes):
    """Calcula el promedio de días de internación de todos los pacientes."""
    if not pacientes:
        print('No se encuentran pacientes registrados en este momento')
        return
    total_dias = 0
    for paciente in pacientes:
        total_dias += paciente[4]
    promedio_dias = total_dias / len(pacientes)
    print(f'El promedio de días de internación es: {promedio_dias}')
    
menu()
