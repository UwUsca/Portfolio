class Relogio:
    def __init__(self):
        self.inicio = ""
        self.termino = ""
        self.running = True

    def get_inputs(self, inpX, inpNome):
        inpX = input("{}: ".format(inpNome))
        return inpX

    def splice_inp(self, inpX):
        inpX = inpX.lower()
        inpX = inpX.replace(" horas e ", ",")
        inpX = inpX.replace(" minutos", ",")
        inpX = inpX.split(",")

        if len(inpX) > 2:
            inpX.pop()
        for i in range(2):
            inpX[i] = int(inpX[i])
        return inpX

    def check_inp(self, inpX):
        if 0 < inpX[0] <= 23 and 0 <= inpX[1] <= 60:
            return True
        else:
            print("Horas ou minutos invalidos")
            return False

    def check_horarios(self):
        if self.inicio[0] > self.termino[0]:
            print("Horário Inválido\n")
        else:
            if self.inicio[0] >= self.termino[0] and self.inicio[1] > self.termino[1]:
                print("Horário Inválido\n")

    def math_horario(self, horaX, horaY):
        horaX = (horaX[0] * 60) + horaX[1]
        horaY = (horaY[0] * 60) + horaY[1]
        self.running = False
        return horaY - horaX

    def run(self):
        while self.running:

            while True:
                self.inicio = self.get_inputs(self.inicio, "Inicio")
                self.inicio = self.splice_inp(self.inicio)
                if self.check_inp(self.inicio):
                    break
                else:
                    pass
            while True:
                self.termino = self.get_inputs(self.termino, "Termino")
                self.termino = self.splice_inp(self.termino)
                if self.check_inp(self.termino):
                    break
                else:
                    pass

            self.check_horarios()
            print("Duração: {} minutos de duração".format(self.math_horario(self.inicio, self.termino)))


if __name__ == '__main__':
    r = Relogio()
    r.run()

'''
Exercicio 5:

Construa um algoritmo que receba através do input do
teclado a hora e minuto de início de um jogo e a hora e
minuto do final do jogo. Calcule a duração do jogo em
minutos, sabendo-se que o tempo máximo de duração do
jogo é de 24 horas e que o jogo deve iniciar e finalizar no
mesmo dia.
'''