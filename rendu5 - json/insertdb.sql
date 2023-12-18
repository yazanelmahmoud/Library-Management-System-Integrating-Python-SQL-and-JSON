INSERT INTO Ressource (titre, dateApparition, editeur, genre, codeClassification, contributeur, exemplaires) VALUES
('Harry Potter à l''école des sorciers', '1997-06-26', 'Gallimard', 'Fantastique', 1, '{"auteur": "J.K. Rowling", "realisateur" :"Chris Columbus", "acteur": "Daniel Radcliffe"}', '[{"id": 1, "etat": "Neuf"}, {"id": 2, "etat": "Bon"}, {"id": 3, "etat": "Abime"}]'),
('Harry Potter et la Chambre des secrets', '1998-07-02', 'Gallimard', 'Fantastique', 1, '{"auteur": "J.K. Rowling", "realisateur" :"Chris Columbus", "acteur": "Daniel Radcliffe"}', '[{"id": 4, "etat": "Neuf"}, {"id": 5, "etat": "Bon"}, {"id": 6, "etat": "Abime"}]'),
('Harry Potter et le Prisonnier d''Azkaban', '1999-07-08', 'Gallimard', 'Fantastique', 1, '{"auteur": "J.K. Rowling", "realisateur" :"Alfonso Cuaron", "acteur": "Daniel Radcliffe"}', '[{"id": 7, "etat": "Neuf"}, {"id": 8, "etat": "Bon"}, {"id": 9, "etat": "Abime"}]'),
('Harry Potter et la Coupe de feu', '2000-07-08', 'Gallimard', 'Fantastique', 1, '{"auteur": "J.K. Rowling", "realisateur" :"Mike Newell", "acteur": "Daniel Radcliffe"}', '[{"id": 10, "etat": "Neuf"}, {"id": 11, "etat": "Bon"}, {"id": 12, "etat": "Abime"}]'),
('Harry Potter et l''Ordre du phénix', '2003-07-08', 'Gallimard', 'Fantastique', 1, '{"auteur": "J.K. Rowling", "realisateur" :"David Yates", "acteur": "Daniel Radcliffe"}', '[{"id": 13, "etat": "Neuf"}, {"id": 14, "etat": "Bon"}, {"id": 15, "etat": "Abime"}]'),
('Harry Potter et le Prince de sang-mêlé', '2005-07-08', 'Gallimard', 'Fantastique', 1, '{"auteur": "J.K. Rowling", "realisateur" :"David Yates", "acteur": "Daniel Radcliffe"}', '[{"id": 16, "etat": "Neuf"}, {"id": 17, "etat": "Bon"}, {"id": 18, "etat": "Abime"}]'),
('Harry Potter et les Reliques de la Mort', '2007-07-08', 'Gallimard', 'Fantastique', 1, '{"auteur": "J.K. Rowling", "realisateur" :"David Yates", "acteur": "Daniel Radcliffe"}', '[{"id": 19, "etat": "Neuf"}, {"id": 20, "etat": "Bon"}, {"id": 21, "etat": "Abime"}]'),
('Le Seigneur des anneaux : La Communauté de l''anneau', '1954-07-29', 'Gallimard', 'Fantastique', 1, '{"auteur": "J.R.R. Tolkien", "realisateur" :"Peter Jackson", "acteur": "Elijah Wood"}', '[{"id": 22, "etat": "Neuf"}, {"id": 23, "etat": "Bon"}, {"id": 24, "etat": "Abime"}]'),
('Le Seigneur des anneaux : Les Deux Tours', '1954-11-11', 'Gallimard', 'Fantastique', 1, '{"auteur": "J.R.R. Tolkien", "realisateur" :"Peter Jackson", "acteur": "Elijah Wood"}', '[{"id": 25, "etat": "Neuf"}, {"id": 26, "etat": "Bon"}, {"id": 27, "etat": "Abime"}]'),
('Le Seigneur des anneaux : Le Retour du roi', '1955-10-20', 'Gallimard', 'Fantastique', 1, '{"auteur": "J.R.R. Tolkien", "realisateur" :"Peter Jackson", "acteur": "Elijah Wood"}', '[{"id": 28, "etat": "Neuf"}, {"id": 29, "etat": "Bon"}, {"id": 30, "etat": "Abime"}]'),
('Le Hobbit : Un voyage inattendu', '1937-09-21', 'Gallimard', 'Fantastique', 1, '{"auteur": "J.R.R. Tolkien", "realisateur" :"Peter Jackson", "acteur": "Martin Freeman"}', '[{"id": 31, "etat": "Neuf"}, {"id": 32, "etat": "Bon"}, {"id": 33, "etat": "Abime"}]'),
('Le Hobbit : La Désolation de Smaug', '1937-09-21', 'Gallimard', 'Fantastique', 1, '{"auteur": "J.R.R. Tolkien", "realisateur" :"Peter Jackson", "acteur": "Martin Freeman"}', '[{"id": 34, "etat": "Neuf"}, {"id": 35, "etat": "Bon"}, {"id": 36, "etat": "Abime"}]'),
('Le Hobbit : La Bataille des Cinq Armées', '1937-09-21', 'Gallimard', 'Fantastique', 1, '{"auteur": "J.R.R. Tolkien", "realisateur" :"Peter Jackson", "acteur": "Martin Freeman"}', '[{"id": 37, "etat": "Neuf"}, {"id": 38, "etat": "Bon"}, {"id": 39, "etat": "Abime"}]'),
('Le Hobbit', '1937-09-21', 'Gallimard', 'Fantastique', 1, '{"auteur": "J.R.R. Tolkien", "realisateur" :"Peter Jackson", "acteur": "Martin Freeman"}', '[{"id": 40, "etat": "Neuf"}, {"id": 41, "etat": "Bon"}, {"id": 42, "etat": "Abime"}]'),
('Le Hobbit : La Désolation de Smaug', '1937-09-21', 'Gallimard', 'Fantastique', 1, '{"auteur": "J.R.R. Tolkien", "realisateur" :"Peter Jackson", "acteur": "Martin Freeman"}', '[{"id": 43, "etat": "Neuf"}, {"id": 44, "etat": "Bon"}, {"id": 45, "etat": "Abime"}]');


INSERT INTO Utilisateur (id, login, password, prenom, nom, email, adresse) VALUES 
(1, 'utilisateur1', 'mdp123', 'Jean', 'Dupont','jean@example.com', '{"rue": "Rue de la Paix", "numero": 10, "codePostal": "75001", "ville": "Paris"}'),
(2, 'utilisateur2', 'mdp123', 'Fabrice', 'Durand','fabrice@example.com', '{"rue": "Rue de Clermont", "numero": 20, "codePostal": "30200", "ville": "Bagnols-sur-Cèze"}'),
(3, 'utilisateur3', 'mdp123', 'Marie', 'Martin','marie@example.com', '{"rue": "Rue de la République", "numero": 30, "codePostal": "13001", "ville": "Marseille"}'),
(4, 'utilisateur4', 'mdp123', 'Sophie', 'Bernard','sophie@example.com', '{"rue": "Rue de la Liberté", "numero": 40, "codePostal": "69001", "ville": "Lyon"}'),
(5, 'utilisateur5', 'mdp123', 'Pierre', 'Petit', 'pierre@example.com', '{"rue": "Rue de la Gare", "numero": 50, "codePostal": "59000", "ville": "Lille"}');

INSERT INTO Adherent (id, numeroTelephone, dateNaissance, statut, sanctions) VALUES
(1, '0123456789', '2002-01-01', 'active', '[{"motif":"perte", "datePret": "2023-12-01","dateRetour": "2023-12-10"},{"motif":"deterioration", "datePret":"2023-11-15", "dateRetour":"null"}]'),
(3, '0456926843', '1995-01-01', 'active', '[{"motif":"perte", "datePret": "2023-12-02","dateRetour": "2023-10-11"}, {"motif":"deterioration", "datePret":"2023-11-15", "dateRetour":"null"}]'),
(5, '0634434566', '2003-01-01', 'active', '[{"motif":"perte", "datePret": "2023-12-03","dateRetour": "2023-12-13"}, {"motif":"deterioration", "datePret":"2023-11-15", "dateRetour":"null"}]');


SELECT prenom, nom, email, A->>'rue' AS Rue, CAST(A->>'numero' AS INTEGER) AS Numero, A->>'codePostal' AS Code_Postal, A->>'ville' AS Ville 
FROM Utilisateur U, JSON_ARRAY_ELEMENT(U.Adresse) A;

SELECT u.nom, u.prenom, a.statut, s->>'motif' AS Motif, s->>'datePret' AS Date_Pret, s->>'dateRetour' AS Date_Retour
FROM Utilisateur u, Adherent a, JSON_ARRAY_ELEMENTS(a.Sanctions) s
WHERE u.id = a.id;

SELECT titre, dateApparition, editeur, genre, codeClassification, CAST(E->>'id' AS INTEGER) AS id_exemplaire, E->>'etat' AS etat_exemplaire, C->>'realisateur' AS Realisateur, C->>'acteur' AS Acteur, C->>'auteur' AS Auteur
FROM Ressource R, JSON_ARRAY_ELEMENTS(R.exemplaires) E, JSON_ARRAY_ELEMENTS(R.contributeur) C;
