#Funções para o projeto 1

def verifica_numero_natural(entrada: int) -> bool:
    """
    Esta função verifica se o número digitado pelo usuário é positivo e maior que 0:

    Args:
        numero (int) = Número inserido pelo usuário.
    
    Returns:
        bool
    """
    try:
        val = int(entrada)
        return val > 0
    except ValueError:
        return False 

def verifica_diferente_zero(entrada: int) -> bool:
    """
    Esta função verifica se o número digitado pelo usuário é diferente de 0.
    
    Args:
        numero (int) = Número inserido pelo usuário.
    
    Returns:
        bool
    """
    try:
        val = int(entrada)
        return val != 0
    except ValueError:
        return False

def verifica_numero(entrada: int) -> bool:
    """
    Esta função verifica se o número digitado pelo usuário é um número de inteiro.

    Args:
        numero (int) = Número inserido pelo usuário.

    Returns:
        bool
    """

    try:
        int(entrada)
        return True
    except ValueError:
        return False


def calculo_pa(a1: int, r: int, n: int) -> tuple[list[int], int]:
    """
    Esta função realiza o cálculo da Progressão Aritimética.
    Recebe os valores inseridos pelo usuários com os dados da PA.
    Retorna uma tupla contendo a lista da sequência da PA e a soma dos termos.
    
    Args:
        a1 (int) = Primeiro termo da PA, inserido pelo usuário.
        r (int) = Razão da PA, inserido pelo usuários.
        n (int) = Quantidade de termos da PA, inserida pelo usuário.
    
    Returns:
        pa (list) = Lista contendo a sequência da PA.
    
    """
    soma = 0
    sequencia = []
    termo_atual = a1
    for valor in range(n):
        sequencia.append(termo_atual)
        soma += termo_atual
        termo_atual += r
        

    return sequencia, soma



