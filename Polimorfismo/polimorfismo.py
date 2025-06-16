class Smartphone:
    def ligar(self):
        print('Smartphone: tocando Melodia de chamada')


class Notebook:
    def ligar(self):
        print('Notebook: iniciando Sistem Operacional')

class SmartTV:
    def ligar(self):
        print('SmartTV: mostrando Logo Nova')

def iniciar_dispositivo(dispositivo):
    dispositivo.ligar()

celular = Smartphone()
laptop = Notebook()
tv = SmartTV()

iniciar_dispositivo(celular)
iniciar_dispositivo(laptop)
iniciar_dispositivo(tv)
