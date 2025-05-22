from datetime import date, datetime
from abc import ABC, abstractmethod
class CuentaBancaria:
    def __init__(self,nombre_titular,dni_titular, fecha_nacimiento, saldo=0):
        self._nombre_titular = nombre_titular       #atributo privado
        self._dni_titular = dni_titular             #atributo privado
        self._fecha_nacimiento = datetime.strptime(fecha_nacimiento, '%Y/%m/%d').date()
        self._saldo = saldo                         #atributo privado

    def obtener_saldo(self):
        return self._saldo
    
@classmethod
@abstractmethod    
def depositar(self,monto):
    if monto > 0:
        self._saldo += monto
        print(f"Se ha depositado {monto} a la cuenta de {self._nombre_titular}, su saldo es de: {self.obtener_saldo()}")
    else:
        print("El monto a depositar debeser mayor a 0")

@classmethod
@abstractmethod
def extraer(self,monto):
    if monto <= self.obtener_saldo():
         self._saldo -= monto
         print(f"Se ha extraido {monto} de la cuenta de {self._nombre_titular}, su saldo acutal es de: {self.obtener_saldo()}")
    else:
        print("No posee saldo suficiente para esta operación")

def _caclular_edad(self):
    fecha_actual = date.today()
    edad = fecha_actual - self._fecha_nacimiento
    return edad.days // 365
    
def obtener_edad(self):
    return self._caclular_edad()

class CuentaAhorro(CuentaBancaria):
    def __init__(self, numero_cuenta, saldo):
        super().__init__(numero_cuenta, saldo)
        self.__tasa_interes = 0.001  # Tasa de interés fija
   
    def calcular_interes(self):
        interes = self.saldo * self.__tasa_interes
        return interes
    def agregar_interes(self):
        interes = self.calcular_interes()
        self.saldo += interes
        return interes
    
    def obtener_saldo(self):
        return self._saldo


--------------------------------------------------------------------------------------------------------------------------------
CuentaAhorro.py
from CuentaBancaria import CuentaBancaria

class CuentaAhorro:
     def __init__(self,numero_cuenta, saldo : 0.001):
          self._numero_cuenta = numero_cuenta
          self._saldo = saldo
------------------------------------------------------------------------------------------------------------------------------
test
from CuentaBancaria import CuentaBancaria

cuenta1 = CuentaBancaria("Gabriel",333333,'1990/02/03',15000)

print(cuenta1.obtener_edad())

cuenta1= CuentaBancaria("123456789", 1000)

print("Saldo inicial:", cuenta1.consultar_saldo())
cuenta1.depositar(500)
print("Saldo después de depositar:", cuenta1.consultar_saldo())
interes = cuenta1.calcular_interes()
print("interes" , interes)
print("Interés calculado:", interes)
cuenta1.agregar_interes()
print("Saldo después de agregar interés:", cuenta1.consultar_saldo())
