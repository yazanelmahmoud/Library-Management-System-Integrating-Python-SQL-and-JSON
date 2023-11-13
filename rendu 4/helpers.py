import psycopg2

def connect_to_db(name):
    conn = psycopg2.connect(database = name, 
                        user = "postgres", 
                        host= 'localhost',
                        password = "postgres",
                        port = 5432)
    return conn

def execute_query(db_name, query):
    conn = connect_to_db(db_name)
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
    conn.close()

def execute_sql_file(db_name, filename):
    conn = connect_to_db(db_name)
    # Create a cursor object to execute SQL statements
    cursor = conn.cursor()

    # Read the SQL file
    with open(filename, 'r') as file:
        sql_script = file.read()

    # Execute the SQL script
    cursor.execute(sql_script)

    # Commit the changes and close the connection
    conn.commit()
    conn.close()

def create_tables(db_name):
    execute_sql_file(db_name, "../rendu 3/CreateDB.session.sql")
    execute_sql_file(db_name, "../rendu 3/InsertDB.session.sql")

def get_prets_from_login(login):
    query = f"""
            SELECT * FROM PretDetails
            WHERE login = '{login}'
    """
    results = execute_query("bibliotheque", query)
    return results

def get_film_exemplaires(titre):
    query = f"""
            SELECT * FROM FilmExemplaires
            WHERE titre_film LIKE '{titre}%'
    """
    results = execute_query("bibliotheque", query)
    return results

def get_film_exemplaires_disponibles(titre):
    query = f"""
            SELECT titre_film, COUNT(titre_film) FROM FilmExemplaires
            WHERE titre_film LIKE '{titre}%' AND disponible = 'true'
            GROUP BY titre_film
    """
    results = execute_query("bibliotheque", query)
    return results

def get_film_ressources(titre):
    query = f"""
            SELECT * FROM FilmDetails
            WHERE titre_film LIKE '{titre}%'
    """
    results = execute_query("bibliotheque", query)
    return results

def get_musique_exemplaires(titre):
    query = f"""
            SELECT * FROM MusiqueExemplaires
            WHERE titre_musique LIKE '{titre}%'
    """
    results = execute_query("bibliotheque", query)
    return results

def get_musique_exemplaires_disponibles(titre):
    query = f"""
            SELECT titre_musique, COUNT(titre_musique) FROM MusiqueExemplaires
            WHERE titre_musique LIKE '{titre}%' AND disponible = 'true'
            GROUP BY titre_musique
    """
    results = execute_query("bibliotheque", query)
    return results

def get_musique_ressources(titre):
    query = f"""
            SELECT * FROM MusiqueDetails
            WHERE titre_musique LIKE '{titre}%'
    """
    results = execute_query("bibliotheque", query)
    return results

def get_livre_exemplaires(titre):
    query = f"""
            SELECT * FROM LivreExemplaires
            WHERE titre_livre LIKE '{titre}%'
    """
    results = execute_query("bibliotheque", query)
    return results

def get_livre_exemplaires_disponibles(titre):
    query = f"""
            SELECT titre_livre, COUNT(titre_livre) FROM LivreExemplaires
            WHERE titre_livre LIKE '{titre}%' AND disponible = 'true'
            GROUP BY titre_livre
    """
    results = execute_query("bibliotheque", query)
    return results

def get_livre_ressources(titre):
    query = f"""
            SELECT * FROM LivreDetails
            WHERE titre_livre LIKE '{titre}%'
    """
    results = execute_query("bibliotheque", query)
    return results

def get_adherent_details(login):
    query = f"""
            SELECT * FROM AdherentDetails
            WHERE login = '{login}'
    """
    results = execute_query("bibliotheque", query)
    return results   

def get_personnel_details(login):
    query = f"""
            SELECT * FROM PersonnelDetails
            WHERE login = '{login}'
    """
    results = execute_query("bibliotheque", query)
    return results

def is_personnel(login):
    if len(get_personnel_details(login)>0):
        return True 
    return False

def get_sanctions(login):
    query = f"""
            SELECT * FROM SanctionDetails
            WHERE login = '{login}'
    """
    results = execute_query("bibliotheque", query)
    return results

def get_all_sanctions():
    query = f"""
            SELECT * FROM SanctionDetails
    """
    results = execute_query("bibliotheque", query)
    return results

def main():
    # create_tables("bibliotheque")
    print("Bienvenue à la bibliothèque")
    print("Prêts user1")
    for pret in get_prets_from_login("user1"):
        print(pret)
    print("Films Exemplaires")
    for pret in get_film_exemplaires("Film"):
        print(pret)
    print("Musiques Exemplaires")
    for pret in get_musique_exemplaires("Music"):
        print(pret)
    print("Livres Exemplaires")
    for pret in get_livre_exemplaires("Book"):
        print(pret)
    print("Films Ressources")
    for pret in get_film_ressources("Film"):
        print(pret)
    print("Musique Ressources")
    for pret in get_musique_ressources("Music"):
        print(pret)
    print("Livre Ressources")
    for pret in get_livre_ressources("Book"):
        print(pret)
    print("Films avec exemplaires disponibles")
    for pret in get_film_exemplaires_disponibles("Film"):
        print(pret)
    print("Livres avec exemplaires disponibles")
    for pret in get_livre_exemplaires_disponibles("Book"):
        print(pret)
    print("Musiques avec exemplaires disponibles")
    for pret in get_musique_exemplaires_disponibles("Music"):
        print(pret)
    print("Adhérents détails")
    for pret in get_adherent_details("user1"):
        print(pret)
    print("Personnel détails")
    for pret in get_personnel_details("user1"):
        print(pret)
    print("Sanctions détails user2")
    for pret in get_sanctions("user2"):
        print(pret)
    print("All Sanctions détails")
    for pret in get_all_sanctions():
        print(pret)
main()