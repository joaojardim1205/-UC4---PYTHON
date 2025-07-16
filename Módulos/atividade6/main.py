# No main.py, crie dois objetos Carro e mostre seus detalhes.

from carro import Carro

carro1 = Carro("Toyota", "Corolla", 2020)
carro2 = Carro("Honda", "Civic", 2021)

print(carro1.detalhes())    
print(carro2.detalhes())