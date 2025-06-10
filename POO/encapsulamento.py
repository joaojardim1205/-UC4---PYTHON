class contaBancaria:
    def __init__(self, saldo):
        self.__saldo = saldo 

    def depositar(self, valor):
        self.__saldo += valor

    def ver_saldo(self):
        return self.__saldo
    
conta = contaBancaria(1000)
conta.depositar(500)
print(conta.ver_saldo())