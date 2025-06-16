# Modifique a classe ContaBancaria para tomar o saldo privado (saldo). Crie métodos depositar()e sacar() que alterem o saldo, e um método ver_saldo() para acessa-lo

class ContaBancaria:
    def __init__(self, titular, saldo_inicial=0):
        self.titular = titular
        self.__saldo = saldo_inicial

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor

    def sacar(self, valor):
        if 0 < valor <= self.__saldo:
            self.__saldo -= valor

    def ver_saldo(self):
        return self.__saldo

conta = ContaBancaria("João", 100)
conta.depositar(50)
conta.sacar(30)
print(conta.ver_saldo())

