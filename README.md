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

# Pseudo-code ( Algorithme de Gale et Shapley )

Entrée : 

    Deux ensembles finis M (d’hommes) et W (de femmes) de cardinal n ;

    Une famille L de relations de préférences ;
         
Sortie : 

    Un ensemble S de couples engagés (homme ; femme) ;

---

    Initialiser tous les m ∈ M et w ∈ W à célibataire
    
    tant que ∃ homme célibataire m qui peut se proposer à une femme w {
    
       w = femme préférée de m parmi celles à qui il ne s'est pas déjà proposé
       
       si w est célibataire
       
         (m, w) forment un couple
         
       sinon un couple (m', w) existe
       
         si w préfère m à m'
         
           (m, w) forment un couple
           
            m' devient célibataire
            
         sinon
         
           (m', w) restent en couple
           
    }
    
    Retourner l’ensemble S des couples engagés
    
