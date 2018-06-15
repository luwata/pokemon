import requests
from bs4 import BeautifulSoup
import mysql.connector

"""ENREGISTREMENT DU CATALOGUE HTML DANS UN FICHIER LOCAL"""
url = "https://pokemondb.net/pokedex/all"

# response = requests.get(url)
# html = str(response.content)

file = open("pokemon_catalog.html", "r")
html = file.read()
file.close()

"""CREATION ET CONNEXION DE LA BDD"""
db = mysql.connector.connect(host="localhost", user="root", password="", database="pokebase")
cursor = db.cursor()

"""VIDE LES TABLES DE LA BDD SI ELLES EXISTENT"""
cursor.execute('USE pokebase')
cursor.execute('SET FOREIGN_KEY_CHECKS = 0;')
cursor.execute('TRUNCATE pokemon')
cursor.execute('TRUNCATE type')
cursor.execute('SET FOREIGN_KEY_CHECKS = 1')


"""FONCTIONS POUR PARSER ET INSERER LES DONNEES"""
soup = BeautifulSoup(html, "html.parser")

# Recupere et insere tous les pokemons dans la table pokemon
def pokemon():

    tab = soup.find(id="pokedex")

    for link in tab.find_all("tr"):
        namelist = []
        for l in link.find_all("td"):
            namelist.append(l.text)
        if(namelist):
            cursor.execute("""INSERT INTO pokemon(ref_pokemon, nom, type, total, hp, attack, defense, sp_atk, sp_def, speed) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""", namelist)


# Recupere et insere tous les types dans la table type
def grabType():
   tab = soup.find(id="filter-pkmn-type")

   skill = []
   for type in tab.find_all("option"):
       t = []
       if type.text != "- All -":
            t.append(type.text)
       skill.append(t)
   del skill[0]
   return(skill)

type = grabType()

for i in range(0, len(type)):
    id = i
    skill = type[i][0]

    req = (id, skill)
    cursor.execute("""INSERT INTO type (id, skill) VALUES (%s,%s)""", req)


"""INSERTION DES DONNEES DANS LA BDD"""
pokemon()
grabType()

db.commit()
cursor.close()
db.close()

