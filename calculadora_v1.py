# Calculadora em Python

# Desenvolva uma calculadora em Python com tudo que você aprendeu nos capítulos até aqui no curso. 
# A solução será apresentada no próximo capítulo!

print("\n******************* Calculadora em Python *******************")

def calc():

    operacao = int(input ('Digita o número correspondente a operação que quer fazer: \n 1 - soma \n2 - diferença \n 3 - divisão \n 4 - multiplicação \n'))
    num1 = float(input('Digite o primeiro número: '))
    num2 = float(input('Digite o segundo número: '))


    if operacao == 1:
        soma = num1 + num2
        print(soma)
    elif operacao == 2:
        dif = num1 - num2
        print (dif)
    elif operacao == 3:
        div = num1/num2
        print (div)
    elif operacao == 4:
        multi = num1 * num2
        print(multi)
    else:
        print('operacao invalida')

calc()