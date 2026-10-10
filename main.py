#Explorando PA e PG

import funcoes

def main():

    print("-"*50)
    print(" PA & PG LAB")
    print("-"*50)
    print(" 1 - Progressão Aritimética")
    print(" 2 - Progressão Geométrica")
    print(" 3 - Sair")

    escolha = input("\n Insira sua escolha: ").strip()

    while escolha not in ["1", "2", "3"]:
        print(" Escolha inválida, tente novamente.")
        escolha = input("\n Insira sua escolha: ").strip()

    if escolha == "1":
        entrada_a1 = input(" Insira o primeiro termo da PA: ")
        while not funcoes.verifica_numero(entrada_a1):
            print(" Valor inválido, tente novamente!")
            entrada_a1 = input("\n Insira o primeiro termo da PA: ")
        primeiro_termo = int(entrada_a1)
        
        entrada_r = input(" Insira a razao da PA: ")
        while not funcoes.verifica_diferente_zero(entrada_r):
            print(" Valor inválido, tente novamente!")
            entrada_r = input(" Insira a razao da PA: ")
        razao = int(entrada_r)

        entrada_n = input(" Insira a quantidade de termos da PA: ")
        while not funcoes.verifica_numero_natural(entrada_n):
            print(" Valor inválido, tente novamente!")
            entrada_n = input(" Insira a quantidade de termos da PA: ")
        qtd_termos = int(entrada_n)

        sequencia, soma = funcoes.calculo_pa(primeiro_termo, razao, qtd_termos)

        print(sequencia)
        print(soma)

        
    elif escolha == "2":
        entrada_a1 = input(" Insira o primeiro termo da PG: ")
        while not funcoes.verifica_numero(entrada_a1):
            print(" Valor inválido, tente novamente!")
            entrada_a1 = input("\n Insira o primeiro termo da PG: ")
        primeiro_termo = int(entrada_a1)

        entrada_r = input(" Insira a razao da PG: ")
        while not funcoes.verifica_diferente_zero(entrada_r):
            print(" Valor inválido, tente novamente!")
            entrada_r = input(" Insira a razao da PG: ")
        razao = int(entrada_r)

        entrada_n = input(" Insira a quantidade de termos da PG: ")
        while not funcoes.verifica_numero_natural(entrada_n):
            print(" Valor inválido, tente novamente!")
            entrada_n = input(" Insira a quantidade de termos da PG: ")
        qtd_termos = int(entrada_n)


if __name__ == "__main__":
    main()
