# Utilisation

Il faut lancer le fichier gui.py dans le dossier build.  
Une interface graphique va s'ouvrir, il suffit d'entrer un nombre d'élèves/établissement et les résultats vont s'afficher dans toutes les cases.




# Projet : Conception et implantation d’un système d’aide à la décision

Le but de ce projet est de faire une analyse critique de l’algorithme du mariage stable. Pour cela, il vous est demandé de :

1. Implanter un programme pour générer des préférences aléatoires des étudiants et des établissements.

2. Implanter l’algorithme du mariage stable.

3. Implanter une interface du système.

4. Proposer une méthode pour mesurer la satisfaction des étudiants ainsi que celle des établissements. Intégrer la méthode dans l’implantation.

5. Tester le programme sur plusieurs jeux de données.

6. Ordonner les deux versions de l’algorithme (priorité aux étudiants et priorité aux établissements) selon l’ordre décroissant de satisfaction globale des étudiants (resp. établissement) par rapport à chaque jeu de données.

7. Proposer une extension du système proposé pour intégrer les représentations compactes des préférences (sans implantation).

**Rendus :**

— Rapport décrivant votre démarche et vos choix (dépôt sur Moodle).

— Code source (dépôt sur Moodle).

— Présentation Orale (15 mn) : Présentation de votre travail & Démonstration du systéme d’aide à la décision.

# Algorithme de Gale et Shapley (Mariage stable)

Entrée : 

    Deux ensembles d'élèves et d'établissement avec leur préférence;

    Une famille L de relations de préférences ;
         

Etape 0 : chaque élève soumet une liste ordonnée de vœux  
Etape 1 : on ne considère que les vœux de rang 1  
 * chaque école considère les élèves qui l’ont classée en 1er vœu  
 * chaque école accepte temporairement les mieux classés dans la limite des places disponibles et rejette les autres.  

. . .  

Etape k : les élèves rejetés à l’étape précédente candidatent
sur leur vœu suivant  
 * chaque école considère conjointement les élèves précédemment
admis et les élèves lui faisant une offre à cette étape  
 * les mieux classés sont temporairement acceptés et les autres
sont rejetés  
L’algorithme se termine au bout d’un nombre fini d’itérations
lorsque plus aucun élève n’est rejeté.
    
Sortie :

    Liste des affectations par couple


