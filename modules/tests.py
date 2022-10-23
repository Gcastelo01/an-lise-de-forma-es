from random import sample
import pandas as pd
import numpy as np


def bootstrap_mean(x, n=5000, size=None):
  """
  Realiza teste de Bootstrap em um vetor

  @param x: vetor de dados
  @n: número de testes a serem realizados
  @size: tamanho da amostra
  
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
  
  """
  baixo = np.percentile(x, low)
  alto = np.percentile(x, high)

  return (baixo, alto)