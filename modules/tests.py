from dataclasses import replace
import numpy as np


def bootstrap_mean(x, column=None, n=5000, size=None) -> np.ndarray:
    """
    Realiza teste de Bootstrap em um vetor

    @param x: vetor de dados
    @param column: Coluna a ser trabalhada
    @param n: número de testes a serem realizados
    @param size: tamanho da amostra

    @return: vetor com as médias de cada permutação.
    """
    if size is None:
        size = len(x)

    values = np.zeros(n)

    for i in range(n):
        sample = np.random.choice(x, size=size, replace=True)

        values[i] = sample.mean()

    return values


def confidence_interval(x, low=2.5, high=97.5) -> tuple:
    """
    Dado um np.ndarray, gera um intervalo de confiança baseado nos percentis definidos nos parâmetros.

    @param x: Array de dados
    @param low: Margem inferior do IC
    @param high: Margem superior do IC

    @return tupla com valores superior e inferior do IC.
    """
    baixo = np.percentile(x, low)
    alto = np.percentile(x, high)

    return (baixo, alto)


def IC_Classico(df, column):
    '''
    Faz um IC clássico usando o teorema central do limite.

    Parâmetros
    ----------
    df: o dataframe
    column: a coluna que queremos focar
    n: número de amostras para o bootstrap
    size: tamanho de cada amostra, por padrão vira o tamanho do df.
    '''
    data = df[column]
    mean = data.mean()
    std = data.std(ddof=1)
    se = std / np.sqrt(len(data))

    return (mean - 1.96 * se, mean + 1.96 * se)


def AB_test(data1, data2, column, n=5000, size=None) -> np.ndarray:
    if size is None:
        size = len(data1)

    values = np.zeros(n)

    for i in range(n):
        sample1 = data1[column].sample(size, replace=True)
        sample2 = data2[column].sample(size, replace=True)
        values[i] = sample1.mean() - sample2.mean()

    return values


def victories_complement(array_s) -> np.ndarray:
    array_s.replace(0, 2)
    array_s.replace(1, 0)
    array_s.replace(2, 1)

    return array_s