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
    Esta função realiza o cálculo da Progressão Aritmética (PA).
    Recebe os valores inseridos pelo usuário com os dados da PA.
    Retorna uma tupla contendo a lista da sequência da PA e a soma dos seus termos.

    Args:
        a1 (int): Primeiro termo da PA, inserido pelo usuário.
        r (int): Razão da PA, inserida pelo usuário.
        n (int): Quantidade de termos da PA, inserida pelo usuário.

    Returns:
        tuple[list[int], int]: Uma tupla contendo a lista da sequência da PA e a soma total dos termos.
    """
    soma = 0
    sequencia = []
    termo_atual = a1
    for valor in range(n):
        sequencia.append(termo_atual)
        soma += termo_atual
        termo_atual += r
        

    return sequencia, soma

def calculo_pg(a1: int, q: int, n: int) -> tuple[list[int], int]:
    """
    Esta função realiza o cálculo da Progressão Geométrica (PG).
    Recebe os valores inseridos pelo usuário com os dados da PG.
    Retorna uma tupla contendo a lista da sequência da PG e a soma dos seus termos.

    Args:
        a1 (int): Primeiro termo da PG, inserido pelo usuário.
        q (int): Razão da PG, inserida pelo usuário.
        n (int): Quantidade de termos da PG, inserida pelo usuário.

    Returns:
        tuple[list[int], int]: Uma tupla contendo a lista da sequência da PG e a soma total dos termos.
    """
    soma = 0
    sequencia = []
    termo_atual = a1
    for valor in range(n):
        sequencia.append(termo_atual)
        soma += termo_atual
        termo_atual *= q
        

    return sequencia, soma

def calculo_meta_pa(a1: int, r: int, meta: int) -> tuple[list[int], int] | None:
    """
    Esta função verifica quantas voltas são necessárias para a soma da PA ultrapassar a meta.
    Ela gera a sequência da PA e acumula seus termos, adaptando a condição de parada
    conforme a direção do crescimento (progressões crescentes ou decrescentes/negativas).

    Args:
        a1 (int): Primeiro termo da PA, inserido pelo usuário.
        r (int): Razão da PA, inserida pelo usuário.
        meta (int): Meta limite para a soma.

    Returns:
        tuple[int, int]: Uma tupla contendo a soma total dos termos e a quantidade de voltas (termos) necessárias.
    """
    soma = 0
    sequencia = []
    termo_atual = a1

    # Se o primeiro termo for negativo e estiver caindo (r < 0)
    while True:
        sequencia.append(termo_atual)
        soma += termo_atual
        termo_atual += r

        if meta >= 0 and soma > meta:
            return sequencia, soma

        if meta < 0 and soma < meta:
            return sequencia, soma

        # Razão zero: a soma nunca mudará de direção
        if r == 0:
            if a1 == 0:
                return None
            if meta >= 0 and a1 < 0:
                return None
            if meta < 0 and a1 > 0:
                return None

        # PA que cresce, mas não conseguiu atingir a meta negativa
        if r > 0 and meta < 0 and termo_atual >= 0:
            return None

        # PA que diminui, mas não conseguiu atingir a meta positiva
        if r < 0 and meta >= 0 and termo_atual <= 0:
            return None


def calculo_meta_pg(a1: int, q: int, meta: int) -> tuple[list[int], int] | None:
    """
    Esta função verifica quantas voltas são necessárias para a soma da PG ultrapassar a meta.
    Ela gera a sequência da PG e acumula seus termos, adaptando a condição de parada
    conforme a direção do crescimento (progressões crescentes ou decrescentes/negativas).

    Args:
        a1 (int): Primeiro termo da PG, inserido pelo usuário.
        q (int): Razão da PG, inserida pelo usuário.
        meta (int): Meta limite para a soma.

    Returns:
        tuple[int, int]: Uma tupla contendo a soma total dos termos e a quantidade de voltas (termos) necessárias.
    """
    soma = 0
    sequencia = []
    termo_atual = a1

    # Razão positiva: todos os termos mantêm o mesmo sinal
    if a1 == 0:
        return None

    if q == 0:
        if meta >= 0 and a1 > meta:
            return [a1], a1
        if meta < 0 and a1 < meta:
            return [a1], a1
        return None

    if q == 1:
        if meta >= 0 and a1 < 0:
            return None
        if meta < 0 and a1 > 0:
            return None

    if q == -1:
        if meta >= 0 and max(0, a1) <= meta:
            return None
        if meta < 0 and min(0, a1) >= meta:
            return None

    if q > 1:
        if meta >= 0 and a1 < 0:
            return None
        if meta < 0 and a1 > 0:
            return None

    while True:
        sequencia.append(termo_atual)
        soma += termo_atual
        termo_atual *= q

        if meta >= 0 and soma > meta:
            return sequencia, soma

        if meta < 0 and soma < meta:
            return sequencia, soma

