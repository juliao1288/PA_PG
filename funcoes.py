#Funções para o projeto 1

def verifica_numero_natural(numero: int) -> bool:
    """
    Esta função verifica se o número digitado pelo usuário é positivo e maior que 0:

    Args:
        numero (int) = Número inserido pelo usuário.
    
    Returns:
        bool
    """
    if str(numero).isdigit() and int(numero) > 0:
        return True
    else:
        return False 

def verifica_diferente_zero(numero: int) -> bool:
    """
    Esta função verifica se o número digitado pelo usuário é diferente de 0.
    
    Args:
        numero (int) = Número inserido pelo usuário.
    
    Returns:
        bool
    """
    if str(numero).isdigit() and int(numero) != 0:
        return True
    else:
        return 0

def verifica_numero(numero: int) -> bool:
    """
    Esta função verifica se o número digitado pelo usuário é um número de inteiro.

    Args:
        numero (int) = Número inserido pelo usuário.

    Returns:
        bool
    """

    if str(numero).isdigit():
        return True
    else:
        return False