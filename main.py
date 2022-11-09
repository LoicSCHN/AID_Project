import sys
import subprocess
subprocess.check_call([sys.executable, "-m", "pip", "install", "pandas"])
subprocess.check_call([sys.executable, "-m", "pip", "install", "iteration_utilities"])
import pandas as pd
from iteration_utilities import duplicates

subprocess.call("generator.py", shell=True)
prefEtudiant = pd.read_csv("fichierEleves.csv", header=None, sep = ",").values.tolist() 

prefEtablissement = pd.read_csv("fichierEtablissements.csv", header=None, sep = ",").values.tolist()

file = open("resultat.txt", "w") 

def attribution(n, prefEtudiant, prefEtablissement):
    print("Tous les etudiants sont libres au debut : ", file=file)
    etudiantLibre = list(range(n))
    print("Liste des etudiants libres : {}".format(etudiantLibre), file=file)
    # Aucun etudiant n'a d'affectation
    affectationEtudiant = [None] * n     
    print("affectation etudiant {}".format(affectationEtudiant), file=file)                 
    # Aucun etablissement n'a d'etudiant
    affectationEtablissement = [None] * n  
    print("affectation etablissement {}".format(affectationEtablissement), file=file)                    
    # Aucun etudiant n'a fait de proposition on est donc sur le choix 1 (0) de chaque etudiant
    suivant = [0] * n  
    print("suivant : {}".format(suivant), file=file)                     
    etape = 0
    # Tant que tous les etudiants n'ont pas d'affectation:
    while etudiantLibre:
        etape = etape +1
        print("  ", file=file)
        print("-------------------------------------------------------------------------------------------", file=file)
        print("  ", file=file)
        print("Etape : {}".format(etape), file=file)
        # On prend le premier des etudiants lilbres
        etudiant = etudiantLibre[0] 
        print("On prend l'etudiant : {}".format(etudiant), file=file)                     
        # On prend ses preferences
        prefEtudiantLibre = prefEtudiant[etudiant]  
        print("Preferences de l'etudiant {}".format(etudiant)," : {}".format(prefEtudiantLibre) , file=file)
        # On prend le choix n de l'etudiant
        etablissement = prefEtudiantLibre[suivant[etudiant]] 
        print("Le choix numero : {}".format(suivant[etudiant])," de l'etudiant : {}".format(etudiant) ," est  : {}".format(etablissement), file=file)
        # On prend le classement de l'elève
        prefEtablissementEleve = prefEtablissement[etablissement]
        print("Classement de l'elève : {}".format(prefEtablissementEleve), file=file)
        # On prend l'etudiant actuellement affecte à cet etablissement
        etudiantActuel = affectationEtablissement[etablissement]
       
        
        if etudiantActuel == None:
          #Si il n'y a pas d'etudiant dejà affecte à cet etablissement la demande est accepte
          affectationEtablissement[etablissement] = etudiant
          affectationEtudiant[etudiant] = etablissement
          print("Aucun etudiant n'est dejà affecte a cet etablissement.", file=file)
          print("{}".format(etudiant)," affecte à l'etablissement : {}".format(etablissement), file=file)
          print("Affectation des etablissements : {}".format(affectationEtablissement), file=file)
          print("Affectation des etudiants : {}".format(affectationEtudiant), file=file)
          #Son choix suivant passe à la femme suivante dans sa liste
          suivant[etudiant] = suivant[etudiant] + 1
          #On l'enlève de la liste des etudiants libres
          etudiantLibre.pop(0)
        else:
          #Si il y a dejà un etudiant affecte à cet etablissement
          print("Preferences de l'etablissement : {}".format(prefEtablissementEleve), file=file)
          print("L'etudiant : {}".format(etudiantActuel)," est deja affecte à l'etablissement {}".format(etablissement) , file=file)

          # On regarde les preferences de l'etablissement pour les 2 elèves
          indexEtudiantActuel = prefEtablissementEleve.index(etudiantActuel)
          
          indexEtudiant2 = prefEtablissementEleve.index(etudiant)
          
          if indexEtudiantActuel > indexEtudiant2:
             #L'etablissement prefere le nouvel etudiant
             print("{}".format(etudiant)," est prefere à {}".format(etudiantActuel),  file=file)
             affectationEtablissement[etablissement] = etudiant
             print("{}".format(etudiant)," affecte à l'etablissement : {}".format(etablissement), file=file)
             affectationEtudiant[etudiant] = etablissement
             suivant[etudiant] = suivant[etudiant] + 1
             #On l'enlève de la liste des etudiants libres
             etudiantLibre.pop(0)
             #L'autre etudiant n'a plus d'etablissement
             etudiantLibre.insert(0,etudiantActuel)
          else:
            print("{}".format(etudiantActuel)," est prefere à {}".format(etudiant), file=file)
            print("Son choix {}".format(suivant[etudiant])," est refuse {}", file=file)
            suivant[etudiant] = suivant[etudiant] + 1
             
           
    
  
    return affectationEtudiant


res = attribution(len(prefEtudiant), prefEtudiant, prefEtablissement)
print("  ", file=file)
print("----------------------------------RESULTATS-----------------------------------------", file=file)
print("  ", file=file)
print("{}".format(res), file= file)
print("{}".format(list(duplicates(res))))
print(res)
print("Le détail du résultat est dans resultat.txt")

file.close()