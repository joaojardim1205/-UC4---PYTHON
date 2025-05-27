class ContaBancaria:
    def __init__(self, saldo):
        saldo.__saldo = saldo

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor

    def ver_saldo(self):
        return self.__saldo
    
conta = ContaBancaria(100)
conta.depositar(50)

print('Saldo atual:', conta.ver_saldo())