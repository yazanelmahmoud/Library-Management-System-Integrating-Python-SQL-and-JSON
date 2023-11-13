import psycopg2
import sys
import os

# select_all_books
def option_1(conn):
    """ Query all rows in the books table """
    cur = conn.cursor()
    cur.execute("SELECT id_livre, isbn, resume, langue FROM livre")
    rows = cur.fetchall()

    print("{:<10} {:<15} {:<50} {:<10}".format("ID Livre", "ISBN", "resume", "langue"))
    print("=" * 90)

    for row in rows:
        print("{:<10} {:<15} {:<50} {:<10}".format(row[0], row[1], row[2], row[3]))

# select_specific_book
def option_2(conn):
    book_id = input("Entrez l'ID du livre : ")
    """ Query all rows in the books table """
    cur = conn.cursor()
    cur.execute("SELECT * FROM books WHERE id = %s", (book_id,))
    rows = cur.fetchall()

    for row in rows:
        print(row)

# insert_book
def option_3(conn):
    title = input("Entrez le titre du livre : ")
    author = input("Entrez l'auteur du livre : ")
    year = input("Entrez l'année du livre : ")
    book = (title, author, year)
    
    """ insert a new book into the books table """
    sql = """INSERT INTO books(title, author, year)
             VALUES(%s, %s, %s) RETURNING id;"""
    cur = conn.cursor()
    cur.execute(sql, book)
    conn.commit()
    book_id = cur.fetchone()[0]
    print(book_id)
    return book_id

# Create a new table
def option_4(conn):
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
    print("1. Afficher tous les livres")
    print("2. Afficher un livre spécifique")
    print("3. Ajouter un livre")
    print("4. Créer une nouvelle table")
    print("5. Quitter")
    print("===============================")

def choisir_option(conn):
    while True:
        afficher_menu()
        choice = input("Quel opération voulez-vous effectuer ? ")
        if choice in ('1', '2', '3', '4','5'):
            if choice == '5':
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
            'password': 'dev',
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
