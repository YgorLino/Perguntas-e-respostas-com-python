
num = input('Digite um número: ')
num = float(num)
def impar_par(numero):
    if num %2 == 0:
        return f' esse número é par {num}'
    return f'esse número é impar {num}'
par = impar_par(num)
print(type(num))
print(par)
