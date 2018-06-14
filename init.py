import requests
from bs4 import BeautifulSoup
import mysql.connector

url = "https://pokemondb.net/pokedex/all"

# response = requests.get(url)
# html = str(response.content)

file = open("pokemon_catalog.html", "r")
html = file.read()
file.close()

soup = BeautifulSoup(html, "html.parser")

"""CREATION ET CONNEXION DE LA BDD"""

db = mysql.connector.connect(host="localhost", user="root", password="", database="pokebase")
cursor = db.cursor()

# cursor.execute("CREATE DATABASE IF NOT EXISTS pokebase")
# Selection de la base de donnee
# cursor.execute("USE pokebase")
# cursor.execute(
# "CREATE TABLE IF NOT EXISTS pokemon(id INT PRIMARY KEY NOT NULL, nom VARCHAR(100), type_id INT(11) NOT NULL, total INT(11) NOT NULL, hp INT(11) NOT NULL, attack INT(11) NOT NULL, defense INT(11) NOT NULL, sp_atk INT(11) NOT NULL, spd_def INT(11) NOT NULL, speed INT(11) NOT NULL);"
# "CREATE TABLE IF NOT EXISTS type(id INT, skill VARCHAR(100);"
# )

"""INSERTION DES DONNEES DANS LA BDD"""

cursor.execute('USE pokebase')
cursor.execute('SET FOREIGN_KEY_CHECKS = 0;')
cursor.execute('TRUNCATE pokemon')
cursor.execute('TRUNCATE type')
cursor.execute('SET FOREIGN_KEY_CHECKS = 1')

"""FONCTIONS POUR EXTRAIRE LES DONNEES"""

# Recupere et insere tous les pokemons
def pokemon():

    tab = soup.find(id="pokedex")

    for link in tab.find_all("tr"):
        namelist = []
        for l in link.find_all("td"):
            namelist.append(l.text)
        if(namelist):
            #print(namelist)
            cursor.execute("""INSERT INTO pokemon(ref_pokemon, nom, type, total, hp, attack, defense, sp_atk, sp_def, speed) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""", namelist)


# Recupere et insere tous les types
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

"""ACTIONS DE TESTS"""

pokemon()
grabType()




db.commit()
cursor.close()
db.close()

