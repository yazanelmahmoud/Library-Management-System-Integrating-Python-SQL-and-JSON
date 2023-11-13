import os
import psycopg2

def connect_to_db(name):
    conn = psycopg2.connect(database = name, 
                        user = "postgres", 
                        host= 'localhost',
                        password = "postgres",
                        port = 5432)
    return conn

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

def execute_sql_file(conn, filename):
    # Create a cursor object to execute SQL statements
    cursor = conn.cursor()

    # Read the SQL file
    with open(filename, 'r') as file:
        sql_script = file.read()

    # Execute the SQL script
    cursor.execute(sql_script)

    # Commit the changes and close the connection
    conn.commit()

############################ PAS UTILISE ###############################################
def create_tables(conn):
    execute_sql_file(conn, "../rendu 3/CreateDB.session.sql")
    execute_sql_file(conn, "../rendu 3/InsertDB.session.sql")

def get_prets_from_login(conn, login):
    query = f"""
            SELECT * FROM PretDetails
            WHERE login = '{login}'
    """
    results = execute_query(conn, query)
    return results

def get_film_exemplaires(conn, titre):
    query = f"""
            SELECT * FROM FilmExemplaires
            WHERE titre_film LIKE '{titre}%'
    """
    results = execute_query(conn, query)
    return results

def get_film_exemplaires_disponibles(conn, titre):
    query = f"""
            SELECT titre_film, COUNT(titre_film) FROM FilmExemplaires
            WHERE titre_film LIKE '{titre}%' AND disponible = 'true'
            GROUP BY titre_film
    """
    results = execute_query(conn, query)
    return results

def get_film_ressources(conn, titre):
    query = f"""
            SELECT * FROM FilmDetails
            WHERE titre_film LIKE '{titre}%'
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
            SELECT titre_musique, COUNT(titre_musique) FROM MusiqueExemplaires
            WHERE titre_musique LIKE '{titre}%' AND disponible = 'true'
            GROUP BY titre_musique
    """
    results = execute_query(conn, query)
    return results

def get_musique_ressources(conn, titre):
    query = f"""
            SELECT * FROM MusiqueDetails
            WHERE titre_musique LIKE '{titre}%'
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
            SELECT titre_livre, COUNT(titre_livre) FROM LivreExemplaires
            WHERE titre_livre LIKE '{titre}%' AND disponible = 'true'
            GROUP BY titre_livre
    """
    results = execute_query(conn, query)
    return results

def get_livre_ressources(conn,titre):
    query = f"""
            SELECT * FROM LivreDetails
            WHERE titre_livre LIKE '{titre}%'
    """
    results = execute_query(conn, query)
    return results

def get_adherent_details(conn, login):
    query = f"""
            SELECT * FROM AdherentDetails
            WHERE login = '{login}'
    """
    results = execute_query(conn, query)
    return results   

def get_personnel_details(conn, login):
    query = f"""
            SELECT * FROM PersonnelDetails
            WHERE login = '{login}'
    """
    results = execute_query(conn, query)
    return results

def is_personnel(conn, login):
    if len(get_personnel_details(conn, login)>0):
        return True 
    return False

def get_sanctions(conn, login):
    query = f"""
            SELECT * FROM SanctionDetails
            WHERE login = '{login}'
    """
    results = execute_query(conn, query)
    return results

def get_all_sanctions(conn):
    query = f"""
            SELECT * FROM SanctionDetails
    """
    results = execute_query(conn, query)
    return results
#####################################################################################

def get_auteurs_livre(conn, id_livre):
    query = f"""
            SELECT * FROM AuteurDetails
            WHERE id_livre = {id_livre}
    """
    results = execute_query(conn, query)
    return results

def get_interpretes_musique(conn, id_musique):
    query = f"""
            SELECT * FROM InterpreteDetails
            WHERE id_musique = {id_musique}
    """
    results = execute_query(conn, query)
    return results

def get_compositeurs_musique(conn, id_musique):
    query = f"""
            SELECT * FROM CompositeurDetails
            WHERE id_musique = {id_musique}
    """
    results = execute_query(conn, query)
    return results

def get_acteurs_film(conn, id_film):
    query = f"""
            SELECT * FROM ActeurDetails
            WHERE id_film = {id_film}
    """
    results = execute_query(conn, query)
    return results

def get_realisateurs_film(conn, id_film):
    query = f"""
            SELECT * FROM RealisateurDetails
            WHERE id_film = {id_film}
    """
    results = execute_query(conn, query)
    return results

def insert_exemplaire(conn, ressource, type):
    os.system('cls')
    etat = input("Etat de l'exemplaire 'Neuf', 'Bon', 'Abime', 'Perdu' : ")
    query = f"""INSERT INTO Exemplaire (id_ressource, etat, disponible)
            VALUES ('{ressource[0]}', '{etat}', true);"""
    execute_query(conn,query)
    display_exemplaires(conn, ressource, type)

def delete_exemplaire(conn, ressource, type):
    id = input("Id de l'exemplaire : ")
    query = f"""DELETE FROM Exemplaire WHERE id = {id}"""
    execute_query(conn,query)
    display_exemplaires(conn, ressource, type)

def update_exemplaire(conn, ressource, type):
    id = input("Id de l'exemplaire : ")
    etat = input("Etat de l'exemplaire 'Neuf', 'Bon', 'Abime', 'Perdu' : ")
    disponible = input("Disponible ? (true: disponible, false: non disponible) : ")
    query = f"""
    UPDATE Exemplaire
    SET etat = '{etat}', disponible = '{disponible}'
    WHERE id = '{id}';
    """
    execute_query(conn,query)
    display_exemplaires(conn, ressource, type)

def display_exemplaires(conn, ressource, type):
    os.system('cls')
    query = f"""
            SELECT * FROM Exemplaire
            WHERE id_ressource = {ressource[0]}
    """
    exemplaires = execute_query(conn, query)
    if len(exemplaires)>0:
        print("\nExemplaires :")
        for exemplaire in exemplaires:
            print("{:<10} {:<15} {:<15}".format(exemplaire[0], exemplaire[2], "disponible" if exemplaire[3] == 1 else "non disponible"))
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
    globals()[f'display_{type}'](conn, ressource)
    

def delete_ressource(conn, id_ressource):
    query = f"""
            DELETE FROM ressource WHERE id = {id_ressource};
    """
    _ = execute_query(conn, query)

def display_livre(conn,livre):
    os.system('cls')
    print(f"Titre: {livre[1]}")
    print(f"Date apparition: {livre[2]}")
    print(f"Editeur: {livre[3]}")
    print(f"Genre: {livre[4]}")
    print(f"Code de classification: {livre[5]}")
    print(f"ISBN: {livre[6]}")
    print(f"Résumé: {livre[7]}")
    print(f"Langue: {livre[8]}")
    auteurs = get_auteurs_livre(conn,livre[0])
    if len(auteurs)>0:
        print("\nAuteurs :")
        for auteur in auteurs:
            print("{:<10} {:<15} {} {:<15}".format(auteur[1], auteur[2], auteur[3], auteur[4]))
    print("\n")
    print("1. Modifier la ressource")
    print("2. Supprimer la ressource")
    print("3. Consulter les exemplaires")
    print("4. Retour")
    choice = int(input("Que voulez_vous faire ? : "))
    if choice ==2: 
        delete_ressource(conn, livre[0])
    elif choice ==1: 
        update_livre(conn, livre)
    elif choice ==3: 
        display_exemplaires(conn, livre,"livre")

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
            print("{:<10} {:<15} {} {:<15}".format(interprete[1], interprete[2], interprete[3], interprete[4]))
    compositeurs = get_compositeurs_musique(conn,musique[0])
    if len(compositeurs)>0:
        print("Compositeurs :")
        for compositeur in compositeurs:
            print("{:<10} {:<15} {} {:<15}".format(compositeur[1], compositeur[2], compositeur[3], compositeur[4]))
    print("\n")
    print("1. Modifier la ressource")
    print("2. Supprimer la ressource")
    print("3. Consulter les exemplaires")
    print("4. Retour")
    choice = int(input("Que voulez_vous faire ? : "))
    if choice ==2: 
        delete_ressource(conn, musique[0])
    elif choice ==1: 
        update_musique(conn, musique)
    elif choice ==3: 
        display_exemplaires(conn, musique, "musique")

def display_film(conn,film):
    os.system('cls')
    print(f"Titre: {film[1]}")
    print(f"Date apparition: {film[2]}")
    print(f"Editeur: {film[3]}")
    print(f"Genre: {film[4]}")
    print(f"Synopsis: {film[5]}")
    print(f"Code de classification: {film[6]}")
    print(f"Durée: {film[7]}")
    print(f"Langue: {film[8]}")
    acteurs = get_acteurs_film(conn,film[0])
    if len(acteurs)>0:
        print("\nActeurs :")
        for acteur in acteurs:
            print("{:<10} {:<15} {} {:<15}".format(acteur[1], acteur[2], acteur[3], acteur[4]))
    realisateurs = get_realisateurs_film(conn,film[0])
    if len(realisateurs)>0:
        print("Realisateurs :")
        for realisateur in realisateurs:
            print("{:<10} {:<15} {} {:<15}".format(realisateur[1], realisateur[2], realisateur[3], realisateur[4]))
    print("\n")
    print("1. Modifier la ressource")
    print("2. Supprimer la ressource")
    print("3. Consulter les exemplaires")
    print("4. Retour")
    choice = int(input("Que voulez_vous faire ? : "))
    if choice ==2: 
        delete_ressource(conn, film[0])
    elif choice ==1: 
        update_film(conn, film)
    elif choice ==3: 
        display_exemplaires(conn, film, "film")

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
        UPDATE Ressource
        SET titre = '{titre}', dateApparition = '{date}', editeur = '{editeur}', genre = '{genre}', codeClassification = '{code}'
        WHERE id = '{livre[0]}';
        """
        execute_query(conn,query1)
    except:
        print("\n")
    try:
        query2 = f"""
        UPDATE Livre
        SET resume = '{resume}', ISBN = '{isbn}', langue = '{langue}'
        WHERE id_livre = '{livre[0]}';
        """
        execute_query(conn,query2)
    except:
        print("\n")
    os.system('cls')
    auteurs = get_auteurs_livre(conn,livre[0])
    if len(auteurs)>0:
        print("\nAuteurs :")
        for auteur in auteurs:
            print("{:<10} {:<10} {:<15} {} {:<15}".format(auteur[5],auteur[1], auteur[2], auteur[3], auteur[4]))
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
    id = input("Id de l'auteur : ")
    query = f"""
        DELETE FROM Auteur
        WHERE id_contributeur = '{id}' AND id_livre = '{livre[0]}'
        """
    execute_query(conn,query)

def insert_auteur(conn, livre):
    nom = input("Nom de l'auteur: ")
    prenom = input("Prenom de l'auteur: ")
    date_naissance = input("Date de naissance: ")
    nationalite = input("Nationalité: ")
    query = f"""
        SELECT * FROM AuteurDetails
        WHERE nom = '{nom}' AND prenom = '{prenom}' AND datenaissance = '{date_naissance}' AND nationalite = '{nationalite}' AND id_livre = '{livre[0]}'
        """
    results = execute_query(conn,query)
    if len(results)==0:
        query = f"""
        SELECT * FROM Contributeur
        WHERE nom = '{nom}' AND prenom = '{prenom}' AND datenaissance = '{date_naissance}' AND nationalite = '{nationalite}'
        """
        results = execute_query(conn,query)
        if len(results)==0:
            query = f"""INSERT INTO Contributeur (prenom, nom, datenaissance,nationalite)
            VALUES ('{prenom}', '{nom}', '{date_naissance}', '{nationalite}');"""
            execute_query(conn,query)
            query = f"""
            SELECT * FROM Contributeur
            WHERE nom = '{nom}' AND prenom = '{prenom}' AND datenaissance = '{date_naissance}' AND nationalite = '{nationalite}'
            """
            results = execute_query(conn,query)
        query = f"""INSERT INTO Auteur (id_livre, id_contributeur)
        VALUES ('{livre[0]}', '{results[0][0]}');"""
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
        UPDATE Ressource
        SET titre = '{titre}', dateApparition = '{date}', editeur = '{editeur}', genre = '{genre}', codeClassification = '{code}'
        WHERE id = '{musique[0]}';
        """
        execute_query(conn,query1)
    except:
        print("\n")
    try:
        query2 = f"""
        UPDATE musique
        SET longueur = '{longueur}'
        WHERE id_musique = '{musique[0]}';
        """
        execute_query(conn,query2)
    except:
        print("\n")
    os.system('cls')
    interpretes = get_interpretes_musique(conn,musique[0])
    if len(interpretes)>0:
        print("\nInterpretes :")
        for interprete in interpretes:
            print("{:<10} {:<10} {:<15} {} {:<15}".format(interprete[5],interprete[1], interprete[2], interprete[3], interprete[4]))
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
            print("{:<10} {:<10} {:<15} {} {:<15}".format(compositeur[5],compositeur[1], compositeur[2], compositeur[3], compositeur[4]))
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
    id = input("Id du compositeur : ")
    query = f"""
        DELETE FROM Compositeur
        WHERE id_contributeur = '{id}' AND id_musique = '{musique[0]}'
        """
    execute_query(conn,query)

def insert_compositeur(conn, musique):
    nom = input("Nom du compositeur: ")
    prenom = input("Prenom du compositeur: ")
    date_naissance = input("Date de naissance: ")
    nationalite = input("Nationalité: ")
    query = f"""
        SELECT * FROM CompositeurDetails
        WHERE nom = '{nom}' AND prenom = '{prenom}' AND datenaissance = '{date_naissance}' AND nationalite = '{nationalite}' AND id_musique = '{musique[0]}'
        """
    results = execute_query(conn,query)
    if len(results)==0:
        query = f"""
        SELECT * FROM Contributeur
        WHERE nom = '{nom}' AND prenom = '{prenom}' AND datenaissance = '{date_naissance}' AND nationalite = '{nationalite}'
        """
        results = execute_query(conn,query)
        if len(results)==0:
            query = f"""INSERT INTO Contributeur (prenom, nom, datenaissance,nationalite)
            VALUES ('{prenom}', '{nom}', '{date_naissance}', '{nationalite}');"""
            execute_query(conn,query)
            query = f"""
            SELECT * FROM Contributeur
            WHERE nom = '{nom}' AND prenom = '{prenom}' AND datenaissance = '{date_naissance}' AND nationalite = '{nationalite}'
            """
            results = execute_query(conn,query)
        query = f"""INSERT INTO Compositeur (id_musique, id_contributeur)
        VALUES ('{musique[0]}', '{results[0][0]}');"""
        execute_query(conn,query)

def delete_interprete(conn, musique):
    id = input("Id de l'interprete : ")
    query = f"""
        DELETE FROM interprete
        WHERE id_contributeur = '{id}' AND id_musique = '{musique[0]}'
        """
    execute_query(conn,query)

def insert_interprete(conn, musique):
    nom = input("Nom de l'interprete: ")
    prenom = input("Prenom de l'interprete: ")
    date_naissance = input("Date de naissance: ")
    nationalite = input("Nationalité: ")
    query = f"""
        SELECT * FROM interpreteDetails
        WHERE nom = '{nom}' AND prenom = '{prenom}' AND datenaissance = '{date_naissance}' AND nationalite = '{nationalite}' AND id_musique = '{musique[0]}'
        """
    results = execute_query(conn,query)
    if len(results)==0:
        query = f"""
        SELECT * FROM Contributeur
        WHERE nom = '{nom}' AND prenom = '{prenom}' AND datenaissance = '{date_naissance}' AND nationalite = '{nationalite}'
        """
        results = execute_query(conn,query)
        if len(results)==0:
            query = f"""INSERT INTO Contributeur (prenom, nom, datenaissance,nationalite)
            VALUES ('{prenom}', '{nom}', '{date_naissance}', '{nationalite}');"""
            execute_query(conn,query)
            query = f"""
            SELECT * FROM Contributeur
            WHERE nom = '{nom}' AND prenom = '{prenom}' AND datenaissance = '{date_naissance}' AND nationalite = '{nationalite}'
            """
            results = execute_query(conn,query)
        query = f"""INSERT INTO interprete (id_musique, id_contributeur)
        VALUES ('{musique[0]}', '{results[0][0]}');"""
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
        SET titre = '{titre}', dateApparition = '{date}', editeur = '{editeur}', genre = '{genre}', codeClassification = '{code}'
        WHERE id = '{film[0]}';
        """
        execute_query(conn,query1)
    except:
        print("\n")
    try:
        query2 = f"""
        UPDATE film
        SET length = '{length}', langue = '{langue}', synopsis='{synopsis}'
        WHERE id_film = '{film[0]}';
        """
        execute_query(conn,query2)
    except:
        print("\n")
    os.system('cls')
    acteurs = get_acteurs_film(conn,film[0])
    if len(acteurs)>0:
        print("\nActeurs :")
        for acteur in acteurs:
            print("{:<10} {:<10} {:<15} {} {:<15}".format(acteur[5],acteur[1], acteur[2], acteur[3], acteur[4]))
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
            print("{:<10} {:<10} {:<15} {} {:<15}".format(realisateur[5],realisateur[1], realisateur[2], realisateur[3], realisateur[4]))
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
    id = input("Id de l'acteur : ")
    query = f"""
        DELETE FROM Acteur
        WHERE id_contributeur = '{id}' AND id_film = '{film[0]}'
        """
    execute_query(conn,query)

def insert_acteur(conn, film):
    nom = input("Nom de l'acteur: ")
    prenom = input("Prenom de l'acteur: ")
    date_naissance = input("Date de naissance: ")
    nationalite = input("Nationalité: ")
    query = f"""
        SELECT * FROM ActeurDetails
        WHERE nom = '{nom}' AND prenom = '{prenom}' AND datenaissance = '{date_naissance}' AND nationalite = '{nationalite}' AND id_film = '{film[0]}'
        """
    results = execute_query(conn,query)
    if len(results)==0:
        query = f"""
        SELECT * FROM Contributeur
        WHERE nom = '{nom}' AND prenom = '{prenom}' AND datenaissance = '{date_naissance}' AND nationalite = '{nationalite}'
        """
        results = execute_query(conn,query)
        if len(results)==0:
            query = f"""INSERT INTO Contributeur (prenom, nom, datenaissance,nationalite)
            VALUES ('{prenom}', '{nom}', '{date_naissance}', '{nationalite}');"""
            execute_query(conn,query)
            query = f"""
            SELECT * FROM Contributeur
            WHERE nom = '{nom}' AND prenom = '{prenom}' AND datenaissance = '{date_naissance}' AND nationalite = '{nationalite}'
            """
            results = execute_query(conn,query)
        query = f"""INSERT INTO Acteur (id_film, id_contributeur)
        VALUES ('{film[0]}', '{results[0][0]}');"""
        execute_query(conn,query)

def delete_realisateur(conn, film):
    id = input("Id du realisateur : ")
    query = f"""
        DELETE FROM realisateur
        WHERE id_contributeur = '{id}' AND id_film = '{film[0]}'
        """
    execute_query(conn,query)

def insert_realisateur(conn, film):
    nom = input("Nom du realisateur: ")
    prenom = input("Prenom du realisateur: ")
    date_naissance = input("Date de naissance: ")
    nationalite = input("Nationalité: ")
    query = f"""
        SELECT * FROM realisateurDetails
        WHERE nom = '{nom}' AND prenom = '{prenom}' AND datenaissance = '{date_naissance}' AND nationalite = '{nationalite}' AND id_film = '{film[0]}'
        """
    results = execute_query(conn,query)
    if len(results)==0:
        query = f"""
        SELECT * FROM Contributeur
        WHERE nom = '{nom}' AND prenom = '{prenom}' AND datenaissance = '{date_naissance}' AND nationalite = '{nationalite}'
        """
        results = execute_query(conn,query)
        if len(results)==0:
            query = f"""INSERT INTO Contributeur (prenom, nom, datenaissance,nationalite)
            VALUES ('{prenom}', '{nom}', '{date_naissance}', '{nationalite}');"""
            execute_query(conn,query)
            query = f"""
            SELECT * FROM Contributeur
            WHERE nom = '{nom}' AND prenom = '{prenom}' AND datenaissance = '{date_naissance}' AND nationalite = '{nationalite}'
            """
            results = execute_query(conn,query)
        query = f"""INSERT INTO realisateur (id_film, id_contributeur)
        VALUES ('{film[0]}', '{results[0][0]}');"""
        execute_query(conn,query)