
class Calculo:
    def __init__(self):
        self.diagMaior = 0
        self.diagMenor = 0
        self.area = 0

    def get_inputs(self):
        while True:
            try:
                self.diagMaior = int(input("Diagonal Maior: "))
                self.diagMenor = int(input("Diagonal Menor: "))
                if self.diagMaior <= 0 or self.diagMenor <= 0:
                    print("\nNúmeros negativos não são validos!\n")
                else:
                    if self.diagMaior < self.diagMenor:
                        aux = self.diagMaior
                        self.diagMaior = self.diagMenor
                        self.diagMenor = aux
                    break
            except ValueError:
                print("\nInsira um NÚMERO válido!\n")

    def print_math(self):
        calcLos = (self.diagMaior * self.diagMenor) /2
        print("Calculo:\n"
              "Area = (D * d)/2\n"
              "Area = ({} * {})/2\n"
              "Area = {}".format(self.diagMaior, self.diagMenor, calcLos))


    def run(self):
        self.get_inputs()
        self.print_math()


if __name__ == '__main__':
    c = Calculo()
    c.run()

'''
Exercicio 1:

Construa um algoritmo que imprima no console a área de um
losango. Deverá receber 2 valores através do input do
teclado para que o usuário possa digitar a diagonal maior e a
diagonal menor. Em seguida, deverá imprimir no console o
cálculo da área.

'''