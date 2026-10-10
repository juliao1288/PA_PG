#Explorando PA e PG

import funcoes

def main():
    while True:
        print("-"*50)
        print(" PA & PG LAB")
        print("-"*50)
        print(" 1 - Progressão Aritimética")
        print(" 2 - Progressão Geométrica")
        print(" 3 - Cálculo da Meta")
        print(" 4 - Sair")

        escolha = input("\n Insira sua escolha: ").strip()

        while escolha not in ["1", "2", "3", "4"]:
            print(" Escolha inválida, tente novamente.")
            escolha = input("\n Insira sua escolha: ").strip()

        if escolha == "1":
            entrada_a1 = input("\n\n Insira o primeiro termo da PA: ")
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

            print(f" Sequência da PA: {" | ".join(map(str, sequencia))}")
            print(f" A soma dos termos é equivalente a {soma}.")
            print()
            
        elif escolha == "2":
            entrada_a1 = input("\n\n Insira o primeiro termo da PG: ")
            while not funcoes.verifica_numero(entrada_a1):
                print(" Valor inválido, tente novamente!")
                entrada_a1 = input("\n Insira o primeiro termo da PG: ")
            primeiro_termo = int(entrada_a1)

            entrada_q = input(" Insira a razao da PG: ")
            while not funcoes.verifica_diferente_zero(entrada_q):
                print(" Valor inválido, tente novamente!")
                entrada_q = input(" Insira a razao da PG: ")
            quociente = int(entrada_q)

            entrada_n = input(" Insira a quantidade de termos da PG: ")
            while not funcoes.verifica_numero_natural(entrada_n):
                print(" Valor inválido, tente novamente!")
                entrada_n = input(" Insira a quantidade de termos da PG: ")
            qtd_termos = int(entrada_n)

            sequencia, soma = funcoes.calculo_pg(primeiro_termo, quociente, qtd_termos)
            
            print(f" Sequência da PG: {" | ".join(map(str, sequencia))}")
            print(f" A soma dos termos é equivalente a {soma}.")
            print()
            
        elif escolha == "3":
            print(" 1 - Progressão Aritimética")
            print(" 2 - Progressão Geométrica")

            tipo = input("\n Insira sua escolha: ").strip()
            
            while tipo not in ["1", "2"]:
                print(" Escolha inválida, tente novamente.")
                tipo = input("\n Insira sua escolha: ").strip()

            if tipo == "1":
                entrada_a1 = input("\n\n Insira o primeiro termo da PA: ")
                while not funcoes.verifica_numero(entrada_a1):
                    print(" Valor inválido, tente novamente!")
                    entrada_a1 = input("\n Insira o primeiro termo da PA: ")
                primeiro_termo = int(entrada_a1)
                
                entrada_r = input(" Insira a razao da PA: ")
                while not funcoes.verifica_diferente_zero(entrada_r):
                    print(" Valor inválido, tente novamente!")
                    entrada_r = input(" Insira a razao da PA: ")
                razao = int(entrada_r)
    
                entrada_meta = input(" Insira a meta da soma da PA: ")
                while not funcoes.verifica_numero(entrada_meta):
                    print(" Valor inválido, tente novamente!")
                    entrada_meta = input(" Insira a meta da soma da PA: ")
                meta = int(entrada_meta)

                soma, necessario = funcoes.calculo_meta_pa(primeiro_termo, razao, meta)
                
                print("Resultado: ")
                print(f" São necessários {necessario} termo(s) para ultrapassar a meta.")
                print(f" A soma dos termos é equivalente a {soma}.")
                
            elif tipo == "2":
                entrada_a1 = input("\n\n Insira o primeiro termo da PG: ")
                while not funcoes.verifica_numero(entrada_a1):
                    print(" Valor inválido, tente novamente!")
                    entrada_a1 = input("\n Insira o primeiro termo da PG: ")
                primeiro_termo = int(entrada_a1)
    
                entrada_q = input(" Insira a razao da PG: ")
                while not funcoes.verifica_diferente_zero(entrada_q):
                    print(" Valor inválido, tente novamente!")
                    entrada_q = input(" Insira a razao da PG: ")
                quociente = int(entrada_q)
    
                entrada_meta = input(" Insira a meta da soma da PG: ")
                while not funcoes.verifica_numero(entrada_meta):
                    print(" Valor inválido, tente novamente!")
                    entrada_meta = input(" Insira a meta da soma da PG: ")
                meta = int(entrada_meta)

                soma, necessario = funcoes.calculo_meta_pg(primeiro_termo, quociente, meta)

                print("Resultado: ")
                print(f" São necessários {necessario} termo(s) para ultrapassar a meta.")
                print(f" A soma dos termos é equivalente a {soma}.")
            

        elif escolha == "4":
            print(" Você escolheu sair...")
            break


if __name__ == "__main__":
    main()
