import random
import csv
import sys



#n = int(input("Entrez le nombre d'élève et établissement : "))
n = int(sys.argv[1])


listeEleve = []
listeEtablissement = []


for i in range(0,n):
    listeEleve.append(i)
    listeEtablissement.append(i)

with open('fichierEleves.csv', 'w', newline='') as f:
    writter = csv.writer(f)
    for i in range(0,len(listeEleve)):  
        random.shuffle(listeEleve)  
        writter.writerow(listeEleve)

f.close()

with open('fichierEtablissements.csv', 'w', newline='') as f:
    writter = csv.writer(f)
    for i in range(0,len(listeEtablissement)): 
        random.shuffle(listeEtablissement)  
        writter.writerow(listeEtablissement)

f.close()