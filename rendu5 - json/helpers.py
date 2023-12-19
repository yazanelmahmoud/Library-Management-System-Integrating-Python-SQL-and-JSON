from datetime import datetime, timedelta
import json
import os
import psycopg2
from psycopg2 import sql
from constants import ADMIN_PASSWORD

def get_user_input(prompt, data_type):
    while True:
        try:
            user_input = data_type(input(prompt))
            return user_input
        except ValueError:
            print("Erreur de saisie. Veuillez entrer une valeur valide.")

def insert_into_pret(connection, values):
    try:
        cursor = connection.cursor()
        insert_query = sql.SQL("INSERT INTO Pret (id_exemplaire, id_adherent, id_responsable, datePret, duree) VALUES ({}, {}, {}, {}, {})").format(
            sql.Literal(values['id_exemplaire']),
            sql.Literal(values['id_adherent']),
            sql.Literal(values['id_responsable']),
            sql.Literal(values['datePret']),
            sql.Literal(values['duree']),
        )
        cursor.execute(insert_query)
        connection.commit()
        print("Insertion réussie dans la table Pret")
    except (Exception, psycopg2.Error) as error:
        print("Erreur lors de l'insertion dans la table Pret:", error)
    finally:
        if cursor:
            cursor.close()

def execute_query(conn, query):
    # Open a cursor to perform database operations
    cur = conn.cursor()
    # Execute a command: create datacamp_courses table
    cur.execute(query)  
    # Get results if results exist
    try:
        rows = cur.fetchall()
        return rows
    except:
        pass
    # Make the changes to the database persistent
    conn.commit()
    # Close cursor and communication with the database
    cur.close()

def get_prets_en_cours_from_login(conn, login):
    query = f"""
            SELECT prets FROM AdherentDetails
            WHERE login LIKE '{login}%' AND prets->'dateRetour' IS NULL
    """
    results = execute_query(conn, query)
    if len(results) >0:
        return results[0][0]
    return None

def get_film_exemplaires(conn, titre):
    query = f"""
            SELECT * FROM FilmExemplaires
            WHERE titre_film LIKE '{titre}%'
    """
    results = execute_query(conn, query)
    return results

def get_ressource_data(conn,id, type):
    query = f"""
            SELECT * FROM {type}
            WHERE id = {id}
    """
    results = execute_query(conn, query)
    return results[0]

def get_user_data(conn,login):
    query = f"""
            SELECT * FROM Utilisateur
            WHERE login LIKE '{login}%'
    """
    results = execute_query(conn, query)
    return results[0]

def get_film_exemplaires_disponibles(conn, titre):
    query = f"""
            SELECT id_film, titre_film, synopsis, langue , COUNT(id_film) FROM FilmExemplaires
            WHERE titre_film LIKE '{titre}%' AND disponible = 'true' AND etat != 'Perdu'
            GROUP BY id_film, titre_film, synopsis, langue
            HAVING COUNT(id_film) >0
    """
    results = execute_query(conn, query)
    return results

def get_film_ressources(conn, titre):
    query = f"""
            SELECT * FROM Film
            WHERE titre LIKE '{titre}%'
    """
    results = execute_query(conn, query)
    return results

def get_musique_exemplaires(conn, titre):
    query = f"""
            SELECT * FROM MusiqueExemplaires
            WHERE titre_musique LIKE '{titre}%'
    """
    results = execute_query(conn, query)
    return results

def get_musique_exemplaires_disponibles(conn, titre):
    query = f"""
            SELECT id_musique, titre_musique, editeur, longueur , COUNT(id_musique) FROM musiqueExemplaires
            WHERE titre_musique LIKE '{titre}%' AND disponible = 'true' AND etat != 'Perdu'
            GROUP BY id_musique, titre_musique, editeur, longueur
            HAVING COUNT(id_musique) >0
    """
    results = execute_query(conn, query)
    return results

def get_musique_ressources(conn, titre):
    query = f"""
            SELECT * FROM Musique
            WHERE titre LIKE '{titre}%'
    """
    results = execute_query(conn, query)
    return results

def get_livre_exemplaires(conn, titre):
    query = f"""
            SELECT * FROM LivreExemplaires
            WHERE titre_livre LIKE '{titre}%'
    """
    results = execute_query(conn, query)
    return results

def get_livre_exemplaires_disponibles(conn, titre):
    query = f"""
            SELECT id_livre, titre_livre, editeur, langue , COUNT(id_livre) FROM livreExemplaires
            WHERE titre_livre LIKE '{titre}%' AND disponible = 'true' AND etat != 'Perdu'
            GROUP BY id_livre, titre_livre, editeur, langue
            HAVING COUNT(id_livre) >0
    """
    results = execute_query(conn, query)
    return results

def get_livre_ressources(conn,titre):
    query = f"""
            SELECT * FROM Livre
            WHERE titre LIKE '{titre}%'
    """
    results = execute_query(conn, query)
    return results

def get_adherent_details(conn, login):
    query = f"""
            SELECT * FROM AdherentDetails
            WHERE login LIKE '{login}%'
    """
    results = execute_query(conn, query)
    return results   

def get_personnel_details(conn, login):
    query = f"""
            SELECT * FROM PersonnelDetails
            WHERE login LIKE '{login}%'
    """
    results = execute_query(conn, query)
    return results

def is_personnel(conn, login):
    if (len(get_personnel_details(conn, login))>0):
        return True 
    return False

def get_auteurs_livre(conn, id_livre):
    query = f"""
            SELECT contributeur->'auteur' FROM Livre
            WHERE id = {id_livre}
    """
    results = execute_query(conn, query)
    if len(results) >0:
        author_list_json = results[0][0]
        return author_list_json
    return None

def get_interpretes_musique(conn, id_musique):
    query = f"""
            SELECT contributeur->'interprete' FROM Musique
            WHERE id = {id_musique}
    """
    results = execute_query(conn, query)
    if len(results) >0:
        interprete_list_json = results[0][0]
        return interprete_list_json
    return results

def get_compositeurs_musique(conn, id_musique):
    query = f"""
            SELECT contributeur->'compositeur' FROM Musique
            WHERE id = {id_musique}
    """
    results = execute_query(conn, query)
    if len(results) >0:
        compositor_list_json = results[0][0]
        return compositor_list_json
    return results

def get_acteurs_film(conn, id_film):
    query = f"""
            SELECT contributeur->'acteur' FROM Film
            WHERE id = {id_film}
    """
    results = execute_query(conn, query)
    if len(results) >0:
        actor_list_json = results[0][0]
        return actor_list_json
    return results

def get_realisateurs_film(conn, id_film):
    query = f"""
            SELECT contributeur->'realisateur' FROM Film
            WHERE id = {id_film}
    """
    results = execute_query(conn, query)
    if len(results) >0:
        director_list_json = results[0][0]
        return director_list_json
    return results

def insert_exemplaire(conn, ressource, type):
    os.system('cls')
    etat = input("Etat de l'exemplaire 'Neuf', 'Bon', 'Abime', 'Perdu' : ")
    exemplaires = ressource[9]
    if type == "Livre":
        exemplaires = ressource[9]
    if type == "Film":
        exemplaires = ressource[11]
    exemplaires.append({"id": len(exemplaires)+1, "etat": etat})
    query = f"""
        UPDATE {type}
        SET exemplaires = '{json.dumps(exemplaires)}'
        WHERE id = {ressource[0]};
        """
    execute_query(conn,query)
    display_exemplaires(conn, ressource, type)

def delete_exemplaire(conn, ressource, type):
    id = input("Index de l'exemplaire : ")
    delete_exemplaire_from_id(conn, ressource, type, id)
    display_exemplaires(conn, ressource, type)

def delete_exemplaire_from_id(conn, ressource, type, id):
    exemplaires = ressource[9]
    if type == "Livre":
        exemplaires = ressource[9]
    if type == "Film":
        exemplaires = ressource[11]
    exemplaires.pop(int(id)-1)
    query = f"""
        UPDATE {type}
        SET exemplaires = '{json.dumps(exemplaires)}'
        WHERE id = {ressource[0]};
        """
    execute_query(conn,query)


def update_exemplaire(conn, ressource, type):
    id = input("Index de l'exemplaire : ")
    etat = input("Etat de l'exemplaire 'Neuf', 'Bon', 'Abime', 'Perdu' : ")
    exemplaires = ressource[9]
    if type == "Livre":
        exemplaires = ressource[9]
    if type == "Film":
        exemplaires = ressource[11]
    exemplaires[int(id)-1] = {"id": exemplaires[int(id)-1]["id"], "etat": etat}
    query = f"""
        UPDATE {type}
        SET exemplaires = '{json.dumps(exemplaires)}'
        WHERE id = {ressource[0]};
        """
    execute_query(conn,query)
    display_exemplaires(conn, ressource, type)

def display_exemplaires(conn, ressource, type):
    os.system('cls')
    query = f"""
            SELECT exemplaires FROM {type}
            WHERE id = {ressource[0]}
    """
    exemplaires = execute_query(conn, query)[0][0]
    if len(exemplaires)>0:
        print("\nExemplaires :")
        for exemplaire in exemplaires:
            print("{:<10} {:<15}".format(exemplaire["id"], exemplaire["etat"]))
    print("\n1. Ajouter Exemplaire")
    print("2. Modifier Exemplaire")
    print("3. Supprimer Exemplaire")
    print("4. Retour")
    choice = int(input("Que voulez_vous faire ? : "))
    if choice == 1:
        insert_exemplaire(conn, ressource, type)
    elif choice == 2:
        update_exemplaire(conn, ressource, type)
    elif choice == 3:
        delete_exemplaire(conn, ressource, type)
    globals()[f'display_{type.lower()}'](conn, ressource)

def display_exemplaires_adherent(conn, ressource, type):
    os.system('cls')
    query = f"""
            SELECT exemplaires FROM {type}
            WHERE id = {ressource[0]}
    """
    exemplaires = execute_query(conn, query)[0][0]
    if len(exemplaires)>0:
        print("\nExemplaires :")
        for exemplaire in exemplaires:
            print("{:<10} {:<15}".format(exemplaire["id"], exemplaire["etat"]))
    print("1. Retour")
    choice = int(input("Que voulez_vous faire ? : "))
    globals()[f'display_{type}_adherent'](conn, ressource)
 
def display_exemplaires_prêt(conn, ressource, values):
    os.system('cls')
    query = f"""
            SELECT * FROM Exemplaire
            WHERE id_ressource = {ressource[0]} AND disponible = 'true' AND etat != 'Perdu'
    """
    exemplaires = execute_query(conn, query)
    if len(exemplaires)>0:
        print("\nExemplaires :")
        for index, exemplaire in enumerate(exemplaires):
            print("{:<10} {:<15} {:<15}".format(index+1, exemplaire[2], "disponible" if exemplaire[3] == 1 else "non disponible"))
    choice = int(input("\nQuel exemplaire choisissez vous (-1 pour annuler) : "))
    if choice in range(-1, len(exemplaires)+1):
        if choice != -1:
            values["id_exemplaire"] = exemplaires[choice-1][0]
            values['datePret'] = input("Entrez la date de prêt (format YYYY-MM-DD) : ")
            values['duree'] = get_user_input("Entrez la durée du prêt (en jours) : ", int)
            insert_into_pret(conn, values)
            emprunt_exemplaire(conn,values["id_exemplaire"])

def emprunt_exemplaire(conn,id_exemplaire):
    query = f"""
        UPDATE Exemplaire
        SET disponible = 'false'
        WHERE id = '{id_exemplaire}';
    """
    _ = execute_query(conn, query)

def delete_ressource(conn, id_ressource, type):
    query = f"""
            DELETE FROM {type} WHERE id = {id_ressource};
    """
    _ = execute_query(conn, query)

def display_livre(conn,livre):
    os.system('cls')
    print(f"Titre: {livre[1]}")
    print(f"Date apparition: {livre[2]}")
    print(f"Editeur: {livre[3]}")
    print(f"Genre: {livre[4]}")
    print(f"Code de classification: {livre[5]}")
    print(f"ISBN: {livre[7]}")
    print(f"Résumé: {livre[8]}")
    print(f"Langue: {livre[9]}")
    auteurs = get_auteurs_livre(conn,livre[0])
    if len(auteurs)>0:
        print("\nAuteurs :")
        for auteur in auteurs:
            print("{:<10} {:<15} {:<15} {:<15}".format(auteur["prenom"], auteur["nom"], auteur["dateNaissance"], auteur["nationalite"]))
    print("\n")
    print("1. Modifier la ressource")
    print("2. Supprimer la ressource")
    print("3. Consulter les exemplaires")
    print("4. Retour")
    choice = int(input("Que voulez_vous faire ? : "))
    if choice ==2: 
        delete_ressource(conn, livre[0], "Livre")
    elif choice ==1: 
        update_livre(conn, livre)
    elif choice ==3: 
        display_exemplaires(conn, livre,"Livre")

def display_musique(conn,musique):
    os.system('cls')
    print(f"Titre: {musique[1]}")
    print(f"Date apparition: {musique[2]}")
    print(f"Editeur: {musique[3]}")
    print(f"Genre: {musique[4]}")
    print(f"Code de classification: {musique[5]}")
    print(f"Durée: {musique[6]}")
    interpretes = get_interpretes_musique(conn,musique[0])
    if len(interpretes)>0:
        print("\nInterpretes :")
        for interprete in interpretes:
            print("{:<10} {:<15} {} {:<15}".format(interprete["prenom"], interprete["nom"], interprete["dateNaissance"], interprete["nationalite"]))
    compositeurs = get_compositeurs_musique(conn,musique[0])
    if len(compositeurs)>0:
        print("Compositeurs :")
        for compositeur in compositeurs:
            print("{:<10} {:<15} {} {:<15}".format(compositeur["prenom"], compositeur["nom"], compositeur["dateNaissance"], compositeur["nationalite"]))
    print("\n")
    print("1. Modifier la ressource")
    print("2. Supprimer la ressource")
    print("3. Consulter les exemplaires")
    print("4. Retour")
    choice = int(input("Que voulez_vous faire ? : "))
    if choice ==2: 
        delete_ressource(conn, musique[0], "Musique")
    elif choice ==1: 
        update_musique(conn, musique)
    elif choice ==3: 
        display_exemplaires(conn, musique, "Musique")

def display_film(conn,film):
    os.system('cls')
    print(f"Titre: {film[1]}")
    print(f"Date apparition: {film[2]}")
    print(f"Editeur: {film[3]}")
    print(f"Genre: {film[4]}")
    print(f"Synopsis: {film[5]}")
    print(f"Code de classification: {film[6]}")
    print(f"Durée: {film[8]}")
    print(f"Langue: {film[7]}")
    acteurs = get_acteurs_film(conn,film[0])
    if len(acteurs)>0:
        print("\nActeurs :")
        for acteur in acteurs:
            print("{:<10} {:<15} {} {:<15}".format(acteur["prenom"], acteur["nom"], acteur["dateNaissance"], acteur["nationalite"]))
    realisateurs = get_realisateurs_film(conn,film[0])
    if len(realisateurs)>0:
        print("Realisateurs :")
        for realisateur in realisateurs:
            print("{:<10} {:<15} {} {:<15}".format(realisateur["prenom"], realisateur["nom"], realisateur["dateNaissance"], realisateur["nationalite"]))
    print("\n")
    print("1. Modifier la ressource")
    print("2. Supprimer la ressource")
    print("3. Consulter les exemplaires")
    print("4. Retour")
    choice = int(input("Que voulez_vous faire ? : "))
    if choice ==2: 
        delete_ressource(conn, film[0], "Musique")
    elif choice ==1: 
        update_film(conn, film)
    elif choice ==3: 
        display_exemplaires(conn, film, "Film")

def display_livre_adherent(conn,livre):
    os.system('cls')
    print(f"Titre: {livre[1]}")
    print(f"Date apparition: {livre[2]}")
    print(f"Editeur: {livre[3]}")
    print(f"Genre: {livre[4]}")
    print(f"Code de classification: {livre[5]}")
    print(f"ISBN: {livre[7]}")
    print(f"Résumé: {livre[8]}")
    print(f"Langue: {livre[9]}")
    auteurs = get_auteurs_livre(conn,livre[0])
    if len(auteurs)>0:
        print("\nAuteurs :")
        for auteur in auteurs:
            print("{:<10} {:<15} {:<15} {:<15}".format(auteur["prenom"], auteur["nom"], auteur["dateNaissance"], auteur["nationalite"]))
    print("\n")
    print("1. Consulter les exemplaires")
    print("2. Retour")
    choice = int(input("Que voulez_vous faire ? : "))
    if choice ==1: 
        display_exemplaires_adherent(conn, livre,"Livre")

def display_musique_adherent(conn,musique):
    os.system('cls')
    print(f"Titre: {musique[1]}")
    print(f"Date apparition: {musique[2]}")
    print(f"Editeur: {musique[3]}")
    print(f"Genre: {musique[4]}")
    print(f"Code de classification: {musique[5]}")
    print(f"Durée: {musique[6]}")
    interpretes = get_interpretes_musique(conn,musique[0])
    if len(interpretes)>0:
        print("\nInterpretes :")
        for interprete in interpretes:
            print("{:<10} {:<15} {} {:<15}".format(interprete["prenom"], interprete["nom"], interprete["dateNaissance"], interprete["nationalite"]))
    compositeurs = get_compositeurs_musique(conn,musique[0])
    if len(compositeurs)>0:
        print("Compositeurs :")
        for compositeur in compositeurs:
            print("{:<10} {:<15} {} {:<15}".format(compositeur["prenom"], compositeur["nom"], compositeur["dateNaissance"], compositeur["nationalite"]))
    print("\n")
    print("1. Consulter les exemplaires")
    print("2. Retour")
    choice = int(input("Que voulez_vous faire ? : "))
    if choice ==1: 
        display_exemplaires_adherent(conn, musique, "Musique")

def display_film_adherent(conn,film):
    os.system('cls')
    print(f"Titre: {film[1]}")
    print(f"Date apparition: {film[2]}")
    print(f"Editeur: {film[3]}")
    print(f"Genre: {film[4]}")
    print(f"Synopsis: {film[5]}")
    print(f"Code de classification: {film[6]}")
    print(f"Durée: {film[8]}")
    print(f"Langue: {film[7]}")
    acteurs = get_acteurs_film(conn,film[0])
    if len(acteurs)>0:
        print("\nActeurs :")
        for acteur in acteurs:
            print("{:<10} {:<15} {} {:<15}".format(acteur["prenom"], acteur["nom"], acteur["dateNaissance"], acteur["nationalite"]))
    realisateurs = get_realisateurs_film(conn,film[0])
    if len(realisateurs)>0:
        print("Realisateurs :")
        for realisateur in realisateurs:
            print("{:<10} {:<15} {} {:<15}".format(realisateur["prenom"], realisateur["nom"], realisateur["dateNaissance"], realisateur["nationalite"]))
    print("\n")
    print("1. Consulter les exemplaires")
    print("2. Retour")
    choice = int(input("Que voulez_vous faire ? : "))
    if choice ==1: 
        display_exemplaires_adherent(conn, film, "Film")

def update_livre(conn, livre):
    os.system('cls')
    titre= input("Titre: ")
    date= input("Date apparition: ")
    editeur= input("Editeur: ")
    genre = input("Genre: ")
    resume= input("Résumé: ")
    code= input("Code de classification: ")
    isbn= input("ISBN: ")
    langue = input("Langue: ")
    try:
        query1 = f"""
        UPDATE Livre
        SET titre = '{titre}', dateApparition = '{date}', editeur = '{editeur}', genre = '{genre}', codeClassification = '{code}', resume = '{resume}', ISBN = '{isbn}', langue = '{langue}'
        WHERE id = '{livre[0]}';
        """
        execute_query(conn,query1)
    except:
        print("\n")
    os.system('cls')
    auteurs = get_auteurs_livre(conn,livre[0])
    if len(auteurs)>0:
        print("\nAuteurs :")
        for index, auteur in enumerate(auteurs):
            print("{:<10} {:<10} {:<15} {} {:<15}".format(index+1,auteur["prenom"], auteur["nom"], auteur["dateNaissance"], auteur["nationalite"]))
        print("\n1. Ajouter Auteur")
        print("2. Supprimer Auteur")
        print("3. Finir")
        while True:
            choice = int(input("Que voulez_vous faire ? : "))
            if choice == 1:
                insert_auteur(conn, livre)
            elif choice == 2:
                delete_auteur(conn, livre)
            else:
                break

def delete_auteur(conn, livre):
    id = input("Index de l'auteur : ")
    contributeurs = livre[10]
    contributeurs["auteur"].pop(int(id)-1)
    query = f"""
        UPDATE Livre
        SET contributeur = '{json.dumps(contributeurs)}'
        WHERE id = {livre[0]};
        """
    execute_query(conn,query)

def insert_auteur(conn, livre):
    nom = input("Nom de l'auteur: ")
    prenom = input("Prenom de l'auteur: ")
    date_naissance = input("Date de naissance: ")
    nationalite = input("Nationalité: ")
    contributeurs = livre[10]
    contributeurs["auteur"].append({"nom": nom, "prenom": prenom, "dateNaissance": date_naissance, "nationalite": nationalite})
    query = f"""
        UPDATE Livre
        SET contributeur = '{json.dumps(contributeurs)}'
        WHERE id = {livre[0]};
        """
    execute_query(conn,query)

def update_musique(conn, musique):
    os.system('cls')
    titre= input("Titre: ")
    date= input("Date apparition: ")
    editeur= input("Editeur: ")
    genre = input("Genre: ")
    longueur= input("Longueur: ")
    code= input("Code de classification: ")
    try:
        query1 = f"""
        UPDATE Musique
        SET titre = '{titre}', dateApparition = '{date}', editeur = '{editeur}', genre = '{genre}', codeClassification = '{code}', longueur = '{longueur}'
        WHERE id = '{musique[0]}';
        """
        execute_query(conn,query1)
    except:
        print("\n")
    os.system('cls')
    interpretes = get_interpretes_musique(conn,musique[0])
    if len(interpretes)>0:
        print("\nInterpretes :")
        for interprete in interpretes:
            print("{:<10} {:<15} {} {:<15}".format(interprete["prenom"], interprete["nom"], interprete["dateNaissance"], interprete["nationalite"]))
        print("\n1. Ajouter Interprete")
        print("2. Supprimer Interprete")
        print("3. Continuer")
        while True:
            choice = int(input("Que voulez_vous faire ? : "))
            if choice == 1:
                insert_interprete(conn, musique)
            elif choice == 2:
                delete_interprete(conn, musique)
            else:
                break
    os.system('cls')
    compositeurs = get_compositeurs_musique(conn,musique[0])
    if len(compositeurs)>0:
        print("\nCompositeurs :")
        for compositeur in compositeurs:
            print("{:<10} {:<15} {} {:<15}".format(compositeur["prenom"], compositeur["nom"], compositeur["dateNaissance"], compositeur["nationalite"]))
        print("\n1. Ajouter Compositeur")
        print("2. Supprimer Compositeur")
        print("3. Finir")
        while True:
            choice = int(input("Que voulez_vous faire ? : "))
            if choice == 1:
                insert_compositeur(conn, musique)
            elif choice == 2:
                delete_compositeur(conn, musique)
            else:
                break

def delete_compositeur(conn, musique):
    id = input("Index du compositeur : ")
    contributeurs = musique[8]
    contributeurs["compositeur"].pop(int(id)-1)
    query = f"""
        UPDATE Musique
        SET contributeur = '{json.dumps(contributeurs)}'
        WHERE id = {musique[0]};
        """
    execute_query(conn,query)

def insert_compositeur(conn, musique):
    nom = input("Nom du compositeur: ")
    prenom = input("Prenom du compositeur: ")
    date_naissance = input("Date de naissance: ")
    nationalite = input("Nationalité: ")
    contributeurs = musique[8]
    contributeurs["compositeur"].append({"nom": nom, "prenom": prenom, "dateNaissance": date_naissance, "nationalite": nationalite})
    query = f"""
        UPDATE Musique
        SET contributeur = '{json.dumps(contributeurs)}'
        WHERE id = {musique[0]};
        """
    execute_query(conn,query)

def delete_interprete(conn, musique):
    id = input("Index de l'interprete : ")
    contributeurs = musique[8]
    contributeurs["interprete"].pop(int(id)-1)
    query = f"""
        UPDATE Musique
        SET contributeur = '{json.dumps(contributeurs)}'
        WHERE id = {musique[0]};
        """
    execute_query(conn,query)

def insert_interprete(conn, musique):
    nom = input("Nom de l'interprete: ")
    prenom = input("Prenom de l'interprete: ")
    date_naissance = input("Date de naissance: ")
    nationalite = input("Nationalité: ")
    contributeurs = musique[8]
    contributeurs["interprete"].append({"nom": nom, "prenom": prenom, "dateNaissance": date_naissance, "nationalite": nationalite})
    query = f"""
        UPDATE Musique
        SET contributeur = '{json.dumps(contributeurs)}'
        WHERE id = {musique[0]};
        """
    execute_query(conn,query)


def update_film(conn, film):
    os.system('cls')
    titre= input("Titre: ")
    date= input("Date apparition: ")
    editeur= input("Editeur: ")
    genre = input("Genre: ")
    length= input("Length: ")
    synopsis= input("Synopsis: ")
    langue = input("Langue: ")
    code= input("Code de classification: ")
    try:
        query1 = f"""
        UPDATE Ressource
        SET titre = '{titre}', dateApparition = '{date}', editeur = '{editeur}', genre = '{genre}', codeClassification = '{code}', length = '{length}', langue = '{langue}', synopsis='{synopsis}'
        WHERE id = '{film[0]}';
        """
        execute_query(conn,query1)
    except:
        print("\n")
    os.system('cls')
    acteurs = get_acteurs_film(conn,film[0])
    if len(acteurs)>0:
        print("\nActeurs :")
        for acteur in acteurs:
            print("{:<10} {:<15} {} {:<15}".format(acteur["prenom"], acteur["nom"], acteur["dateNaissance"], acteur["nationalite"]))
        print("\n1. Ajouter Acteur")
        print("2. Supprimer Acteur")
        print("3. Continuer")
        while True:
            choice = int(input("Que voulez_vous faire ? : "))
            if choice == 1:
                insert_acteur(conn, film)
            elif choice == 2:
                delete_acteur(conn, film)
            else:
                break
    os.system('cls')
    realisateurs = get_realisateurs_film(conn,film[0])
    if len(realisateurs)>0:
        print("\nRéalisateurs :")
        for realisateur in realisateurs:
            print("{:<10} {:<15} {} {:<15}".format(realisateur["prenom"], realisateur["nom"], realisateur["dateNaissance"], realisateur["nationalite"]))
        print("\n1. Ajouter Réalisateur")
        print("2. Supprimer Réalisateur")
        print("3. Finir")
        while True:
            choice = int(input("Que voulez_vous faire ? : "))
            if choice == 1:
                insert_realisateur(conn, film)
            elif choice == 2:
                delete_realisateur(conn, film)
            else:
                break

def delete_acteur(conn, film):
    id = input("Index de l'acteur: ")
    contributeurs = film[10]
    contributeurs["acteur"].pop(int(id)-1)
    query = f"""
        UPDATE Film
        SET contributeur = '{json.dumps(contributeurs)}'
        WHERE id = {film[0]};
        """
    execute_query(conn,query)

def insert_acteur(conn, film):
    nom = input("Nom de l'acteur: ")
    prenom = input("Prenom de l'acteur: ")
    date_naissance = input("Date de naissance: ")
    nationalite = input("Nationalité: ")
    contributeurs = film[10]
    contributeurs["acteur"].append({"nom": nom, "prenom": prenom, "dateNaissance": date_naissance, "nationalite": nationalite})
    query = f"""
        UPDATE Film
        SET contributeur = '{json.dumps(contributeurs)}'
        WHERE id = {film[0]};
        """
    execute_query(conn,query)

def delete_realisateur(conn, film):
    id = input("Index de l'realisateur: ")
    contributeurs = film[10]
    contributeurs["realisateur"].pop(int(id)-1)
    query = f"""
        UPDATE Film
        SET contributeur = '{json.dumps(contributeurs)}'
        WHERE id = {film[0]};
        """
    execute_query(conn,query)

def insert_realisateur(conn, film):
    nom = input("Nom du realisateur: ")
    prenom = input("Prenom du realisateur: ")
    date_naissance = input("Date de naissance: ")
    nationalite = input("Nationalité: ")
    contributeurs = film[10]
    contributeurs["realisateur"].append({"nom": nom, "prenom": prenom, "dateNaissance": date_naissance, "nationalite": nationalite})
    query = f"""
        UPDATE Film
        SET contributeur = '{json.dumps(contributeurs)}'
        WHERE id = {film[0]};
        """
    execute_query(conn,query)

def display_prêts(conn,prêt):
    print(f"Date prêt: {prêt[1]}")
    print(f"Durée: {prêt[2]}")
    print(f"Etat: {prêt[13]}")
    print(f"Date retour: {prêt[3]}")
    print(f"Etat retour: {prêt[4]}")
    print(f"Titre ressource: {prêt[15]}")
    print(f"Tel: {prêt[5]}")
    print(f"Login: {prêt[8]}")
    print(f"Prenom: {prêt[9]}")
    print(f"Nom: {prêt[10]}")
    print("\n")
    print("1. Enregister le rendu du prêt")
    print("2. Supprimer le prêt")
    print("3. Retour")
    choice = int(input("Que voulez_vous faire ? : "))
    if choice ==2: 
        delete_prêt(conn, prêt)
    elif choice ==1: 
        rendre_prêt(conn, prêt)

def delete_prêt(conn, pret):
    if pret[3] is None:
        query =        f"""UPDATE Exemplaire
        SET disponible = 'true'
        WHERE id = '{pret[20]}';"""
        execute_query(conn,query)
    if pret[4]:
        query =        f"""UPDATE Exemplaire
        SET etat = '{pret[4]}'
        WHERE id = '{pret[20]}';"""
        execute_query(conn,query)
    query = f"""
        DELETE FROM Pret
        WHERE id = '{pret[0]}'
        """
    execute_query(conn,query)

def insert_into_sanction(connection, values):
    try:
        cursor = connection.cursor()
        insert_query = sql.SQL("INSERT INTO Sanction (id_adherent, DateSanction, motif, montant) VALUES ({}, {}, {}, {})").format(
            sql.Literal(values['id_adherent']),
            sql.Literal(values['DateSanction']),
            sql.Literal(values['motif']),
            sql.Literal(values['montant'])
        )
        cursor.execute(insert_query)
        connection.commit()
        print("Insertion réussie dans la table Sanction")
    except (Exception, psycopg2.Error) as error:
        print("Erreur lors de l'insertion dans la table Sanction:", error)
    finally:
        if cursor:
            cursor.close()

def rendre_prêt(conn, pret):
    etat_retour = input("Etat retour (Abime, Neuf, Bon, Perdu): ")
    date_retour = datetime.strptime(input("Date retour (YYYY-MM-DD): "), '%Y-%m-%d').date()
    if etat_retour != pret[13] or pret[1] + timedelta(days=pret[2]) < date_retour:
        values ={}
        values["id_adherent"]= get_utilisateur_id_from_login(conn,pret[8])
        values["DateSanction"] = datetime.now()
        if etat_retour != pret[13]:
            values["motif"]="Deterioration"
            if etat_retour == "Perdu":
                values["motif"]="Perte"
            values["montant"]=int(input("Montant à payer pour détérioration: "))
        elif pret[1] + timedelta(days=pret[2]) < date_retour:
            values["motif"]="Retard"
            values["montant"]=int(input("Montant à payer pour retard: "))
        insert_into_sanction(conn,values)
    query =        f"""UPDATE Pret
        SET etatretour = '{etat_retour}', dateretour = '{date_retour}'
        WHERE id = '{pret[0]}';"""
    execute_query(conn,query)
    query =        f"""UPDATE Exemplaire
        SET etat = '{etat_retour}', disponible = 'true'
        WHERE id = '{pret[20]}';"""
    execute_query(conn,query)

def update_status_adherent(conn):
    login = input("Login: ")
    id = get_utilisateur_id_from_login(conn,login)
    status = input("Nouveau statut (active, exepire, suspendue, blackliste): ")
    query = f"""UPDATE Adherent
        SET statut = '{status}'
        WHERE id = '{id}';"""
    execute_query(conn,query)
def check_login_adherent_valid(conn, login):
    query = f"""
            SELECT * FROM AdherentDetails
            WHERE login = '{login}' AND statut = 'active'
    """
    results = execute_query(conn, query)
    if len(results)>0:
        return results[0][0]
    return ""

def check_login_personnel_valid(conn, login):
    query = f"""
            SELECT * FROM PersonnelDetails
            WHERE login = '{login}'
    """
    results = execute_query(conn, query)
    if len(results)>0:
        return results[0][0]
    return ""

def handle_utilisateurs(conn):
    os.system("cls")
    print("1. Gérer les Adhérents")
    print("2. Gérer le Personnel")
    print("3. Retour")
    choice = int(input("Que voulez vous faire ?: "))
    if choice == 1:
        handle_adherent(conn)
    elif choice == 2:
        handle_personnel(conn)
        
def handle_personnel(conn):
    mot_de_passe = input("Entrez le mot de passe : ")
    if mot_de_passe != ADMIN_PASSWORD:
        print("Mot de passe incorrect !")
        return
    login = input("Entrez login recherché: ")
    personnel = get_personnel_details(conn, login)
    print("\nMembres du personnel :")
    for index, membre in enumerate(personnel):
            print("{:<10} {:<10} {:<15} {:15} {:<15}".format(index+1,membre[1], membre[3], membre[4], membre[5]))
    print("\n1. Ajouter membre")
    print("2. Supprimer membre")
    print("3. Retour")
    choice = int(input("Que voulez_vous faire ? : "))
    if choice == 1:
                insert_personnel(conn)
    elif choice == 2:
                delete_personnel(conn)

def handle_adherent(conn):
    login = input("Entrez login recherché: ")
    adherent = get_adherent_details(conn, login)
    print("\nAdhérents :")
    for index, membre in enumerate(adherent):
            print("{:<10} {:<10} {:<15} {:15} {:<15} {:<15}".format(index+1,membre[1], membre[3], membre[4], membre[5], membre[12]))
    print("\n1. Ajouter membre")
    print("2. Supprimer membre")
    print("3. Modifier statut adherent")
    print("4. Retour")
    choice = int(input("Que voulez_vous faire ? : "))
    if choice == 1:
                insert_adherent(conn)
    elif choice == 2:
                delete_adherent(conn)
    elif choice == 3:
        update_status_adherent(conn)

def insert_into_adresse(connection, values):
    try:
        cursor = connection.cursor()
        insert_query = sql.SQL("INSERT INTO Adresse (rue, numero, codePostal, ville) VALUES ({}, {}, {}, {})").format(
            sql.Literal(values['rue']),
            sql.Literal(values['numero']),
            sql.Literal(values['codePostal']),
            sql.Literal(values['ville'])
        )
        cursor.execute(insert_query)
        connection.commit()
        print("Insertion réussie dans la table Adresse")
    except (Exception, psycopg2.Error) as error:
        print("Erreur lors de l'insertion dans la table Adresse:", error)
    finally:
        if cursor:
            cursor.close()

def insert_into_utilisateur(connection, values):
    try:
        cursor = connection.cursor()
        insert_query = sql.SQL("INSERT INTO Utilisateur (login, password, prenom, nom, email, adresse) VALUES ( {}, {}, {}, {}, {}, {})").format(
            sql.Literal(values['login']),
            sql.Literal(values['password']),
            sql.Literal(values['prenom']),
            sql.Literal(values['nom']),
            sql.Literal(values['email']),
            sql.Literal(values['id_adresse'])
        )
        cursor.execute(insert_query)
        connection.commit()
        print("Insertion réussie dans la table Utilisateur")
    except (Exception, psycopg2.Error) as error:
        print("Erreur lors de l'insertion dans la table Utilisateur:", error)
    finally:
        if cursor:
            cursor.close()

def insert_into_personnel(connection, values):
    try:
        cursor = connection.cursor()
        insert_query = sql.SQL("INSERT INTO Personnel (id) VALUES ({})").format(
            sql.Literal(values['id_utilisateur'])
        )
        cursor.execute(insert_query)
        connection.commit()
        print("Insertion réussie dans la table Personnel")
    except (Exception, psycopg2.Error) as error:
        print("Erreur lors de l'insertion dans la table Personnel:", error)
    finally:
        if cursor:
            cursor.close()

# Exemple d'insertion dans la table Adherent
def insert_into_adherent(connection, values):
    try:
        cursor = connection.cursor()
        insert_query = sql.SQL("INSERT INTO Adherent (id, numeroTelephone, dateNaissance, statut) VALUES ({}, {}, {}, {})").format(
            sql.Literal(values['id_utilisateur']),
            sql.Literal(values['numeroTelephone']),
            sql.Literal(values['dateNaissance']),
            sql.Literal(values['statut'])
        )
        cursor.execute(insert_query)
        connection.commit()
        print("Insertion réussie dans la table Adherent")
    except (Exception, psycopg2.Error) as error:
        print("Erreur lors de l'insertion dans la table Adherent:", error)
    finally:
        if cursor:
            cursor.close()

def get_adresse_id_from_data(conn, values):
    try:
        query = f"""
        SELECT id FROM Adresse
        WHERE rue = '{values["rue"]}' AND numero = '{values["numero"]}' AND codepostal = '{values["codePostal"]}' AND ville = '{values["ville"]}'
        """
        return execute_query(conn, query)[0]
    except:
        return ""

def get_utilisateur_id_from_login(conn, login):
    try:
        query = f"""
        SELECT id FROM Utilisateur
        WHERE login = '{login}'
        """
        return execute_query(conn, query)[0][0]
    except:
        return ""

def insert_personnel(conn):
    os.system("cls")
    values = {}
    values['login'] = input("Login: ")
    values['password'] = input("Password: ")
    values['prenom'] = input("Prenom: ")
    values['nom'] = input("Nom: ")
    values['email'] = input("Email: ")
    values['rue'] = input("Rue: ")
    values['numero'] = input("N°: ")
    values['codePostal'] = input("Code Postal: ")
    values['ville'] = input("Ville: ")
    try:
        insert_into_adresse(conn,values)
    except:
        print("")
    values['id_adresse'] = get_adresse_id_from_data(conn, values)
    if values['id_adresse'] != "":
        try:
            insert_into_utilisateur(conn, values)
        except:
            print("")
        values['id_utilisateur'] = get_utilisateur_id_from_login(conn, values["login"])
        if values['id_utilisateur'] != "":
            insert_into_personnel(conn,values)

def delete_personnel(conn):
    login = input("Login du membre du personnel à supprimer: ")
    choice = input("Voulez-vous supprimer ses données utilisateurs ? (oui/non): ")
    if choice == "oui":  
        query = f"""
            DELETE FROM Utilisateur
            WHERE login = '{login}'
            """
        execute_query(conn, query)
    else:
        id = get_utilisateur_id_from_login(conn, login)
        query = f"""
            DELETE FROM Personnel
            WHERE id = '{id}'
            """
        execute_query(conn, query)

def insert_adherent(conn):
    os.system("cls")
    values = {}
    values['login'] = input("Login: ")
    values['password'] = input("Password: ")
    values['prenom'] = input("Prenom: ")
    values['nom'] = input("Nom: ")
    values['email'] = input("Email: ")
    values['numeroTelephone'] = input("numero de téléphone: ")
    values['dateNaissance'] = input("Date de naissance (YYYY-MM-DD): ")
    values['statut'] = "active"
    values['rue'] = input("Rue: ")
    values['numero'] = input("N°: ")
    values['codePostal'] = input("Code Postal: ")
    values['ville'] = input("Ville: ")
    try:
        insert_into_adresse(conn,values)
    except:
        print("")
    values['id_adresse'] = get_adresse_id_from_data(conn, values)
    if values['id_adresse'] != "":
        try:
            insert_into_utilisateur(conn, values)
        except:
            print("")
        values['id_utilisateur'] = get_utilisateur_id_from_login(conn, values["login"])
        if values['id_utilisateur'] != "":
            insert_into_adherent(conn,values)

def delete_adherent(conn):
    login = input("Login de l'adhérent à supprimer: ")
    choice = input("Voulez-vous supprimer ses données utilisateurs ? (oui/non): ")
    if choice == "oui":  
        query = f"""
            DELETE FROM Utilisateur
            WHERE login = '{login}'
            """
        execute_query(conn, query)
    else:
        id = get_utilisateur_id_from_login(conn, login)
        query = f"""
            DELETE FROM Adherent
            WHERE id = '{id}'
            """
        execute_query(conn, query)

def insert_prêt(conn,login):
    values = {}
    values['id_responsable'] = check_login_personnel_valid(conn, login)
    os.system('cls')
    if values['id_responsable'] != "":
        login = input("Entrez un login Adhérent: ")
        values['id_adherent'] = check_login_adherent_valid(conn, login)
        os.system('cls')
        if values['id_adherent'] != "":
            title = input("Entrez le titre de la ressource: ")
            os.system('cls')
            films = get_film_exemplaires_disponibles(conn, title)
            musiques = get_musique_exemplaires_disponibles(conn, title)
            livres = get_livre_exemplaires_disponibles(conn, title)
            print("Livres")
            print("{:<10} {:<15} {:<50} {:<15}".format("Index", "Titre", "Résumé", "Langue"))
            print("=" * 90)
            for index, row in enumerate(livres):
                print("{:<10} {:<15} {:<50} {:<15}".format(index, row[1], row[2], row[3]))
            print("=" * 90)
            print("\n")
            print("Films")
            print("{:<10} {:<15} {:<50} {:<10}".format("Index", "Titre", "Synopsis", "Langue"))
            print("=" * 90)
            for index, row in enumerate(films):
                print("{:<10} {:<15} {:<50} {:<10}".format(index+len(livres), row[1], row[2], row[3]))
            print("=" * 90)
            print("\n")
            print("Musiques")
            print("{:<10} {:<15} {:<50} {:<10}".format("Index", "Titre", "Editeur", "Longueur"))
            print("=" * 90)
            for index, row in enumerate(musiques):
                print("{:<10} {:<15} {:<50} {:<10}".format(index+len(musiques)+len(livres), row[1], row[2], row[3]))
            print("=" * 90)
            choice = int(input("Index de la ressource d'intérêt (-1 pour annuler): "))
            if choice in range(-1, len(films)+len(musiques)+len(livres)):
                if choice != -1:
                        if choice < len(livres):
                            ressource = livres[choice]
                        elif choice >= len(livres) + len(films):
                            ressource = musiques[choice-len(livres)-len(films)]
                        else:
                            ressource = films[choice-len(livres)]
                        display_exemplaires_prêt(conn, ressource, values)


def choose_table(conn):
    os.system("cls")
    print("Choisissez la table dans laquelle vous souhaitez insérer des données :")
    print("1. Livre")
    print("2. Musique")
    print("3. Film")
    print("4. Retour")
    # Ajoutez d'autres tables ici

    table_choice = get_user_input("Entrez le numéro de la table : ", int)

    # Saisie des valeurs auprès de l'utilisateur
    values = {}

    if table_choice == 1:  # Si la table est Livre
            values['titre'] = input("Entrez le titre de la ressource : ")
            values['dateApparition'] = input("Entrez la date d'apparition de la ressource (format YYYY-MM-DD) : ")
            values['editeur'] = input("Entrez l'éditeur de la ressource : ")
            values['genre'] = input("Entrez le genre de la ressource : ")
            values['codeClassification'] = get_user_input("Entrez le code de classification de la ressource : ", int)
            values['ISBN'] = input("Entrez le code ISBN du livre : ")
            values['resume'] = input("Entrez le résumé du livre : ")
            values['langue'] = input("Entrez la langue du livre : ")
            values['dureeMaxPret'] = get_user_input("Entrez la durée maximum de prêt (en jours) : ", int)
            insert_livre(conn, values)
    # ...

    elif table_choice == 2:  # Si la table est Musique
        values['titre'] = input("Entrez le titre de la ressource : ")
        values['dateApparition'] = input("Entrez la date d'apparition de la ressource (format YYYY-MM-DD) : ")
        values['editeur'] = input("Entrez l'éditeur de la ressource : ")
        values['genre'] = input("Entrez le genre de la ressource : ")
        values['codeClassification'] = get_user_input("Entrez le code de classification de la ressource : ", int)
        values['longueur'] = get_user_input("Entrez la longueur de la musique (en secondes) : ", int)
        values['dureeMaxPret'] = get_user_input("Entrez la durée maximum de prêt (en jours) : ", int)
        insert_musique(conn, values)

    elif table_choice == 3:  # Si la table est Film
        values['titre'] = input("Entrez le titre de la ressource : ")
        values['dateApparition'] = input("Entrez la date d'apparition de la ressource (format YYYY-MM-DD) : ")
        values['editeur'] = input("Entrez l'éditeur de la ressource : ")
        values['genre'] = input("Entrez le genre de la ressource : ")
        values['codeClassification'] = get_user_input("Entrez le code de classification de la ressource : ", int)
        values['langue'] = input("Entrez la langue du film : ")
        values['length'] = get_user_input("Entrez la durée du film (en minutes) : ", int)
        values['synopsis'] = input("Entrez le synopsis du film : ")
        values['dureeMaxPret'] = get_user_input("Entrez la durée maximum de prêt (en jours) : ", int)
        insert_film(conn, values)

def get_active_sanctions_from_login(conn,login):
    query = f"""
            SELECT login, sanctions FROM AdherentDetails
            WHERE login LIKE '{login}%' AND (
                (sanctions->>'dateFinSanction' IS NULL OR (sanctions->>'dateFinSanction')::DATE > CURRENT_DATE) 
                OR (sanctions->>'paye' = 'false' OR sanctions->>'paye' IS NULL)
            )
    """
    results = execute_query(conn, query)
    return results

def handle_sanctions(conn):
            os.system("cls")
            login = input("Entrez un login : ")
            os.system("cls")
            sanctions = get_active_sanctions_from_login(conn,login)
            print("Sanctions")
            print("{:<6} {:<10} {:<16} {:<18} {:<15} {:<10} {:<10}".format("Index", "Login", "Date sanction", "Date fin sanction", "Motif", "Montant", "Payé"))
            print("=" * 90)
            for index, user in enumerate(sanctions):
                for index2, sanction in enumerate(user[1]):
                    print("{:<6} {:<10} {:<16} {:<18} {:<15} {:<10} {:<10}".format(
                        index2 + 1,
                        user[0] if user[0] is not None else "",
                        f'{sanction["dateSanction"]}' if sanction["dateSanction"] is not None else "",
                        f'{sanction["dateFinSanction"]}' if sanction["dateFinSanction"] is not None else "",
                        sanction["motif"] if sanction["motif"] is not None else "",
                        sanction["montant"] if sanction["montant"] is not None else "",
                        'Oui' if sanction["paye"] is not None or sanction["paye"]==1 else "Non"
                    ))
            print("=" * 90)
            print("\n")
            choice = int(input("Sélectionnez un index de sanction (-1 retour): "))
            if choice in range(-1, len(sanctions)+1):
                if choice != -1 and choice !=0:
                    handle_sanction(conn, sanctions[choice-1])

def handle_sanctions_adherent(conn,login):
            os.system("cls")
            sanctions = get_active_sanctions_from_login(conn,login)
            print("Sanctions")
            print("{:<6} {:<10} {:<16} {:<18} {:<15} {:<10} {:<10}".format("Index", "Login", "Date sanction", "Date fin sanction", "Motif", "Montant", "Payé"))
            print("=" * 90)
            for index, user in enumerate(sanctions):
                for index2, sanction in enumerate(user[1]):
                    print("{:<6} {:<10} {:<16} {:<18} {:<15} {:<10} {:<10}".format(
                        index2 + 1,
                        user[0] if user[0] is not None else "",
                        f'{sanction["dateSanction"]}' if sanction["dateSanction"] is not None else "",
                        f'{sanction["dateFinSanction"]}' if sanction["dateFinSanction"] is not None else "",
                        sanction["motif"] if sanction["motif"] is not None else "",
                        sanction["montant"] if sanction["montant"] is not None else "",
                        'Oui' if sanction["paye"] is not None or sanction["paye"]==1 else "Non"
                    ))
            print("=" * 90)
            print("\n")
            print("1. Retour")
            choice = input("Que voulez-vous faire ?")

def handle_sanction(conn, sanction):
    print("1. Régler la sanction")
    print("2. Ajouter date de fin à la sanction")
    print("3. Supprimer la sanction")
    print("4. Annuler")
    choice = int(input("Que voulez-vous faire ?: "))
    if choice ==1 :
        pay_sanction(conn, sanction[1])
    elif choice == 2:
        set_end_date_sanction(conn, sanction[1])
    elif choice == 3:
        delete_sanction(conn, sanction[1])

def pay_sanction(conn, id_sanction):
    query = f"""
    UPDATE Sanction
    SET paye = 'true'
    WHERE id_sanction = '{id_sanction}';
    """
    execute_query(conn,query)

def set_end_date_sanction(conn, id_sanction):
    date = input("Date de fin sanction (YYYY-MM-DD): ")
    query = f"""
    UPDATE Sanction
    SET datefinsanction = '{date}'
    WHERE id_sanction = '{id_sanction}';
    """
    execute_query(conn,query)

def delete_sanction(conn, id_sanction):
    query = f"""
    DELETE FROM Sanction
    WHERE id_sanction = '{id_sanction}';
    """
    execute_query(conn,query)

def check_credentials(conn, login, pwd):
    query = f"""
    SELECT * FROM Utilisateur
    WHERE login = '{login}' AND password = '{pwd}'
    """
    results = execute_query(conn, query)
    if len(results)>0:
        if is_personnel(conn, login):
            return "personnel"
        else:
            statut = get_adherent_details(conn, login)[0][9]
            if statut == 'active':
                return "adherent"
    return "non"

def global_stats(conn):
    query = f"""
    SELECT titre, COUNT(titre) FROM PretDetails
    GROUP BY titre
    ORDER BY COUNT(titre) DESC
    """
    results = execute_query(conn, query)
    if len(results)>0:
        print("Statistiques\n")
        print("{:<15}{:<5}".format("Titre", "Nombre d'emprunts"))
        for result in results:
            print("{:<15}{:<5}".format(result[0], result[1]))
        print("\n1. Retour")
        choice = input("Que voulez_vous faire ? : ")

def recommandations(conn, login):
    query = f"""
    SELECT P.titre, P.genre, COUNT(P.titre) FROM PretDetails P
    WHERE P.login='{login}'
    GROUP BY titre, genre
    ORDER BY COUNT(titre) DESC
    """
    results = execute_query(conn, query) 
    if len(results)>0:
        titre = results[0][0]
        print(f"Comme vous avez aimé {results[0][0]}")
        print(f"Nous vous recommandons dans le même genre '{results[0][1]}' :\n")
        query = f"""
        SELECT titre FROM Ressource R
        WHERE R.genre='{results[0][1]}'
        """
        results = execute_query(conn, query)
        if len(results)>0: 
            for result in results:
                if result[0] != titre:
                    print("{:<15}".format(result[0]))
        print("\n1. Retour")
        choice = input("Que voulez_vous faire ? : ")

def insert_livre(conn, values):
    insert_query = sql.SQL("INSERT INTO Livre (titre, dateApparition, editeur, genre, codeClassification, dureeMaxPret, ISBN, resume, langue) VALUES ({}, {}, {}, {}, {}, {}, {}, {}, {})").format(
            sql.Literal(values['titre']),
            sql.Literal(values['dateApparition']),
            sql.Literal(values['editeur']),
            sql.Literal(values['genre']),
            sql.Literal(values['codeClassification']),
            sql.Literal(values['dureeMaxPret']),
            sql.Literal(values['ISBN']),
            sql.Literal(values['resume']),
            sql.Literal(values['langue'])
        )
    cursor = conn.cursor()
    cursor.execute(insert_query)
    conn.commit()
    cursor.close()

def insert_musique(conn, values):
    insert_query = sql.SQL("INSERT INTO Musique (titre, dateApparition, editeur, genre, codeClassification, dureeMaxPret, longueur) VALUES ({}, {}, {}, {}, {}, {}, {})").format(
            sql.Literal(values['titre']),
            sql.Literal(values['dateApparition']),
            sql.Literal(values['editeur']),
            sql.Literal(values['genre']),
            sql.Literal(values['codeClassification']),
            sql.Literal(values['dureeMaxPret']),
            sql.Literal(values['longueur'])
        )
    cursor = conn.cursor()
    cursor.execute(insert_query)
    conn.commit()
    cursor.close()

def insert_film(conn, values):
    insert_query = sql.SQL("INSERT INTO Film (titre, dateApparition, editeur, genre, codeClassification, dureeMaxPret, langue, length, synopsis) VALUES ({}, {}, {}, {}, {}, {}, {})").format(
            sql.Literal(values['titre']),
            sql.Literal(values['dateApparition']),
            sql.Literal(values['editeur']),
            sql.Literal(values['genre']),
            sql.Literal(values['codeClassification']),
            sql.Literal(values['dureeMaxPret']),
            sql.Literal(values['langue']),
            sql.Literal(values['length']),
            sql.Literal(values['synopsis'])
        )
    cursor = conn.cursor()
    cursor.execute(insert_query)
    conn.commit()
    cursor.close()