INSERT INTO Ressource (id, titre, dateApparition, editeur, genre, codeClassification)
VALUES
    (1, 'Book 1', '2023-01-01', 'Publisher A', 'Fiction', 101),
    (2, 'Music 1', '2023-02-01', 'Music Label A', 'Pop', 102),
    (3, 'Film 1', '2023-03-01', 'Studio A', 'Action', 103);

INSERT INTO Livre (id_livre, ISBN, resume, langue)
VALUES
    (1, 'ISBN-1', 'Book 1 Summary', 'English'),
    (2, 'ISBN-2', 'Book 2 Summary', 'French');

INSERT INTO Musique (id_musique, longueur)
VALUES
    (1, 180),
    (2, 240);

INSERT INTO Film (id_film, langue, length, synopsis)
VALUES
    (1, 'English', 120, 'Film 1 Synopsis'),
    (2, 'French', 150, 'Film 2 Synopsis');

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
    (1, 2),
    (2, 1);

INSERT INTO Compositeur (id_musique, id_contributeur)
VALUES
    (1, 1),
    (2, 2);

INSERT INTO Acteur (id_film, id_contributeur)
VALUES
    (1, 1),
    (2, 2);

INSERT INTO Realisateur (id_film, id_contributeur)
VALUES
    (1, 2),
    (2, 1);

INSERT INTO Exemplaire (id, etat, disponible)
VALUES
    (1, 'Neuf', true),
    (2, 'Bon', true),
    (3, 'Abimé', false);

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
