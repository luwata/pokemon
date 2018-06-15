# Pokemon

Pokemon est un catalogue exhaustif qui recense presque tous les pokemons existant

### Pre-requis 

Il est nécessaire pour faire fonctionner l'API d'installer python3 et les libraries suivantes :
	-mysql-connector
	-hug
	-bs4 de beautifulsoup

#### Sur Linux

Il faut installer mysql pour que la base de donnée fonctionne

```
sudo apt-get install mysql-server
```

Exécutez les commandes décrites ci-dessous dans un terminal
```
sudo apt-get install python3
sudo apt-get install -y python3-pip
sudo apt-get install python3-bs4
pip3 install mysql-connector
pip3 install hug --upgrade
```
#### Sur Windows

##### Installer MySQL
Pour télécharger MySQL, vous pouvez vous rendre sur le site suivant :

http://dev.mysql.com/downloads/mysql/#downloads

Sélectionnez l'OS sur lequel vous travaillez (Windows).

Téléchargez MySQL avec l'installeur (MSI Installer), puis exécutez le fichier téléchargé. L'installeur démarre et vous guide lors de l'installation.

##### Installer un terminal pour éxécuter des commandes linux

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

## Comment utiliser l'API

Pour visualiser tous les pokemons, il faut se rendre sur le lien suivant :
**Attention : Vérifier que le __serveur python__ est bien lancé**


```
http://localhost:8000/pokemon
```

Pour les autres fonctionnalités de l'API, il faut utiliser l'outil __Postman__.
On peut le télécharger sur le lien suivant : https://www.getpostman.com/apps

Les fonctionnalités sont listées dans le dossier __swagger.yaml__.
Pour consulter la documentation, ouvrir le fichier __index.html__

-----------------
## Auteur

* **Yacine Souadda** - [Luwata](https://github.com/luwata)