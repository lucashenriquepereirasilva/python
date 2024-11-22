def somalista(valores = []):
    """
    A função somalista, recebe uma   lista de numeros e faz a soma de todos os números da lista e retorna o resultado de soma parameters
    ---------------
    valores:[]

        lista de números para a soma

    returns
    ----------------
    retorna a soma de lista

    """
    resultado = 0
    for i in valores:
        resultado+=i
    return resultado
def maiorvalor(lista=[]):
    """
    A função maiorvalor encontra o valor em uma lista nummerica

    parameters
    ----------
        lista: int[]

    returns
    ----------
        retorna o maior valor da lista

    """
    m = lista[0]
    for i in lista:
        if i > m:
            m = i
    return m


def inverter(palavra=""):
    # vamos ultilizar o comando 
    # len(length-comprimentos) para obter
    # a quantidade de caracters da palavra
    qtd = len(palavra) 
    invertida = ""
    for i in range(qtd-1,-1,-1):
        invertida+=palavra[i]
    return invertida
   
def palindromo(palavra=""):
    org = inverter(palavra).lower()
    if palavra.lower()==org:
        return "É  um palindromo"
    else:
        return "Não é um palindromo"
    
    


















    