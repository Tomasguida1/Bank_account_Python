"""
Bank account programmed using OOP
"""
from os import system


class Persona:
    """class Persona object"""
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellidos = apellido


class Cliente(Persona):
    """class client"""
    def __init__(self, nombre, apellido, numero_cuenta, balance = 0):
        super().__init__(nombre, apellido)
        self.numero_cuenta = numero_cuenta
        self.balance = balance

    def imprimir(self):
        """prints the account's balance"""
        return print(f"el cliente {self.numero_cuenta} tiene un balance de {self.balance}")
    
    def depositar(self):
        """lets you enter money to your account"""
        deposito = int(input("ingrese cuanto dinero va a depositar: "))
        self.balance +=  deposito
        return self.balance
    
    def retirar(self):
        """lets you retire money from your account, and verifies that the amount is lower than the one in the account"""
        retiro = int(input("ingrese cuanto dinero va a retirar: "))
        if self.balance >= retiro:
            self.balance -= retiro
            return self.balance
        else: 
            print ("el monto que desea extraer es mayor al que posee en el banco")


def crear_cliente():
    """function to enter the user's information"""
    nombre = input("ingrese el nombre del cliente: ")
    apellido = input("ingrese el apellido del cliente: ")
    numero_cuenta = int(input("ingrese el numero de cuenta: "))
    cliente = Cliente(nombre,apellido,numero_cuenta)
    return cliente
 
def inicio():
    """main program"""
    opcion_usuario = 0
    cliente = crear_cliente()
    while opcion_usuario != 3:
        opcion_usuario = int(input("ingrese una opcion(1-hacer un deposito/2-retirar un monto/3-salir")) 
        system("cls")
        if opcion_usuario == 1:
            cliente.depositar()
            cliente.imprimir()
            continue
        elif opcion_usuario == 2:
            cliente.retirar()
            cliente.imprimir()
            continue
 
inicio()
