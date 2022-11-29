import subprocess
import os
import sys

if len(sys.argv) != 3:
    n = int(input("Entrez le nombre d'élève et établissement : "))
    boucle = int(input("Entrez le nombre de boucle à effectuer : "))
else:
    n = int(sys.argv[1])
    boucle = int(sys.argv[2])


file = open("testResultats.txt", "w") 


for i in range(0,boucle):
    os.system("python generator.py {}".format(n))
    os.system("python main.py {}")
file.close()