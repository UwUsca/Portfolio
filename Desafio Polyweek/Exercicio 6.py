
class Informacoes:
    def __init__(self):
        self.vetor = [2, 6, 4, 8, 9, 2, 5, 6, 7, 2, 3, 4, 4, 5, 4, 8, 1, 4, 9, 3]

    def math_moda(self):
        maiorQtde = 0
        moda = 0
        cont = 0
        for i in range(len(self.vetor)):
            aux = self.vetor[i]
            for j in range(len(self.vetor)):
                if self.vetor[j] == aux:
                    cont += 1
            if cont >= maiorQtde:
                maiorQtde = cont
                moda = self.vetor[i]
            cont = 0
        return moda

    def math_media(self):
        return sum(self.vetor)/len(self.vetor)

    def math_maior(self):
        aux = 0
        for i in range(len(self.vetor)):
            if aux < self.vetor[i]:
                aux = self.vetor[i]
        return aux

    def math_menor(self):
        aux = self.math_maior()
        for i in range(len(self.vetor)):
            if aux > self.vetor[i]:
                aux = self.vetor[i]
        return aux

    def math_soma(self):
        return sum(self.vetor)

    def run(self):
        print("Vetor: {}\n"
              "Moda: {}\n"
              "Média aritmédica: {}\n"
              "Maior valor: {}\n"
              "Menor valor: {}\n"
              "Soma de todos os valores: {}".format(self.vetor, self.math_moda(), self.math_media(), self.math_maior(),
                                                    self.math_menor(), self.math_soma()))


if __name__ == '__main__':
    info = Informacoes()
    info.run()

'''
Exercicio 6:

Dado o vetor A abaixo, construa um algoritmo que imprima
no console as seguintes informações do vetor:
§ Moda
§ Média aritmética
§ Maior valor
§ Menor valor
§ Soma de todos os valores
A = 2 6 4 8 9 2 5 6 7 2 3 4 4 5 4 8 1 4 9 3
'''