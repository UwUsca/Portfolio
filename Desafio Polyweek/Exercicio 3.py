
class Calendario:
    def __init__(self):
        self.numDias = 0
        self.qtdeHoras = 0
        self.qtdeMins = 0
        self.qtdeSegs = 0

    def get_input(self):
        while True:
            try:
                self.numDias = int(input("Quantidade de Dias: "))
                if self.numDias < 1:
                    print("\nInsira um numero valido de dias\n")
                else:
                    break
            except ValueError:
                print("\nInsira um NUMERO\n")

    def math(self):
        self.qtdeHoras = self.numDias * 24
        self.qtdeMins = self.qtdeHoras * 60
        self.qtdeSegs = self.qtdeMins * 60

    def print_math(self):
        print("Quantidades de dias: {}\n"
              "Total de horas: {}\n"
              "Total de minutos: {}\n"
              "Total de segundos: {}".format(self.numDias, self.qtdeHoras, self.qtdeMins, self.qtdeSegs))

    def run(self):
        self.get_input()
        self.math()
        self.print_math()


if __name__ == '__main__':
    c = Calendario()
    c.run()

'''
Exercicio 3:

Construa um algoritmo que imprima no console a
quantidade de dias, horas, minutos e segundos que tivemos
em um determinado ano. Deverá receber apenas 1 valor
através do input do teclado, para que o usuário possa digitar
a quantidade de dias que teve no ano em que deseja saber os
dados abaixo. Em seguida, deverá imprimir no console os
seguintes dados:

§ Quantidade de horas no ano
§ Quantidade de minutos no ano
§ Quantidade de segundos no ano
'''