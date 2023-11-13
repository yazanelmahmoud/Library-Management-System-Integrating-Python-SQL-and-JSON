INSERT INTO Ressource (id, titre, dateApparition, editeur, genre, codeClassification)
VALUES
    (1, 'Book 1', '2023-01-01', 'Publisher A', 'Fiction', 101),
    (2, 'Book 2', '2023-01-01', 'Publisher A', 'Fiction', 102),
    (3, 'Music 1', '2023-02-01', 'Music Label A', 'Pop', 103),
    (4, 'Film 1', '2023-03-01', 'Studio A', 'Action', 104);

INSERT INTO Livre (id_livre, ISBN, resume, langue)
VALUES
    (1, 'ISBN-1', 'Book 1 Summary', 'English'),
    (2, 'ISBN-2', 'Book 2 Summary', 'French');

INSERT INTO Musique (id_musique, longueur)
VALUES
    (3, 180);

INSERT INTO Film (id_film, langue, length, synopsis)
VALUES
    (4, 'English', 120, 'Film 1 Synopsis');

INSERT INTO Contributeur (id, prenom, nom, dateNaissance, nationalite)
VALUES
    (1, 'John', 'Doe', '1990-05-15', 'American'),
    (2, 'Jane', 'Smith', '1985-12-10', 'French');

INSERT INTO Auteur (id_livre, id_contributeur)
VALUES
    (1, 1),
    (2, 2);

INSERT INTO Interprete (id_musique, id_contributeur)
VALUES
    (3, 2),
    (3, 1);

INSERT INTO Compositeur (id_musique, id_contributeur)
VALUES
    (3, 2),
    (3, 1);

INSERT INTO Acteur (id_film, id_contributeur)
VALUES
    (4, 2),
    (4, 1);

INSERT INTO Realisateur (id_film, id_contributeur)
VALUES
    (4, 2),
    (4, 1);

INSERT INTO Exemplaire (id, id_ressource, etat, disponible)
VALUES
    (1, 1, 'Neuf', true),
    (2, 1,'Bon', true),
    (3, 2,'Bon', false),
    (4, 3,'Abimé', false),
    (5, 4,'Bon', false);

INSERT INTO Adresse (id, rue, numero, codePostal, ville)
VALUES
    (1, '123 Main St', 45, 12345, 'City A'),
    (2, '456 Elm St', 67, 67890, 'City B');

INSERT INTO Utilisateur (id, login, password, prenom, nom, email, adresse)
VALUES
    (1, 'user1', 'password1', 'User', 'One', 'user1@example.com', 1),
    (2, 'user2', 'password2', 'User', 'Two', 'user2@example.com', 2);

INSERT INTO Personnel (id, id_personnel)
VALUES
    (1, 2),
    (2, 1);

INSERT INTO Adherent (id, numeroTelephone, dateNaissance, statut)
VALUES
    (1, '123-456-7890', '1990-07-20', 'active'),
    (2, '987-654-3210', '1985-04-15', 'expiré');

INSERT INTO Pret (id, id_exemplaire, id_adherent, id_responsable, datePret, duree, dateRetour, etatRetour)
VALUES
    (1, 1, 1, 2, '2023-01-10', 14, '2023-01-24', 'bon'),
    (2, 2, 2, 1, '2023-02-15', 7, '2023-02-22', 'neuf');

INSERT INTO Sanction (id_sanction, DateSanction, DateFinSanction, motif, montant)
VALUES
    (1, '2023-01-25', '2023-02-25', 'Retard', 10.00),
    (2, '2023-02-23', '2023-03-23', 'Détérioration', 15.00);

INSERT INTO Ressource (id, titre, dateApparition, editeur, genre, codeClassification)
VALUES
    (5, 'Book 3', '2023-04-01', 'Publisher B', 'Mystery', 105),
    (6, 'Music 2', '2023-05-01', 'Music Label B', 'Rock', 106),
    (7, 'Film 2', '2023-06-01', 'Studio B', 'Comedy', 107),
    (8, 'Magazine 1', '2023-07-01', 'Magazine Corp', 'Magazine', 108),
    (9, 'Book 4', '2023-08-01', 'Publisher C', 'Thriller', 109);

-- Livres
INSERT INTO Livre (id_livre, ISBN, resume, langue)
VALUES
    (3, 'ISBN-3', 'Book 3 Summary', 'Spanish'),
    (4, 'ISBN-4', 'Book 4 Summary', 'German'),
    (5, 'ISBN-5', 'Book 5 Summary', 'English');

-- Musiques
INSERT INTO Musique (id_musique, longueur)
VALUES
    (4, 200),
    (5, 150),
    (6, 220);

-- Films
INSERT INTO Film (id_film, langue, length, synopsis)
VALUES
    (5, 'French', 110, 'Film 2 Synopsis'),
    (6, 'German', 130, 'Film 3 Synopsis'),
    (7, 'Spanish', 95, 'Film 4 Synopsis');

-- Contributeurs
INSERT INTO Contributeur (id, prenom, nom, dateNaissance, nationalite)
VALUES
    (3, 'Alice', 'Johnson', '1988-08-25', 'British'),
    (4, 'Carlos', 'Rodriguez', '1995-03-12', 'Spanish'),
    (5, 'Eva', 'Martinez', '1992-12-01', 'Mexican');

-- Auteurs
INSERT INTO Auteur (id_livre, id_contributeur)
VALUES
    (3, 3),
    (4, 4),
    (5, 5);

-- Interprètes
INSERT INTO Interprete (id_musique, id_contributeur)
VALUES
    (4, 4),
    (5, 3),
    (6, 5);

-- Compositeurs
INSERT INTO Compositeur (id_musique, id_contributeur)
VALUES
    (5, 5),
    (6, 3),
    (7, 4);

-- Acteurs
INSERT INTO Acteur (id_film, id_contributeur)
VALUES
    (5, 4),
    (6, 3),
    (7, 5);

-- Réalisateurs
INSERT INTO Realisateur (id_film, id_contributeur)
VALUES
    (6, 3),
    (7, 4),
    (8, 5);

-- Exemplaires
INSERT INTO Exemplaire (id, id_ressource, etat, disponible)
VALUES
    (6, 3, 'Neuf', true),
    (7, 4, 'Bon', true),
    (8, 5, 'Abimé', false),
    (9, 6, 'Bon', false),
    (10, 6, 'Neuf', true);

-- Adresses
INSERT INTO Adresse (id, rue, numero, codePostal, ville)
VALUES
    (3, '789 Oak St', 89, 34567, 'City C'),
    (4, '101 Pine St', 12, 45678, 'City D'),
    (5, '567 Maple St', 34, 56789, 'City E');

-- Utilisateurs
INSERT INTO Utilisateur (id, login, password, prenom, nom, email, adresse)
VALUES
    (3, 'user3', 'password3', 'User', 'Three', 'user3@example.com', 3),
    (4, 'user4', 'password4', 'User', 'Four', 'user4@example.com', 4),
    (5, 'user5', 'password5', 'User', 'Five', 'user5@example.com', 5);

-- Personnels
INSERT INTO Personnel (id, id_personnel)
VALUES
    (3, 3),
    (4, 4),
    (5, 5);

-- Adhérents
INSERT INTO Adherent (id, numeroTelephone, dateNaissance, statut)
VALUES
    (3, '111-222-3333', '1987-06-18', 'active'),
    (4, '444-555-6666', '1992-11-30', 'active'),
    (5, '777-888-9999', '1998-04-05', 'expiré');

-- Prêts
INSERT INTO Pret (id, id_exemplaire, id_adherent, id_responsable, datePret, duree, dateRetour, etatRetour)
VALUES
    (5, 5, 5, 4, '2023-05-05', 10, '2023-05-15', 'bon'),
    (6, 6, 6, 3, '2023-06-12', 7, '2023-06-19', 'neuf'),
    (7, 7, 7, 5, '2023-07-18', 14, '2023-08-01', 'bon');

-- Sanctions
INSERT INTO Sanction (id_sanction, DateSanction, DateFinSanction, motif, montant)
VALUES
    (5, '2023-05-20', '2023-06-20', 'Retard', 8.00),
    (6, '2023-06-18', '2023-07-18', 'Détérioration', 12.00);


