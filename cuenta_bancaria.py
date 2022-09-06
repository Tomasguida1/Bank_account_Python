from os import system
class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellidos = apellido
    
class Cliente(Persona):
    def __init__(self, nombre, apellido, numero_cuenta, balance = 0):
        super().__init__(nombre, apellido)
        self.numero_cuenta = numero_cuenta
        self.balance = balance

        
    def imprimir(self):
        return print(f"el cliente {self.numero_cuenta} tiene un balance de {self.balance}")
    
    def depositar(self):
        deposito = int(input("ingrese cuanto dinero va a depositar: "))
        self.balance +=  deposito
        return self.balance
    
    def retirar(self):
        retiro = int(input("ingrese cuanto dinero va a retirar: "))
        if self.balance >= retiro:
            self.balance -= retiro
            return self.balance
        else: 
            print ("el monto que desea extraer es mayor al que posee en el banco")

def crear_cliente():
        nombre = input("ingrese el nombre del cliente: ")
        apellido = input("ingrese el apellido del cliente: ")
        numero_cuenta = int(input("ingrese el numero de cuenta: "))
        cliente = Cliente(nombre,apellido,numero_cuenta)
        return cliente
    
def inicio():
    """nombre = input("ingrese el nombre del cliente: ")
    apellido = input("ingrese el apellido del cliente: ")
    numero_cuenta = int(input("ingrese el numero de cuenta: "))
    #balance = int(input("ingrese el saldo de la cuenta: "))"""
    op = 0
    cliente = crear_cliente()
    while op != 3:
        op = int(input("ingrese una opcion(1-hacer un deposito/2-retirar un monto/3-salir")) 
        system("cls")
        if op == 1:
            cliente.depositar()
            cliente.imprimir()
            continue
        elif op == 2:
            cliente.retirar()
            cliente.imprimir()
            continue
        
inicio = inicio()