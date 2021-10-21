
class Matriz:
    def __init__(self):
        self.nums = [5, 1, 9, 0, 7, 6, 2, 1, 2]
        self.matriz = []

    def math(self):
        for i in range(3):
            self.matriz.append([])
        for i in range(len(self.nums), 0, -1):
            if i >= 7:
                self.matriz[0].append(self.nums[i-1])
            elif 6 >= i >= 4:
                self.matriz[1].append(self.nums[i-1])
            elif i <= 3:
                self.matriz[2].append(self.nums[i-1])

    def print_math(self):
        print("Numeros: {}\n"
              "Matriz: \n {}\n {}\n {}".format(self.nums, self.matriz[0], self.matriz[1], self.matriz[2]))

    def run(self):
        self.math()
        self.print_math()


if __name__ == '__main__':
    m = Matriz()
    m.run()

'''
Exercicio 4:

Data a matriz A abaixo, construa um algoritmo que imprima
no console os valores desta matriz na ordem contrária, do
último elemento (5) até o primeiro elemento (2):
§ 5 1 9 0 7 6 2 1 2
'''