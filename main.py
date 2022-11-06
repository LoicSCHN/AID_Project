import sys
import subprocess
subprocess.check_call([sys.executable, "-m", "pip", "install", "pandas"])
subprocess.check_call([sys.executable, "-m", "pip", "install", "iteration_utilities"])
import pandas as pd
from iteration_utilities import duplicates

subprocess.call("generator.py", shell=True)
prefEtudiant = pd.read_csv("fichierEleves.csv", header=None, sep = ",").values.tolist() 

prefEtablissement = pd.read_csv("fichierEtablissements.csv", header=None, sep = ",").values.tolist()

def attribution(n, prefEtudiant, prefEtablissement):
    etudiantLibre = list(range(n))
    affectationEtudiant = [None] * n     
    affectationEtablissement = [None] * n  
    suivant = [0] * n                     
    etape = 0
    while etudiantLibre:
        etape = etape +1
        etudiant = etudiantLibre[0] 
        prefEtudiantLibre = prefEtudiant[etudiant]  
        etablissement = prefEtudiantLibre[suivant[etudiant]] 
        prefEtablissementEleve = prefEtablissement[etablissement]
        etudiantActuel = affectationEtablissement[etablissement]
       
        
        if etudiantActuel == None:
          affectationEtablissement[etablissement] = etudiant
          affectationEtudiant[etudiant] = etablissement
          suivant[etudiant] = suivant[etudiant] + 1
          etudiantLibre.pop(0)
        else:
          indexEtudiantActuel = prefEtablissementEleve.index(etudiantActuel)
          indexEtudiant2 = prefEtablissementEleve.index(etudiant)
          
          if indexEtudiantActuel > indexEtudiant2:
             affectationEtablissement[etablissement] = etudiant
             affectationEtudiant[etudiant] = etablissement
             suivant[etudiant] = suivant[etudiant] + 1
             etudiantLibre.pop(0)
             etudiantLibre.insert(0,etudiantActuel)
          else:
            suivant[etudiant] = suivant[etudiant] + 1
             
  
    return affectationEtudiant


res = attribution(len(prefEtudiant), prefEtudiant, prefEtablissement)
print("  ")
print("----------------------------------RESULTATS-----------------------------------------")
print("  ")
print(res)
print(list(duplicates(res)))