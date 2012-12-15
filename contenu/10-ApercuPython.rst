Généralités sur Python et l'intérêt de son utilisation  
======================================================


Python est un language interprété. L'utilisateur voit immédiatement l'effet de
sa commande. Ce mécanisme s'avère être très utile en sciences où beaucoup de
traitements complexes sont menées pas à pas, en vérifiant et en testant à
chaque pas la validité des résultats. 

Le langage Python rencontre aujourd'hui un engouement très grand dans de
nombreuses communautés scientifiques qui ont la nécessité de "manipuler" des
données et de les faire parler. Ce mouvement est profond et potentiellement
extrèmement fécond car il génère des liens inter-disciplinaires autour de
besoins communs : la maîtrise du calcul, la maîtrise des données, la communication des résultats. 

Pour accompagner ce mouvement et pour l'accentuer, il importe que de plus en
plus de scientifiques s'emparent de ces outils et apprennent à en maîtriser la
puissance et à en apprécier l'élégance. 


Premier exemple 
----------------

Voici un exemple d'une courte session, exécutée dans l'environnement 
interactif Ipython (initié à l'Université de Berkeley par `Fernando
Perez <http://fperez.org>`_ ) qui tend à devenir une plateforme universelle pour l'utilisation du langage
Python dans le domaine des sciences.  

.. ipython::
    
    In [1]: from math import *
    
    In [2]: import scipy.constants as cst

    In [3]: phi = (1+sqrt(5))/2

    In [4]: cos(phi)**2+sin(phi)**2

    In [5]: phi*phi - phi

    In [6]: -(1j*1j).real

    In [7]: cst.epsilon_0*cst.mu_0*(cst.c)**2

    In [8]: [ (k,cst.__dict__[k]) for k in cst.__dict__.keys()[20:29]] 

.. note::    

    La première étape d'un programme Python consiste à charger des modules
    spécialisés. Ceux-ci sont très nombreux et couvrent un très large éventail de
    besoins.  **L'objectif de la formation sera de comprendre les modules importants pour
    le calcul scientifique**
    
Par exemple dans l'exemple précédent le module `math` donne accès aux
fonctions de
la librairie standard `math` du langage C. Sans cette importation, il serait
impossible d'accèder aux fonctions :math:`\sin(x)`, :math:`\cos(x)` et
:math:`\sqrt{x}`. 


.. note::

    Une fonction se reconnait à son prototype qui utilise obligatoirement les
    parenthèses `unnomdefunction()`
    
.. ipython::

    In [1]: exp(1j*pi)


L'interpréteur du langage renvoie un message d'erreur indiquant qu'il ne sait
pas calculer une exponentielle avec un argument complexe. 

C'est gênant. 

Fort heureusement, il existe d'autres modules, plus complets, qui peuvent prendre le relais. 
Parmi ceux-ci le module `numpy`.

.. ipython::
    
    In [2]: from numpy import *
    
    In [1]: exp(1j*pi)

C'est mieux ! Mais viens alors la question : 
Comment fait Python pour savoir quelle exponentielle choisir,
puisqu'il a le choix entre l'exponentielle du module `math` et l'exponentielle 
du module `numpy` ? 

C'est effectivement un problème. Il vient de se créer un conflit entre espaces
de noms : celui du module  `math` et celui de `numpy`. 
Un même nom est partagé par plusieurs modules !

On peut régler ce probléme en important le module différemment. Il y a trois
possibilités : 

    + importer le module (sans son espace de noms)
    + importer le module * (avec son espace de noms)
    + importer le module avec un alias (souvent court par commodité)   

.. ipython::
    
    In [1]: import numpy 

    In [2]: from numpy import *

    In [3]: import numpy as np

**La troisième solution est la bonne pratique**. 

L'inconvénient, c'est qu'il faut alonger le nom des fonctions appartenant au module en les faisant précéder de
**np.**, (**numpy.** dans le premier cas), ce qui nuit (un peu) à la lisibilité du code.

Le grand avantage est que l'on règle ainsi le problème du conflit entre
espaces de noms. Celui ci peut être très gênant et souvent source d'erreurs pénibles
à découvrir (*la fonction appelée n'étant pas la fonction que l'on croit être appelée*).
Ceci peut facilement se produire, car quel développeur peut prétendre avoir
mémorisé l'intégralité des fonctions de tous les modules dont il a l'usage ? 
C'est trop vaste, il faut donc cloisonner, et Python permet cela. 

Bien sûr, si l'usage que l'on a de python implique très peu de modules, l'import * est raisonable. 

Les librairies importantes ont des alias génériques adoptés par tous qu'il
convient d'employer. 

.. ipython::

    In [1]: import numpy as np

    In [1]: import scipy as sp

    In [1]: import scipy.io as ios
    
    In [1]: import scipy.linalg as la

    In [1]: import matplotlib.pyplot as plt
    
    In [1]: import pylab as pl



