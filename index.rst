.. template documentation master file, created by
   sphinx-quickstart on Sun Oct  7 09:55:51 2012.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Formation Python et Python Scientifique
=======================================

Introduction 
------------

Ce document est destiné à élaborer collaborativement un
contenu de formation à Python et Python scientifique ( Numpy, Scipy, matplotlib, ...) 
à destination des enseignants des classes préparatoires aux grandes écoles. 

Le contenu des deux jours de formation est conçu sur 12 heures (4 séances de
1h30). 

La formation doit permettre d'apréhender par l'exemple les notions de base du langage Python lors de
la première journée, et de découvrir l'utilisation de Python dans le domaine des sciences lors de la seconde journée. 



Première journée : Le langage Python 
-------------------------------------


Séance 1  : Overview
~~~~~~~~~~~~~~~~~~~~

    + Objectif de la formation 
    + Présentation générale du monde Python
        + Historique 
        + `Le tao de python <http://www.willmcgugan.com/blog/tech/2009/3/7/live-your-life-by-the-tao-of-python/>`_
        + Les différentes communautés Python 
        + Les bibliothèques - modules 
            + numpy scipy matplotlib 
            + scikit-imahe scikits-learn   
            + networkx shapely  
            + ...
        + ipython notebook 

            présentation de l'outil en live
            %R
            %Rget 


Séance 2 : Python de base 
~~~~~~~~~~~~~~~~~~~~~~~~~

- structures de données
    + (),[],{}
    + listes en compréhension
    
- éléments du language   
        boucles, conditions, fonctions, itérateur, map , enumerate 

- Exemple en algorithmique de base 

.. ipython::   

    In [1]: def tri1():

    %timeit l1.sort() 

Séance 3 : Chaines et fichiers
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + traitement des chaines de caractères  
        + s.replace() 
        + s1 + s2 
    + un exemple de regexp simple
    + type de fichiers 
        + mode d'accès
    + glob.glob 


Séance 4 : Algorithmique - Python Objet - BDD
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    + Classe 
    + Méthodes
    + Surcharge d'opérateurs 

    + Construire un exemple de classe progressivement 

        Idéalement un exemple avec l'utilisation d'une base de données MySQL
        utiliser `pymysql`

Deuxième journée : Python Scientifique
---------------------------------------

Séance 5 Numpy  
~~~~~~~~~~~~~~~

    + Lecture fichiers (type structuré) 

    + Algèbre de base 

    + broadcasting 

    + stacking(hstack,vstack,dstack) 

    + boucle ou pas boucle einsum vs numba comme exemple 

Séance 6 : Matplotlib 
~~~~~~~~~~~~~~~~~~~~~

    + `visite de la grande galerie <http://matplotlib.og/gallery.html>`_ 

    + constuction graduelle d'un plot 2d en ajoutant des éléments
      graduellement  pour enrichir le graphe (légende, titres, ....) 

Séance 7 : Scipy 
~~~~~~~~~~~~~~~~

    + optimisation 
    + ode 
    + stats  

Séance 8 : Cas pratique de mise en oeuvre
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    1. Récupérer des données physiques ouvertes sur le réseau (T°, ...) 
    2. Appliquer un traitement 
    3. Mettre en forme une représentation graphique des données    
    4. automatisation du script avec crontab    



.. toctree::
   :maxdepth: 2
    
   seances.rst 
   

