import os
import psycopg2
from psycopg2 import sql
from helpers import execute_query

def insert_into_ressource(connection, values):
    try:
        cursor = connection.cursor()
        insert_query = sql.SQL("INSERT INTO Ressource (titre, dateApparition, editeur, genre, codeClassification) VALUES ({}, {}, {}, {}, {})").format(
            sql.Literal(values['titre']),
            sql.Literal(values['dateApparition']),
            sql.Literal(values['editeur']),
            sql.Literal(values['genre']),
            sql.Literal(values['codeClassification'])
        )
        cursor.execute(insert_query)
        connection.commit()
        print("Insertion réussie dans la table Ressource")
        query = f"""
            SELECT id FROM Ressource
            WHERE titre = '{values['titre']}' AND dateApparition = '{values['dateApparition']}' AND editeur = '{values['editeur']}' AND genre = '{values['genre']}' AND codeClassification = '{values['codeClassification']}'
            """
        return execute_query(connection, query)[0]
    except (Exception, psycopg2.Error) as error:
        print("Erreur lors de l'insertion dans la table Ressource:", error)
    finally:
        if cursor:
            cursor.close()

# Insertion dans la table Livre
def insert_into_livre(connection, values):
    try:
        id = insert_into_ressource(connection, values)
        cursor = connection.cursor()
        insert_query = sql.SQL("INSERT INTO Livre (id_livre, ISBN, resume, langue) VALUES ({}, {}, {}, {})").format(
            sql.Literal(id),
            sql.Literal(values['ISBN']),
            sql.Literal(values['resume']),
            sql.Literal(values['langue'])
        )
        cursor.execute(insert_query)
        connection.commit()
        print("Insertion réussie dans la table Livre")
    except (Exception, psycopg2.Error) as error:
        print("Erreur lors de l'insertion dans la table Livre:", error)
    finally:
        if cursor:
            cursor.close()


# Exemple d'insertion dans la table Musique
def insert_into_musique(connection, values):
    try:
        id = insert_into_ressource(connection, values)
        cursor = connection.cursor()
        insert_query = sql.SQL("INSERT INTO Musique (id_musique, longueur) VALUES ({}, {})").format(
            sql.Literal(id),
            sql.Literal(values['longueur'])
        )
        cursor.execute(insert_query)
        connection.commit()
        print("Insertion réussie dans la table Musique")
    except (Exception, psycopg2.Error) as error:
        print("Erreur lors de l'insertion dans la table Musique:", error)
    finally:
        if cursor:
            cursor.close()




# Exemple d'insertion dans la table Film
def insert_into_film(connection, values):
    try:
        id = insert_into_ressource(connection, values)
        cursor = connection.cursor()
        insert_query = sql.SQL("INSERT INTO Film (id_film, langue, length, synopsis) VALUES ({}, {}, {}, {})").format(
            sql.Literal(id),
            sql.Literal(values['langue']),
            sql.Literal(values['length']),
            sql.Literal(values['synopsis'])
        )
        cursor.execute(insert_query)
        connection.commit()
        print("Insertion réussie dans la table Film")
    except (Exception, psycopg2.Error) as error:
        print("Erreur lors de l'insertion dans la table Film:", error)
    finally:
        if cursor:
            cursor.close()

# Exemple d'insertion dans la table Contributeur
def insert_into_contributeur(connection, values):
    try:
        cursor = connection.cursor()
        insert_query = sql.SQL("INSERT INTO Contributeur (id, prenom, nom, dateNaissance, nationalite) VALUES ({}, {}, {}, {}, {})").format(
            sql.Literal(values['id']),
            sql.Literal(values['prenom']),
            sql.Literal(values['nom']),
            sql.Literal(values['dateNaissance']),
            sql.Literal(values['nationalite'])
        )
        cursor.execute(insert_query)
        connection.commit()
        print("Insertion réussie dans la table Contributeur")
    except (Exception, psycopg2.Error) as error:
        print("Erreur lors de l'insertion dans la table Contributeur:", error)
    finally:
        if cursor:
            cursor.close()

# Répétez ce processus pour les autres tables

# Exemple d'insertion dans la table Auteur
def insert_into_auteur(connection, values):
    try:
        cursor = connection.cursor()
        insert_query = sql.SQL("INSERT INTO Auteur (id_livre, id_contributeur) VALUES ({}, {})").format(
            sql.Literal(values['id_livre']),
            sql.Literal(values['id_contributeur'])
        )
        cursor.execute(insert_query)
        connection.commit()
        print("Insertion réussie dans la table Auteur")
    except (Exception, psycopg2.Error) as error:
        print("Erreur lors de l'insertion dans la table Auteur:", error)
    finally:
        if cursor:
            cursor.close()

# Continuez ce modèle pour les autres tables (Interprete, Compositeur, Acteur, Realisateur, Exemplaire, Adresse, Utilisateur, Personnel, Adherent, Pret, Sanction)

# Exemple d'insertion dans la table Interprete
def insert_into_interprete(connection, values):
    try:
        cursor = connection.cursor()
        insert_query = sql.SQL("INSERT INTO Interprete (id_musique, id_contributeur) VALUES ({}, {})").format(
            sql.Literal(values['id_musique']),
            sql.Literal(values['id_contributeur'])
        )
        cursor.execute(insert_query)
        connection.commit()
        print("Insertion réussie dans la table Interprete")
    except (Exception, psycopg2.Error) as error:
        print("Erreur lors de l'insertion dans la table Interprete:", error)
    finally:
        if cursor:
            cursor.close()

# Exemple d'insertion dans la table Compositeur
def insert_into_compositeur(connection, values):
    try:
        cursor = connection.cursor()
        insert_query = sql.SQL("INSERT INTO Compositeur (id_musique, id_contributeur) VALUES ({}, {})").format(
            sql.Literal(values['id_musique']),
            sql.Literal(values['id_contributeur'])
        )
        cursor.execute(insert_query)
        connection.commit()
        print("Insertion réussie dans la table Compositeur")
    except (Exception, psycopg2.Error) as error:
        print("Erreur lors de l'insertion dans la table Compositeur:", error)
    finally:
        if cursor:
            cursor.close()

# Continuez ce modèle pour les autres tables (Acteur, Realisateur, Exemplaire, Adresse, Utilisateur, Personnel, Adherent, Pret, Sanction)

# Exemple d'insertion dans la table Acteur
def insert_into_acteur(connection, values):
    try:
        cursor = connection.cursor()
        insert_query = sql.SQL("INSERT INTO Acteur (id_film, id_contributeur) VALUES ({}, {})").format(
            sql.Literal(values['id_film']),
            sql.Literal(values['id_contributeur'])
        )
        cursor.execute(insert_query)
        connection.commit()
        print("Insertion réussie dans la table Acteur")
    except (Exception, psycopg2.Error) as error:
        print("Erreur lors de l'insertion dans la table Acteur:", error)
    finally:
        if cursor:
            cursor.close()

# Répétez ce processus pour les autres tables

# Exemple d'insertion dans la table Realisateur
def insert_into_realisateur(connection, values):
    try:
        cursor = connection.cursor()
        insert_query = sql.SQL("INSERT INTO Realisateur (id_film, id_contributeur) VALUES ({}, {})").format(
            sql.Literal(values['id_film']),
            sql.Literal(values['id_contributeur'])
        )
        cursor.execute(insert_query)
        connection.commit()
        print("Insertion réussie dans la table Realisateur")
    except (Exception, psycopg2.Error) as error:
        print("Erreur lors de l'insertion dans la table Realisateur:", error)
    finally:
        if cursor:
            cursor.close()

# Continuez ce modèle pour les autres tables (Exemplaire, Adresse, Utilisateur, Personnel, Adherent, Pret, Sanction)

# Exemple d'insertion dans la table Exemplaire
def insert_into_exemplaire(connection, values):
    try:
        cursor = connection.cursor()
        insert_query = sql.SQL("INSERT INTO Exemplaire (id, id_ressource, etat, disponible) VALUES ({}, {}, {}, {})").format(
            sql.Literal(values['id']),
            sql.Literal(values['id_ressource']),
            sql.Literal(values['etat']),
            sql.Literal(values['disponible'])
        )
        cursor.execute(insert_query)
        connection.commit()
        print("Insertion réussie dans la table Exemplaire")
    except (Exception, psycopg2.Error) as error:
        print("Erreur lors de l'insertion dans la table Exemplaire:", error)
    finally:
        if cursor:
            cursor.close()

# Répétez ce processus pour les autres tables

# Exemple d'insertion dans la table Adresse
def insert_into_adresse(connection, values):
    try:
        cursor = connection.cursor()
        insert_query = sql.SQL("INSERT INTO Adresse (id, rue, numero, codePostal, ville) VALUES ({}, {}, {}, {}, {})").format(
            sql.Literal(values['id']),
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

# Exemple d'insertion dans la table Utilisateur
def insert_into_utilisateur(connection, values):
    try:
        cursor = connection.cursor()
        insert_query = sql.SQL("INSERT INTO Utilisateur (id, login, password, prenom, nom, email, adresse) VALUES ({}, {}, {}, {}, {}, {}, {})").format(
            sql.Literal(values['id']),
            sql.Literal(values['login']),
            sql.Literal(values['password']),
            sql.Literal(values['prenom']),
            sql.Literal(values['nom']),
            sql.Literal(values['email']),
            sql.Literal(values['adresse'])
        )
        cursor.execute(insert_query)
        connection.commit()
        print("Insertion réussie dans la table Utilisateur")
    except (Exception, psycopg2.Error) as error:
        print("Erreur lors de l'insertion dans la table Utilisateur:", error)
    finally:
        if cursor:
            cursor.close()

# Répétez ce processus pour les autres tables

# Exemple d'insertion dans la table Personnel
def insert_into_personnel(connection, values):
    try:
        cursor = connection.cursor()
        insert_query = sql.SQL("INSERT INTO Personnel (id, id_personnel) VALUES ({}, {})").format(
            sql.Literal(values['id']),
            sql.Literal(values['id_personnel'])
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
            sql.Literal(values['id']),
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

# Répétez ce processus pour les autres tables

# Exemple d'insertion dans la table Pret
def insert_into_pret(connection, values):
    try:
        cursor = connection.cursor()
        insert_query = sql.SQL("INSERT INTO Pret (id, id_exemplaire, id_adherent, id_responsable, datePret, duree, dateRetour, etatRetour) VALUES ({}, {}, {}, {}, {}, {}, {}, {})").format(
            sql.Literal(values['id']),
            sql.Literal(values['id_exemplaire']),
            sql.Literal(values['id_adherent']),
            sql.Literal(values['id_responsable']),
            sql.Literal(values['datePret']),
            sql.Literal(values['duree']),
            sql.Literal(values['dateRetour']),
            sql.Literal(values['etatRetour'])
        )
        cursor.execute(insert_query)
        connection.commit()
        print("Insertion réussie dans la table Pret")
    except (Exception, psycopg2.Error) as error:
        print("Erreur lors de l'insertion dans la table Pret:", error)
    finally:
        if cursor:
            cursor.close()

# Exemple d'insertion dans la table Sanction
def insert_into_sanction(connection, values):
    try:
        cursor = connection.cursor()
        insert_query = sql.SQL("INSERT INTO Sanction (id_sanction, DateSanction, DateFinSanction, motif, montant) VALUES ({}, {}, {}, {}, {})").format(
            sql.Literal(values['id_sanction']),
            sql.Literal(values['DateSanction']),
            sql.Literal(values['DateFinSanction']),
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

def get_user_input(prompt, data_type):
    while True:
        try:
            user_input = data_type(input(prompt))
            return user_input
        except ValueError:
            print("Erreur de saisie. Veuillez entrer une valeur valide.")
            
def insert_data_into_table(connection, table_choice, values):
    # if table_choice == 1:
    #     insert_into_ressource(connection, values)
    if table_choice == 1:
        insert_into_livre(connection, values)
    elif table_choice == 2:
        insert_into_musique(connection, values)
    elif table_choice == 3:
        insert_into_film(connection, values)
    # elif table_choice == 5:
    #     insert_into_contributeur(connection, values)
    # elif table_choice == 6:
    #     insert_into_auteur(connection, values)
    # elif table_choice == 7:
    #     insert_into_interprete(connection, values)
    # elif table_choice == 8:
    #     insert_into_compositeur(connection, values)
    # elif table_choice == 9:
    #     insert_into_acteur(connection, values)
    # elif table_choice == 10:
    #     insert_into_realisateur(connection, values)
    # elif table_choice == 11:
    #     insert_into_exemplaire(connection, values)
    # elif table_choice == 12:
    #     insert_into_adresse(connection, values)
    # elif table_choice == 13:
    #     insert_into_utilisateur(connection, values)
    # elif table_choice == 14:
    #     insert_into_personnel(connection, values)
    # elif table_choice == 15:
    #     insert_into_adherent(connection, values)
    # elif table_choice == 16:
    #     insert_into_pret(connection, values)
    # elif table_choice == 17:
    #     insert_into_sanction(connection, values)
    else:
        print("\n")

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
    # if table_choice == 1:  # Si la table est Ressource
    #     values['id'] = get_user_input("Entrez l'ID de la ressource : ", int)
    #     values['titre'] = input("Entrez le titre de la ressource : ")
    #     values['dateApparition'] = input("Entrez la date d'apparition de la ressource (format YYYY-MM-DD) : ")
    #     values['editeur'] = input("Entrez l'éditeur de la ressource : ")
    #     values['genre'] = input("Entrez le genre de la ressource : ")
    #     values['codeClassification'] = get_user_input("Entrez le code de classification de la ressource : ", int)
    
    if table_choice == 1:  # Si la table est Livre
            values['titre'] = input("Entrez le titre de la ressource : ")
            values['dateApparition'] = input("Entrez la date d'apparition de la ressource (format YYYY-MM-DD) : ")
            values['editeur'] = input("Entrez l'éditeur de la ressource : ")
            values['genre'] = input("Entrez le genre de la ressource : ")
            values['codeClassification'] = get_user_input("Entrez le code de classification de la ressource : ", int)
            values['ISBN'] = input("Entrez le code ISBN du livre : ")
            values['resume'] = input("Entrez le résumé du livre : ")
            values['langue'] = input("Entrez la langue du livre : ")
    # ...

    elif table_choice == 2:  # Si la table est Musique
        values['titre'] = input("Entrez le titre de la ressource : ")
        values['dateApparition'] = input("Entrez la date d'apparition de la ressource (format YYYY-MM-DD) : ")
        values['editeur'] = input("Entrez l'éditeur de la ressource : ")
        values['genre'] = input("Entrez le genre de la ressource : ")
        values['codeClassification'] = get_user_input("Entrez le code de classification de la ressource : ", int)
        values['longueur'] = get_user_input("Entrez la longueur de la musique (en secondes) : ", int)

    elif table_choice == 3:  # Si la table est Film
        values['titre'] = input("Entrez le titre de la ressource : ")
        values['dateApparition'] = input("Entrez la date d'apparition de la ressource (format YYYY-MM-DD) : ")
        values['editeur'] = input("Entrez l'éditeur de la ressource : ")
        values['genre'] = input("Entrez le genre de la ressource : ")
        values['codeClassification'] = get_user_input("Entrez le code de classification de la ressource : ", int)
        values['langue'] = input("Entrez la langue du film : ")
        values['length'] = get_user_input("Entrez la durée du film (en minutes) : ", int)
        values['synopsis'] = input("Entrez le synopsis du film : ")

    # elif table_choice == 5:  # Si la table est Contributeur
    #     values['id'] = get_user_input("Entrez l'ID du contributeur : ", int)
    #     values['prenom'] = input("Entrez le prénom du contributeur : ")
    #     values['nom'] = input("Entrez le nom du contributeur : ")
    #     values['dateNaissance'] = input("Entrez la date de naissance du contributeur (format YYYY-MM-DD) : ")
    #     values['nationalite'] = input("Entrez la nationalité du contributeur : ")

    # elif table_choice == 6:  # Si la table est Auteur
    #     values['id_livre'] = get_user_input("Entrez l'ID du livre : ", int)
    #     values['id_contributeur'] = get_user_input("Entrez l'ID du contributeur : ", int)


    # elif table_choice == 7:  # Si la table est Interprete
    #     values['id_musique'] = get_user_input("Entrez l'ID de la musique : ", int)
    #     values['id_contributeur'] = get_user_input("Entrez l'ID du contributeur : ", int)

    # elif table_choice == 8:  # Si la table est Compositeur
    #     values['id_musique'] = get_user_input("Entrez l'ID de la musique : ", int)
    #     values['id_contributeur'] = get_user_input("Entrez l'ID du contributeur : ", int)

    # elif table_choice == 9:  # Si la table est Acteur
    #     values['id_film'] = get_user_input("Entrez l'ID du film : ", int)
    #     values['id_contributeur'] = get_user_input("Entrez l'ID du contributeur : ", int)

    # elif table_choice == 10:  # Si la table est Realisateur
    #     values['id_film'] = get_user_input("Entrez l'ID du film : ", int)
    #     values['id_contributeur'] = get_user_input("Entrez l'ID du contributeur : ", int)

    # elif table_choice == 11:  # Si la table est Exemplaire
    #     values['id'] = get_user_input("Entrez l'ID de l'exemplaire : ", int)
    #     values['id_ressource'] = get_user_input("Entrez l'ID de la ressource associée : ", int)
    #     values['etat'] = input("Entrez l'état de l'exemplaire : ")
    #     values['disponible'] = input("L'exemplaire est-il disponible ? (True/False) : ")  # Vous pouvez ajuster cela en fonction du type de votre colonne

    # elif table_choice == 12:  # Si la table est Adresse
    #     values['id'] = get_user_input("Entrez l'ID de l'adresse : ", int)
    #     values['rue'] = input("Entrez le nom de la rue : ")
    #     values['numero'] = get_user_input("Entrez le numéro de l'adresse : ", int)
    #     values['codePostal'] = get_user_input("Entrez le code postal : ", int)
    #     values['ville'] = input("Entrez le nom de la ville : ")

    # elif table_choice == 13:  # Si la table est Utilisateur
    #     values['id'] = get_user_input("Entrez l'ID de l'utilisateur : ", int)
    #     values['login'] = input("Entrez le nom d'utilisateur : ")
    #     values['password'] = input("Entrez le mot de passe : ")  # Assurez-vous de gérer les mots de passe de manière sécurisée dans une application réelle
    #     values['prenom'] = input("Entrez le prénom de l'utilisateur : ")
    #     values['nom'] = input("Entrez le nom de l'utilisateur : ")
    #     values['email'] = input("Entrez l'adresse e-mail de l'utilisateur : ")
    #     values['adresse'] = get_user_input("Entrez l'ID de l'adresse associée : ", int)

    # elif table_choice == 14:  # Si la table est Personnel
    #     values['id'] = get_user_input("Entrez l'ID du personnel : ", int)
    #     values['id_personnel'] = get_user_input("Entrez l'ID de l'utilisateur associé à ce personnel : ", int)

    # elif table_choice == 15:  # Si la table est Adherent
    #     values['id'] = get_user_input("Entrez l'ID de l'adhérent : ", int)
    #     values['numeroTelephone'] = input("Entrez le numéro de téléphone de l'adhérent : ")
    #     values['dateNaissance'] = input("Entrez la date de naissance de l'adhérent (format YYYY-MM-DD) : ")
    #     values['statut'] = input("Entrez le statut de l'adhérent : ")

    # elif table_choice == 16:  # Si la table est Pret
    #     values['id'] = get_user_input("Entrez l'ID du prêt : ", int)
    #     values['id_exemplaire'] = get_user_input("Entrez l'ID de l'exemplaire : ", int)
    #     values['id_adherent'] = get_user_input("Entrez l'ID de l'adhérent : ", int)
    #     values['id_responsable'] = get_user_input("Entrez l'ID du responsable du prêt : ", int)
    #     values['datePret'] = input("Entrez la date de prêt (format YYYY-MM-DD) : ")
    #     values['duree'] = get_user_input("Entrez la durée du prêt (en jours) : ", int)
    #     values['dateRetour'] = input("Entrez la date de retour (format YYYY-MM-DD) : ")
    #     values['etatRetour'] = input("Entrez l'état de retour : ")

    # elif table_choice == 17:  # Si la table est Sanction
    #     values['id_sanction'] = get_user_input("Entrez l'ID de la sanction : ", int)
    #     values['DateSanction'] = input("Entrez la date de la sanction (format YYYY-MM-DD) : ")
    #     values['DateFinSanction'] = input("Entrez la date de fin de la sanction (format YYYY-MM-DD) : ")
    #     values['motif'] = input("Entrez le motif de la sanction : ")
    #     values['montant'] = get_user_input("Entrez le montant de la sanction : ", float)



    # Appelez la fonction d'insertion correspondante
    insert_data_into_table(conn, table_choice, values)
    
