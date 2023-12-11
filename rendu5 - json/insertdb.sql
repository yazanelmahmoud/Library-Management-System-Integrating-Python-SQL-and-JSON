-- Ajout des Utilisateurs
INSERT INTO Utilisateur (id, login, password, prenom, nom, email, adresse)
VALUES (1, 'utilisateur1', 'mdp123', 'Jean', 'Dupont', 'jean@example.com', '{"rue": "Rue de la Paix", "numero": 10, "codePostal": "75001", "ville": "Paris"}');

INSERT INTO Utilisateur (id, login, password, prenom, nom, email, adresse)
VALUES (2,'utilisateur2', 'secret456', 'Alice', 'Lefevre', 'alice@example.com', '{"rue": "Avenue des Roses", "numero": 25, "codePostal": "69002", "ville": "Lyon"}');

-- Ajout des Adherents qui sont des Utilisateurs
INSERT INTO Adherent (id, numeroTelephone, dateNaissance, statut)
VALUES (1, '0123456789', '1990-05-15', 'active');

-- Après avoir ajouté les utilisateurs, vous pouvez insérer les autres données
INSERT INTO Ressource (id, titre, dateApparition, editeur, genre, codeClassification, contributeur)
VALUES (1, 'Titre du livre', '2023-01-15', 'Éditeur ABC', 'Fiction', 123, '{"prenomAuteur": "Paul", "nomAuteur": "Martin", "dateNaissance": "1985-10-20", "nationalite": "Français"}');

INSERT INTO Ressource (id, titre, dateApparition, editeur, genre, codeClassification, contributeur)
VALUES (2, 'Titre du film', '2022-05-20', 'Studio XYZ', 'Action', 456, '{"prenomRealisateur": "Sophie", "nomRealisateur": "Bertrand", "dateNaissance": "1990-05-15", "nationalite": "Espagnole"}');

INSERT INTO Livre (id_livre, ISBN, resume, langue)
VALUES (1, '123-456-789', 'Résumé du livre', 'Français');

INSERT INTO Film (id_film, langue, length, synopsis)
VALUES (2, 'Français', 120, 'Synopsis du film');

INSERT INTO Exemplaire (id_ressource, etat, disponible)
VALUES (1, 'Neuf', true);

INSERT INTO Exemplaire (id_ressource, etat, disponible)
VALUES (2, 'Bon', true);

INSERT INTO Personnel (id)
VALUES (1);

INSERT INTO Pret (id_exemplaire, id_adherent, id_responsable, datePret, duree)
VALUES (1, 1, 1, '2023-01-20', 15);

INSERT INTO Sanction (id_adherent, DateSanction, DateFinSanction, motif, montant, paye)
VALUES (1, '2023-01-25', '2023-02-25', 'Retard', 50.0, false);
