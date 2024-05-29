## *Compétences acquises durant la réalisation ce projet :*
- Déconstruire  des problèmes complexes
- Développer des algorithmes efficaces pour concevoir des solutions adaptées


# Présentation
Ce programme a pour but de créer un algorithme qui déterminera la combinaison d'actions en bourse en se basant sur des fichiers donnés.

Deux versions d'algorithmes sont présentées dans ce programme: 
* Une version bruteforce qui va lister toutes les combinaisons possibles avant de choisir la meilleure.
* Une version qui utilise la programmation dynamique pour optimiser le choix des actions à acheter.


# Instructions
## Prérequis
Avoir installé une version de Python égale ou supérieure à la 3.12.2

## Récupérer le programme
Téléchargement du dossier zip:
[en cliquant ici](https://github.com/marillierpeg/Openclassrooms_Projet-7/archive/refs/heads/main.zip)

Choisissez l'endroit où vous souhaitez le dézipper. C'est dans ce dossier que le programme stockera les fichiers extraits après lancement.

## Environnement virtuel
Principalement pour des raisons de compatibilité de versions et ainsi éviter tout bug du à des conflits de versions des librairies/packages utilisés, il est fortement conseillé de travailler au sein d'un environnement virtuel.

Commencez par utiliser votre terminal pour vous placer dans le dossier que vous avez choisi pour dézipper.

#### Créer l'environnement virtuel
saisir la commande  suivante :
```
python -m venv env
```

#### Lancer l'environnement virtuel :
* saisir la commande  suivante  **sous Windows** (cmd) :
```
env\Scripts\activate.bat
```

* saisir la commande  suivante  **sous Windows** (PowerShell) :

```
env\Scripts\activate.ps1
```

* saisir la commande  suivante **sous Linux / Mac** :

```
source env/bin/activate
```

#### Installation des librairies/packages nécessaires :
```
pip install -r requirements.txt
```
Vous pouvez contrôler lesquels se sont installés avec la commande suivante : 
```
pip freeze
```


### Lancement des programmes
Saisir la commande suivante :
```
python3 main.py
```
