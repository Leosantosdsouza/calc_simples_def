from calcula_class import subtracao, multiplicacao, soma, divisao

opcao=1

while opcao:

    print("\n Calculadora ")

    print("\n 0. Sair")
    print(" 1. Somar")
    print(" 2. Subtrair")
    print(" 3. Multiplicação")
    print(" 4. Divisão ")

    opcao = int(input(" \n Opção: "))

    if(opcao==1):
        soma()

    if(opcao==2):
        subtracao()

    if(opcao==3):
        multiplicacao()

    if(opcao==4):
        divisao()

