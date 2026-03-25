petit programme pédagogique et personnel codé en python pour créer, hacher, et cracker des mots de passe avec brute force et hash cat.

Avec ce programme il est possible de tester la solidité d'un mot de passe soit avec une attaque de brute force python simple(très lente, totalement inefficace
sur un mot de passe de plus de 3 ou 4 caractères) soit avec une attaque de brute force effectuée par le logiciel externe Hashcat(très rapide et efficace).

Ces deux attaques ont des performances très différentes. 

Ce programme permet alors également de faire des estimations sur la durée nécessaire pour cracker un mot de passe donné si celui-ci est trop complexe et pour python 
et pour hashcat. 
Lorsque mises à l'épreuve de mot de passe qui suivent les recommendations de l'Agence nationale de la sécurité des systèmes d’information ces deux attaques 
bruteforce s'avèrent largement inefficaces(durée estimée qui va de plusieurs années jusqu'à des échelles de temps cosmiques et inhumaines). 

Soit il s'agit d'un défaut de conception de mon programme soit il s'agit de l'inefficience complète des attaques bruteforce en général.

Hashcat est déjà préinstallé 

## Prérequis

- Python 3.8+
- pip
- cx_Freeze

---

# Installation

## 1. Cloner le projet

git clone -b master https://github.com/adm971/test-mot-de-passe.git


---

# Installation sur Windows

1. Installer Python depuis :
https://www.python.org/downloads/

2. Installer cx_Freeze :

python -m pip install cx_Freeze

3. Compiler le programme :

python setup.py build

4. Lancer le programme :

un dossier "build" sera créé avec un sous dossier "exe.win" dans le quel se trouve "main.exe"
Lancer main.exe
