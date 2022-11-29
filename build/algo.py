import sys
import subprocess
#subprocess.check_call([sys.executable, "-m", "pip", "install", "pandas"])
#subprocess.check_call([sys.executable, "-m", "pip", "install", "iteration_utilities"])
import pandas as pd
from iteration_utilities import duplicates

#subprocess.call("generator.py", shell=True)

#prefEtudiant = pd.read_csv("fichierEleves.csv", header=None, sep = ",").values.tolist() 
#prefEtablissement = pd.read_csv("fichierEtablissements.csv", header=None, sep = ",").values.tolist()
#n = len(prefEtablissement)


def attribution(n, prefEtudiant, prefEtablissement):
   
    etudiantLibre = list(range(n))
    
    affectationEtudiant = [None] * n     
   
    affectationEtablissement = [None] * n  
   
    suivant = [0] * n  
             
    etape = 0
    while etudiantLibre:
        etape = etape +1
       
        # On prend le premier des etudiants lilbres
        etudiant = etudiantLibre[0] 
      
        prefEtudiantLibre = prefEtudiant[etudiant]  
      
        # On prend le choix n de l'etudiant
        etablissement = prefEtudiantLibre[suivant[etudiant]] 
       
        prefEtablissementEleve = prefEtablissement[etablissement]
      
        etudiantActuel = affectationEtablissement[etablissement]
       
        
        if etudiantActuel == None:
          #Si il n'y a pas d'etudiant dejà affecte à cet etablissement la demande est accepte
          affectationEtablissement[etablissement] = etudiant
          affectationEtudiant[etudiant] = etablissement
         
          #Son choix suivant passe à l'etablissement suivante dans sa liste
          suivant[etudiant] = suivant[etudiant] + 1
          #On l'enlève de la liste des etudiants libres
          etudiantLibre.pop(0)
        else:
          #Si il y a dejà un etudiant affecte à cet etablissement
         

          # On regarde les preferences de l'etablissement pour les 2 elèves
          indexEtudiantActuel = prefEtablissementEleve.index(etudiantActuel)
          
          indexEtudiant2 = prefEtablissementEleve.index(etudiant)
          
          if indexEtudiantActuel > indexEtudiant2:
             #L'etablissement prefere le nouvel etudiant
            
             affectationEtablissement[etablissement] = etudiant
            
             affectationEtudiant[etudiant] = etablissement
             suivant[etudiant] = suivant[etudiant] + 1
             #On l'enlève de la liste des etudiants libres
             etudiantLibre.pop(0)
             #L'autre etudiant n'a plus d'etablissement
             etudiantLibre.insert(0,etudiantActuel)
          else:
           
            suivant[etudiant] = suivant[etudiant] + 1
             
           
    
  
    return affectationEtudiant






# retourne la somme des priorités (0, 1, 2) recues dans cette attribution
def etudiantSatisfaction(attribution, prefEtudiant):
    result = 0
    for etudiant,etablissement in enumerate(attribution):
        result = (result + prefEtudiant[etudiant].index(etablissement)) # ajoute 0, 1 ou 2
       
    return 1 - (result /(len(prefEtudiant)*len(prefEtudiant)))

def etablissmentSatisfaction( attribution, prefEtablissement):
    result = 0
    for etudiant,etablissement in enumerate(attribution):
        result = result + prefEtablissement[etablissement].index(etudiant) # ajoute 0, 1 ou 2
        
    return 1 - (result /(len(prefEtablissement)*len(prefEtablissement)))

def fonctionLineaire(x):
    return x

#res = attribution(len(prefEtudiant), prefEtudiant, prefEtablissement)
#res2 = attribution(len(prefEtudiant),prefEtablissement, prefEtudiant)


"""
file = open("testResultats.txt", "w")
#print(res)
print(" ",file=file)
print("Priorite aux eleves : ",file=file)
print("{}".format(res),file = file)
print("Satisfaction des etablissement : ",file = file)
print("{}".format(etudiantSatisfaction(len(prefEtudiant), res, prefEtudiant, prefEtablissement, fonctionLineaire)/n),file = file)
print("Satisfaction des etablissements : ",file = file)
print("{}".format(etablissmentSatisfaction(len(prefEtudiant), res, prefEtudiant, prefEtablissement, fonctionLineaire)/n),file = file)


#print(res)
print(" ",file=file)
print("Priorite aux eleve : ",file=file)
print("{}".format(res),file = file)
print("Satisfaction des etudiants : ",file = file)
print("{}".format(etudiantSatisfaction(len(prefEtudiant), res, prefEtudiant, prefEtablissement, fonctionLineaire)/n),file = file)
print("Satisfaction des etablissements : ",file = file)
print("{}".format(etablissmentSatisfaction(len(prefEtudiant), res, prefEtudiant, prefEtablissement, fonctionLineaire)/n),file = file)



"""