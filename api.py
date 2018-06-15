# filename: api.py
"""API Pokemons"""

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
def pokemonAdd(ref_pokemon, nom, type_pok, hp, attack, defense, sp_atk, sp_def, speed):
    """ Ajoute un pokemon """
    db = mysql.connector.connect(host="localhost", user="root", password="", database="pokebase")
    cursor = db.cursor()

    cursor.execute("""SELECT EXISTS(SELECT * FROM pokemon WHERE nom =%s )""", (nom, ))
    test = cursor.fetchone()
    if int(test[0]) == 0:
        total = hp + attack + defense + sp_atk + sp_def + speed
        req = (ref_pokemon, nom, type_pok, total, hp, attack, defense, sp_atk, sp_def, speed)
        cursor.execute("""INSERT INTO pokemon (ref_pokemon, nom, type, total, hp, attack, defense, sp_atk, sp_def, speed) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""", req)
        db.commit()
        cursor.execute("""SELECT * FROM pokemon WHERE nom=%s""", (nom,))
        f = cursor.fetchone()
        result = 'Votre pokemon {0} a été ajouté'.format(str(f[0]))
    else:
        result = 'Votre pokemon existe deja !'
    cursor.close()
    db.close()
    return result


@hug.put('/pokemon/update')
def pokemonUpdate(pokname, ref_pokemon, nom, type_pok, hp, attack, defense, sp_atk, sp_def, speed):
    """ Modifie un pokemon """
    db = mysql.connector.connect(host="localhost", user="root", password="", database="pokebase")
    cursor = db.cursor()
    cursor.execute("""SELECT EXISTS(SELECT * FROM pokemon WHERE nom =%s )""", (nom,))
    test = cursor.fetchone()
    if int(test[0]) == 0:
        total = hp + attack + defense + sp_atk + sp_def + speed
        req = (ref_pokemon, nom, type_pok, total, hp, attack, defense, sp_atk, sp_def, speed, pokname)
        cursor.execute("""UPDATE pokemon SET ref_pokemon=%s, nom=%s, type=%s, total=%s, hp=%s, attack=%s, defense=%s, sp_atk=%s, sp_def=%s, speed=%s WHERE nom =%s""", req)
        db.commit()
        cursor.execute("""SELECT * FROM pokemon WHERE nom=%s""", (nom, ))
        f = cursor.fetchone()
        result = 'Votre pokemon {0} a été mis à jour en {1}'.format(pokname, f[2])
    else:
        result = 'Votre pokemon existe deja !'
    cursor.close()
    db.close()
    return result

@hug.delete('/pokemon/delete')
def pokemonDel(namepok):
    """ Supprime un pokemon """
    db = mysql.connector.connect(host="localhost", user="root", password="", database="pokebase")
    cursor = db.cursor()
    cursor.execute("""SELECT EXISTS(SELECT * FROM pokemon WHERE nom =%s )""", (namepok,))
    test = cursor.fetchone()
    if int(test[0]) == 0:
        result = 'Le pokemon que vous essayez de supprimer n existe pas !'
    else:
        cursor.execute("""DELETE FROM pokemon WHERE nom =%s""", (namepok, ))
        db.commit()
        result = 'Votre pokemon a bien été supprimé !'
    cursor.close()
    db.close()
    return result
