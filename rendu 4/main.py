import os
import psycopg2
from constants import POSTGRES_DB, POSTGRES_HOST, POSTGRES_PASSWORD, POSTGRES_PORT, POSTGRES_USER, ADMIN_PASSWORD

from helpers import display_prêts, get_film_ressources, get_musique_ressources, get_livre_ressources, display_livre, display_musique, display_film, get_prets_en_cours_from_login, handle_utilisateurs, choose_table, insert_prêt

# Search
def option_1(conn):
    os.system('cls')
    title = input("Entrez le titre de la ressource: ")
    os.system('cls')

    films = get_film_ressources(conn, title)
    musiques = get_musique_ressources(conn, title)
    livres = get_livre_ressources(conn, title)
    print("Livres")
    print("{:<10} {:<15} {:<50} {:<15}".format("Index", "Titre", "Résumé", "Langue"))
    print("=" * 90)
    for index, row in enumerate(livres):
        print("{:<10} {:<15} {:<50} {:<15}".format(index, row[1], row[7], row[8]))
    print("=" * 90)
    print("\n")
    print("Films")
    print("{:<10} {:<15} {:<50} {:<10}".format("Index", "Titre", "Synopsis", "Langue"))
    print("=" * 90)
    for index, row in enumerate(films):
        print("{:<10} {:<15} {:<50} {:<10}".format(index+len(livres), row[1], row[5], row[8]))
    print("=" * 90)
    print("\n")
    print("Musiques")
    print("{:<10} {:<15} {:<50} {:<10}".format("Index", "Titre", "Editeur", "Longueur"))
    print("=" * 90)
    for index, row in enumerate(musiques):
        print("{:<10} {:<15} {:<50} {:<10}".format(index+len(musiques)+len(livres), row[1], row[3], row[6]))
    print("=" * 90)
    choice = int(input("Index de la ressource à consulter (-1 pour retour): "))
    if choice in range(-1, len(films)+len(musiques)+len(livres)):
            if choice != -1:
                if choice < len(livres):
                    display_livre(conn,livres[choice])
                elif choice >= len(livres) + len(films):
                    display_musique(conn,musiques[choice-len(livres)-len(films)])
                else:
                    display_film(conn,films[choice-len(livres)])

    os.system('cls')

# Handle prêts
def option_3(conn):
    os.system('cls')
    login = input("Entrez un login: ")
    os.system('cls')
    prêts = get_prets_en_cours_from_login(conn, login)
    print(f"Prêts en cours des logins commençant par {login}")
    print("{:5} {} {:<5} {} {:<15} {:<15} {:<15} {:<15}".format("Index","Date prêt", "Durée", "Date retour", "Titre","Prenom", "Nom", "Login"))
    print("=" * 90)
    for index, row in enumerate(prêts):
        print("{:5} {} {:<5} {} {:<15} {:<15} {:<15} {:<15}".format(index, row[1], row[2], row[3],row[15],row[9],row[10], row[8]))
    print("=" * 90)
    print("\n")
    print("1. Ajouter un nouveau prêt")
    print("2. Gérer un prêt")
    print("3. Retour")
    choice = int(input("Que voulez_vous faire ? : "))
    if choice ==2: 
        index = int(input("Index du prêt à modifier (-1 retour) : "))
        display_prêts(conn,prêts[index])
    elif choice ==1: 
        insert_prêt(conn)


# Insert ressources
def option_2(conn):
    choose_table(conn)

# Handle sanctions
def option_4(conn):
    print("A implementer")

# Handle utilisateurs
def option_5(conn):
    handle_utilisateurs(conn)

# Visualiser les tables
def option_6(conn):
    os.system('cls')
    mot_de_passe = input("Entrez le mot de passe : ")
    if mot_de_passe != ADMIN_PASSWORD:
        print("Mot de passe incorrect !")
        return
    try:
        sql = """SELECT table_name FROM information_schema.tables WHERE table_schema = 'public' AND table_type = 'BASE TABLE';"""
        cur = conn.cursor()
        cur.execute(sql)
        tables = cur.fetchall()

        if not tables:
            print("Aucune table trouvée.")
            return

        print("Voici les tables :")
        for i, table in enumerate(tables, start=1):
            print(f"{i}. {table[0]}")

    except Exception as e:
        print(f"Erreur lors de la visualisation des tables : {e}")
        print("Veuillez réessayer.")
        conn.rollback()
    
    # Demander à l'utilisateur s'il veut voir le contenu d'une table
    while True:
        choice = input("Choisissez une table pour voir son contenu (0 pour retour) : ")
        if choice == '0':
            return
        elif choice in [str(i) for i in range(1, len(tables)+1)]:
            try:
                sql = f"""SELECT * FROM {tables[int(choice)-1][0]};"""
                cur = conn.cursor()
                cur.execute(sql)
                rows = cur.fetchall()
                
                if not rows:
                    print(f"Aucune donnée trouvée dans la table {tables[int(choice)-1][0]}.")
                    return

                print(f"\nVoici le contenu de la table {tables[int(choice)-1][0]} :")
                print("=" * 40)

                # Exibindo cabeçalho
                header = [desc[0] for desc in cur.description]
                print(" | ".join(header))
                print("-" * 40)

                # Exibindo dados
                for i, row in enumerate(rows, start=1):
                    print(f"{row}")

                print("=" * 40)

            except Exception as e:
                print(f"Erreur lors de la visualisation du contenu de la table : {e}")
                print("Veuillez réessayer.")
                conn.rollback()
        else:
            print("Choix invalide. Veuillez réessayer.")
        
    
# Create a new table
def option_7(conn):
    os.system('cls')
    # Il faut que l'utilisateur soit un administrateur
    mot_de_passe = input("Entrez le mot de passe : ")
    if mot_de_passe != ADMIN_PASSWORD:
        print("Mot de passe incorrect !")
        return
    
    while True:
        nom_table = input("Entrez le nom de la table : ")
        if nom_table == "":
            print("Le nom de la table ne peut pas être vide !")
            continue
        else:
            break

    sql = f"""CREATE TABLE {nom_table} ();"""

    try:
        cur = conn.cursor()
        cur.execute(sql)
        conn.commit()
    
    except Exception as e:
        print("Erreur lors de la création de la table! avec le message suivant: ", end='')
        print(e, end='')
        print("Veuillez réessayer.")
        conn.rollback()
        return
    
    while True:
        nom_colonne = input("Entrez le nom de la colonne : ")
        if nom_colonne == "":
            print("Le nom de la colonne ne peut pas être vide !")
            continue
        # Type de la colonne en sql
        print("Choisissez le type de la colonne :   ")
        print("1. VARCHAR")
        print("2. INT")
        print("3. DATE")
        print("4. FLOAT")
        print("5. BOOLEAN")
        
        while True:
            type_colonne = input("Entrez votre choix : ")
            if type_colonne == '1':
                type_colonne = input("Choisissez le nombre de caractères : ")
                type_colonne = f"VARCHAR({type_colonne})"
                break

            elif type_colonne == '2':
                type_colonne = "INT"
                break

            elif type_colonne == '3':
                type_colonne = "DATE"
                break

            elif type_colonne == '4':
                type_colonne = "FLOAT"
                break

            elif type_colonne == '5':
                type_colonne = "BOOLEAN"
                break

            else:
                print("Choix invalide. Veuillez réessayer.")
                continue
        
        while True:
            primary_key = input("Est-ce que c'est une clé primaire ? (O/N) : ")
            if primary_key in ('O', 'o','N', 'n'):
                break
            else:
                print("Choix invalide. Veuillez réessayer.")
                continue
        
        constraint = input("Ecrit le constrait s'il y a: (EX: NOT NULL, UNIQUE, AUTO INCREMENT)?:")

        # Inserto into table
        if primary_key == 'O' or primary_key == 'o':
            sql = f"""ALTER TABLE {nom_table} ADD COLUMN {nom_colonne} {type_colonne} PRIMARY KEY;"""
        elif constraint != None:
            sql = f"""ALTER TABLE {nom_table} ADD COLUMN {nom_colonne} {type_colonne} {constraint};"""
        else:
            sql = f"""ALTER TABLE {nom_table} ADD COLUMN {nom_colonne} {type_colonne};"""
        
        try:
            cur = conn.cursor()
            cur.execute(sql)
            conn.commit()
        except Exception as e:
            print(e, end='')
            print("Erreur lors de l'ajout de la colonne !")
            print("Veuillez réessayer.")
            conn.rollback()

        input_user = input("Voulez-vous ajouter une autre colonne ? (O/N) : ")
        if input_user == 'N' or input_user == 'n':
            print("La table a été créée avec succès !")
            break
        elif input_user == 'O' or input_user == 'o':
            continue
        else:
            print("Choix invalide. Veuillez réessayer.")
            
#Supprimer une table
def option_8(conn):
    os.system('cls')
    mot_de_passe = input("Entrez le mot de passe : ")
    if mot_de_passe != ADMIN_PASSWORD:
        print("Mot de passe incorrect !")
        return
    
    try:
        os.system('cls')
        sql = """SELECT table_name FROM information_schema.tables WHERE table_schema = 'public' AND table_type = 'BASE TABLE';"""
        cur = conn.cursor()
        cur.execute(sql)
        tables = cur.fetchall()

        if not tables:
            print("Il n'y a aucune table à supprimer.")
            return

        print("Voici les tables :")
        for i, table in enumerate(tables, start=1):
            print(f"{i}. {table[0]}")

    except Exception as e:
        print(f"Erreur lors de la visualisation des tables : {e}")
        print("Veuillez réessayer.")
        conn.rollback()
    
    # Demander à l'utilisateur s'il veut voir le contenu d'une table
    while True:
        choice = input("Choisissez une table pour la supprimer (0 pour retour) : ")
        if choice == '0':
            return
        elif choice in [str(i) for i in range(1, len(tables)+1)]:
            try:
                sql = f"""DROP TABLE {tables[int(choice)-1][0]};"""
                cur = conn.cursor()
                cur.execute(sql)
                conn.commit()
                print("La table a été supprimée avec succès !")
                break
            except Exception as e:
                print(e, end='')
                print("Erreur lors de la suppression de la table")
                print("Veuillez réessayer.")
                conn.rollback()
        else:
            print("Choix invalide. Veuillez réessayer.")
            
        
def afficher_menu():
    #os.system("cls")
    print("\n=============== Menu ===============")
    print("1. Recherche Livre / Musique / Film")
    print("2. Ajouter Livre / Musique / Film")
    print("3. Gérer les prêts")
    print("4. Gérer les sanctions (à implémenter)")
    print("5. Gérer les utilisateurs")
    print("6. Visualiser les tables (Administrateur)")
    print("7. Créer une nouvelle table (Administrateur)")
    print("8. Supprimer une table (Administrateur) ")
    print("9. Quitter")
    print("=============================================")

def choisir_option(conn):
    while True:
        afficher_menu()
        choice = input("Quel opération voulez-vous effectuer ? ")
        if choice in ('1', '2', '3', '4','5', '6', '7', '8', '9'):
            if choice == '9':
                print("Au revoir !")
                break
            globals()[f'option_{choice}'](conn)

        else:
            print("Choix invalide. Veuillez réessayer.")
    
def connect():
    conn = None
    try:
        # read connection parameters
        params = {
            'host': POSTGRES_HOST,
            'database': POSTGRES_DB,
            'user': POSTGRES_USER,
            'password': POSTGRES_PASSWORD,
            'port': POSTGRES_PORT
        }
        conn = psycopg2.connect(**params)
        return conn
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

def disconnect(conn):
    if conn is not None:
        conn.close()
        print('Database connection closed.')

def main():
    conn = connect()
    choisir_option(conn)
    disconnect(conn)
    

if __name__ == '__main__':
    main()
