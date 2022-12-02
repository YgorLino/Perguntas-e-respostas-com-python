num = float (input('Digite um número: '))
opcao = int (input ('Escolha um multiplicador: '))
def multiplicar(numero):
        resultado = num*opcao
        return resultado
valor_final = multiplicar(num)
print(valor_final)
