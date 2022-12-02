erros = 0
acertos = 0
while True:
    perguntas = input('Quanto é 2+2? ')
    perguntas = int(perguntas)
    
    if perguntas == 4:
        acertos += 1
        print('Você acertou !!')
        pergunta2 = input('Quanto é 5*5? ')
        pergunta2 = int(pergunta2)
        if pergunta2 == 25:
            print('Você está indo muito bem !!')
            acertos += 1
            pergunta3 = input('Quanto é 10/2? ')
            pergunta3 = int(pergunta3)
        elif pergunta2 != 25:
            print('Tente novamente !')
            erros += 1
            continue
        if pergunta3 == 5:
            print('Você zerou o game !!')
            acertos +=1
            break               
        elif pergunta3 !=5:
                print('Tente novamente !')
                erros += 1
                continue
    elif perguntas != 4:
        print('Tente novamente !')
        erros += 1
        continue
print('Acabou o jogo !')
print(f'Você acertou {acertos} perguntas ')
print(f'Você errou {erros} perguntas ')