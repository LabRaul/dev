def soma(a,b):
    return a + b

def chamada_soma():
    a = int(input("Digite um numero: "))
    b = int(input("Digite outro numero: "))
    resultado = soma(a,b)
    print(resultado)

def imc(peso, altura):
    return peso / (altura * altura)

def chamada_imc():
    peso = float(input("Digite o seu peso: "))
    altura = float(input("Digite a sua altura: "))
    resultado = imc(peso, altura)
    print(resultado)

def menu():
    print("Informe a opção desejada:")
    print("1 --> SOMA")
    print("2 --> IMC")
    print("3 --> SAIR")
    
    option = int(input(""))
    if (option == 1):
        chamada_soma()
        menu()
    elif (option == 2):
        chamada_imc()
        menu()
    elif (option == 3):
        quit
    else:
        print("Digita uma opção valida, infeliz!")
        menu()

menu()