=======================================
Formation Python et Python Scientifique
=======================================

Introduction
------------

Ce document est destiné à élaborer collaborativement une formation
à Python et Python scientifique (Numpy, Scipy, matplotlib, ...)
à destination des enseignants des classes préparatoires aux grandes écoles.

La formation, prévue sur *deux jours* comporte 2x4 séances de 1h30 (12h au total),
avec

* un premier jour centré sur Python "en générale" 
* et le 2ème sur Python scientifique


.. image:: images/plan_formation.png
    :width: 500 px

Pour rendre un peu plus concrets les concepts présentés, chaque séance s'appuira sur
un ou des exemples.


Première journée : Le langage Python 
-------------------------------------


Séance 1 : Un apercu des possibles utilisations de Python
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+ Objectif de la formation 
+ Présentation générale du monde Python
    + Historique 
    + `Le tao de python <http://www.willmcgugan.com/blog/tech/2009/3/7/live-your-life-by-the-tao-of-python/>`_
    + Les différentes communautés Python 
    + Modules et espace de nom  
    + Les bibliothèques - modules
        + numpy scipy matplotlib 
        + scikit-image scikits-learn   
        + networkx, shapely  
        + simpy, SymPy 

+ les outils de travail avec Python
    + éditeur de texte + IPython (commandes intéractives + `%run`)
    + environnement de développement intégré (ex. Spyder)
    + Notebook IPython (proche de Maple/Mathematica)


Séance 2 : Éléments de base du language
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

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
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    + traitement des chaines de caractères
        + s.replace() 
        + s1 + s2 
    + un exemple de regexp simple
    + type de fichiers 
        + mode d'accès
    + glob.glob 


Séance 4 : Python Objet & Bases de données
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    + Classe 
    + Méthodes
    + Surcharge d'opérateurs 

    + Construire un exemple de classe progressivement 

        Idéalement un exemple avec l'utilisation d'une base de données MySQL
        utiliser `pymysql`



--------------------------------------
Deuxième journée : Python Scientifique
--------------------------------------

Séance 5 : Calcul numérique avec Numpy
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    + Lecture fichiers (type structuré) 

    + Algèbre de base 

    + broadcasting 

    + stacking(hstack,vstack,dstack) 

    + boucle ou pas boucle einsum vs numba comme exemple 

Séance 6 : Graphiques avec Matplotlib
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    + `visite de la grande galerie <http://matplotlib.org/gallery.html>`_ 

    + construction d'un graphe simple en 2d en ajoutant des éléments
      graduellement pour enrichir le graphe (légendes, titre, ....) 

    + imshow , contouplot 
     
    + 3D ? 

Séance 7 : Calcul scientifique avec Scipy
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    + optimisation 
    + intégration, ode
    + stats

Séance 8 : Cas pratique de mise en oeuvre
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    1. Récupérer des données physiques ouvertes sur le réseau (T°, ...)
    2. Appliquer un traitement 
    3. Mettre en forme une représentation graphique des données



.. toctree::
   :maxdepth: 2
    
   seances.rst
   

