# filename: api.py
"""A basic (single function) API written using hug"""

import hug
import mysql.connector


@hug.get('/pokemon')
def pokemonDisplayAll():
    """Affiche tous les pokemons """
    db = mysql.connector.connect(host="localhost", user="root", password="", database="pokebase")
    cursor = db.cursor()
    cursor.execute("""SELECT * FROM pokemon""")
    f = cursor.fetchall()
    cursor.close()
    db.close()
    return f


@hug.post('/pokemon/add')
def pokemonAdd(ref_pokemon, nom, type_pok, total, hp, attack, defense, sp_atk, sp_def, speed):
    """ Ajoute un pokemon """
    db = mysql.connector.connect(host="localhost", user="root", password="", database="pokebase")
    cursor = db.cursor()
    req = (ref_pokemon, nom, type_pok, total, hp, attack, defense, sp_atk, sp_def, speed)
    f = cursor.execute("""INSERT INTO pokemon (ref_pokemon, nom, type, total, hp, attack, defense, sp_atk, sp_def, speed) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""", req)
    db.commit()
    cursor.close()
    db.close()
    return f


@hug.put('/pokemon/update')
def pokemonUpdate(pokname, ref_pokemon, nom, type_pok, total, hp, attack, defense, sp_atk, sp_def, speed):
    """ Modifie un pokemon """
    db = mysql.connector.connect(host="localhost", user="root", password="", database="pokebase")
    cursor = db.cursor()
    req = (ref_pokemon, nom, type_pok, total, hp, attack, defense, sp_atk, sp_def, speed, pokname)
    f = cursor.execute("""UPDATE pokemon SET ref_pokemon=%s, nom=%s, type=%s, total=%s, hp=%s, attack=%s, defense=%s, sp_atk=%s, sp_def=%s, speed=%s WHERE nom =%s""", req)
    db.commit()
    cursor.close()
    db.close()
    return f


@hug.delete('/pokemon/delete')
def pokemonDel(namepok):
    """ Supprime un pokemon """
    db = mysql.connector.connect(host="localhost", user="root", password="", database="pokebase")
    cursor = db.cursor()
    cursor.execute("""DELETE FROM pokemon WHERE nom =(?)""", namepok)
    db.commit()
    cursor.close()
    db.close()
