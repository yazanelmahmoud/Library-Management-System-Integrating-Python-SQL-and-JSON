import os
import psycopg2

from insert import choose_table
from helpers import get_film_ressources, get_musique_ressources, get_livre_ressources, display_livre, display_musique, display_film, create_tables

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
    print("A implementer")

# Insert ressources
def option_2(conn):
    choose_table(conn)

# Handle sanctions
def option_4(conn):
    print("A implementer")

# Handle utilisateurs
def option_5(conn):
    print("A implementer")

# Create a new table
def option_6(conn):
    nom_table = input("Entrez le nom de la table : ")
    sql = f"""CREATE TABLE {nom_table} ();"""
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()
    
    while True:
        nom_colonne = input("Entrez le nom de la colonne : ")
        type_colonne = input("Entrez le type de la colonne :\n  ")
        primary_key = input("Est-ce que c'est une clé primaire ? (O/N) : ")
        constraint = input("Ecrit le constrait s'il y a: (EX: NOT NULL, UNIQUE, AUTO INCREMENT)?:")

        # Inserto into table
        if primary_key == 'O':
            sql = f"""ALTER TABLE {nom_table} ADD COLUMN {nom_colonne} {type_colonne} PRIMARY KEY;"""
        elif constraint != 'NULL':
            sql = f"""ALTER TABLE {nom_table} ADD COLUMN {nom_colonne} {type_colonne} {constraint};"""
        else:
            sql = f"""ALTER TABLE {nom_table} ADD COLUMN {nom_colonne} {type_colonne} 
            ;"""
        cur = conn.cursor()
        cur.execute(sql)
        conn.commit()
        
        input_user = input("Voulez-vous ajouter une autre colonne ? (O/N) : ")
        if input_user == 'N':
            print("La table a été créée avec succès !")
            break

def afficher_menu():
    print("\n=============== Menu ===============")
    print("1. Recherche Livre / Musique / Film")
    print("2. Ajouter Livre / Musique / Film")
    print("3. Gérer les prêts (à implémenter)")
    print("4. Gérer les sanctions (à implémenter)")
    print("5. Gérer les utilisateurs (à implémenter)")
    print("6. Créer une nouvelle table (à implémenter)")
    print("7. Visualiser les tables (à implémenter)")
    print("8. Quitter")
    print("===============================")

def choisir_option(conn):
    while True:
        afficher_menu()
        choice = input("Quel opération voulez-vous effectuer ? ")
        if choice in ('1', '2', '3', '4','5', '6', '7', '8'):
            if choice == '8':
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
            'host': 'localhost',
            'database': 'bibliotheque',
            'user': 'postgres',
            'password': 'postgres',
            'port': '5432'
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
