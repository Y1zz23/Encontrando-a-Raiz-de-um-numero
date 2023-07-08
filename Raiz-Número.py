import math
n = int(input("Digite um número: "))
raiz = math.sqrt(n)
print("A raiz de {} é igual a {:.2f}".format(n,raiz))

#Método de pegar apenas uma funcao 
#*A variavel até muda, no exemplo acima o math era incluido e no metodo a baixo nao é necessario
from math import sqrt
n = int(input("Digite um número: "))
raiz = sqrt(n)
print("A raiz de {} é igual a {:.2f}".format(n,raiz))

#Método mais otimizado
from math import sqrt
n = int(input("Digite um número: "))
print("A raiz de {} é igual a {:.2f}".format(n,(sqrt(n))))
