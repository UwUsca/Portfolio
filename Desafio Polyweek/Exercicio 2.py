
class Tabuada:
    def print_math(self):
        for i in range(10):
            for j in range(10):
                print("{} * {} => {}".format(i+1, j+1, (i+1)*(j+1)))
            print("")

if __name__ == '__main__':
    t = Tabuada()
    t.print_math()

'''
Exercicio 2:

Construa um algoritmo que
calcule a tabuada dos
números de 1 a 10. Não é
necessário nenhuma entrada
pelo input do teclado. Deverá
apenas construir sua lógica
para imprimir no console a
tabuada de todos os números
de 1 a 10
'''