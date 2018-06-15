# Pokemon

Pokemon est un catalogue qui recense tous les pokemons existant

## Pour commencer

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Pre-requis 

Il est nécessaire pour faire fonctionner l'API d'installer python3 et les libraries suivantes :
	+mysql-connector
	+hug
	+bs4 de beautifulsoup

#### Sur Linux

Exécutez les commandes décrites ci-dessous dans un terminal
```
sudo apt-get install python3
sudo apt-get install -y python3-pip
sudo apt-get install python3-bs4
pip3 install mysql-connector
pip3 install hug --upgrade
```
#### Sur Windows

Utilisez une console comme Cmder pour pouvoir éxecuter les même commandes ci-dessus : http://cmder.net/

### Installation

Pour utiliser l'API, il est nécessaire d'importer la base de données SQL avec le fichier __pokebase.sql__

Pour renseigner notre base de données avec le catalogue de pokemons, il faut éxécuter le fichier **init.py** dans votre console

```
python init.py
```
Ensuite, on va éxécuter notre serveur python en même temps que l'API.

```
hug -f api.py
```

## Comment Utiliser l'API

Pour visualiser tous les pokemons, il faut qe rendre sur le lien suivant :
(Attention : Vérifier que le __serveur python__ est bien lancé)

```
http://localhost:8000/pokemon
```

Pour les autres fonctionnalités de l'API, il faut utiliser l'outil Postman.
On peut le télécharger sur le lien suivant : https://www.getpostman.com/apps

Les fonctionnalités sont listées dans le dossier __documentation API__.
Pour consulter la documentation, ouvrir le fichier __index.html__

## Auteur

* **Yacine Souadda** - [Luwata](https://github.com/luwata)