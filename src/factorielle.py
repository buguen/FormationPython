#!/usr/bin/python
#-*- coding:Utf-8 -*-
#
# L'usage de l'anglais est souhaitable dans la docstring des fonctions.
#
# L'usage de l'anglais devrait être toléré dans ce contexte car il s'agit
# d'une bonne pratique qui donne une plus grande valeur d'usage au code
# produit.
#
# Importations par défaut
#
# Préférer :
# import numpy as np
# pour des modules génériques afin d'éviter des collisions entre espaces de noms
#
# %timeit factorielle_v1(30)
# %timeit factorielle_v2(30)
# %timeit factorielle_v3(30)
# L'implémentation scipy est plus lente, on regagne lorsque l'on traite des
# tableaux 
# %timeit factorielle_v3(arange(100))
# %timeit factorial(30)
#
from numpy import *
import scipy as sp
from scipy.misc import factorial
import matplotlib.pyplot as plt
import doctest


def factorielle_v1(n):
    """ calcule la factorielle de l'entier n

    Parameters
    ----------
    n :
        int

    Examples
    --------
    >>> factorielle_v1(0)
    1
    >>> factorielle_v1(1)
    1
    >>> factorielle_v1(2)
    2

    """

    f = 1
    i = 1
    while (i<=n):
        f = f*i
        i = i + 1
    return(f)

def factorielle_v2(n):
    """ calcule la factorielle de l'entier n récursivement

    Parameters
    ----------
    n :
        int

    Examples
    --------

    >>> factorielle_v2(0)
    1
    >>> factorielle_v2(1)
    1
    >>> factorielle_v2(2)
    2

    """
    if (n>1):
        f = n*factorielle_v2(n-1)
    else:
        f = 1

    return(f)

def factorielle_v3(n):
    return factorial(n)

if __name__ == '__main__':
    doctest.testmod()

