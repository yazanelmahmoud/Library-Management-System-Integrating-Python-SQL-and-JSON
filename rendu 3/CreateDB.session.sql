CREATE TABLE IF NOT EXISTS Ressource (
    id INT PRIMARY KEY,
    titre VARCHAR(100),
    dateApparition DATE,
    editeur VARCHAR(100),
    genre VARCHAR(100),
    codeClassification INT
);

CREATE TABLE IF NOT EXISTS Livre (
    id_livre INT PRIMARY KEY,
    ISBN VARCHAR(100),
    resume VARCHAR(255),
    langue VARCHAR(50),
    FOREIGN KEY (id_livre) REFERENCES Ressource(id)
);

CREATE TABLE IF NOT EXISTS Musique (
    id_musique INT PRIMARY KEY,
    longueur INT NOT NULL,
    FOREIGN KEY (id_musique) REFERENCES Ressource(id)
);

CREATE TABLE IF NOT EXISTS Film (
    id_film INT PRIMARY KEY,
    langue VARCHAR(50),
    length INT NOT NULL,
    synopsis VARCHAR(255),
    FOREIGN KEY (id_film) REFERENCES Ressource(id)
);

CREATE TABLE IF NOT EXISTS Contributeur (
    id INT PRIMARY KEY,
    prenom VARCHAR(100),
    nom VARCHAR(100),
    dateNaissance DATE,
    nationalite VARCHAR(50)
);

CREATE TABLE IF NOT EXISTS Auteur (
    id_livre INT NOT NULL,
    id_contributeur INT NOT NULL,
    PRIMARY KEY (id_livre, id_contributeur),
    FOREIGN KEY (id_livre) REFERENCES Livre(id_livre),
    FOREIGN KEY (id_contributeur) REFERENCES Contributeur(id)
);

CREATE TABLE IF NOT EXISTS Interprete (
    id_musique INT NOT NULL,
    id_contributeur INT NOT NULL,
    PRIMARY KEY (id_musique, id_contributeur),
    FOREIGN KEY (id_musique) REFERENCES Musique(id_musique),
    FOREIGN KEY (id_contributeur) REFERENCES Contributeur(id)
);

CREATE TABLE IF NOT EXISTS Compositeur (
    id_musique INT NOT NULL,
    id_contributeur INT NOT NULL,
    PRIMARY KEY (id_musique, id_contributeur),
    FOREIGN KEY (id_musique) REFERENCES Musique(id_musique),
    FOREIGN KEY (id_contributeur) REFERENCES Contributeur(id)
);

CREATE TABLE IF NOT EXISTS Acteur (
    id_film INT NOT NULL,
    id_contributeur INT NOT NULL,
    PRIMARY KEY (id_film, id_contributeur),
    FOREIGN KEY (id_film) REFERENCES Film(id_film),
    FOREIGN KEY (id_contributeur) REFERENCES Contributeur(id)
);

CREATE TABLE IF NOT EXISTS Realisateur (
    id_film INT NOT NULL,
    id_contributeur INT NOT NULL,
    PRIMARY KEY (id_film, id_contributeur),
    FOREIGN KEY (id_film) REFERENCES Film(id_film),
    FOREIGN KEY (id_contributeur) REFERENCES Contributeur(id)
);

CREATE TABLE IF NOT EXISTS Exemplaire (
    id INT PRIMARY KEY,
    id_ressource INT,
    etat VARCHAR(20) CHECK (etat IN ('Neuf', 'Bon', 'Abimé', 'Perdu')),
    disponible BOOLEAN,
    FOREIGN KEY (id_ressource) REFERENCES Ressource(id)
);

CREATE TABLE IF NOT EXISTS Adresse (
    id INT PRIMARY KEY,
    rue VARCHAR(100),
    numero INT,
    codePostal INT,
    ville VARCHAR(100)
);

CREATE TABLE IF NOT EXISTS Utilisateur (
    id INT PRIMARY KEY,
    login VARCHAR(150),
    password VARCHAR(150),
    prenom VARCHAR(100),
    nom VARCHAR(100),
    email VARCHAR(150),
    adresse INT,
    FOREIGN KEY (adresse) REFERENCES Adresse(id)
);
 
CREATE TABLE IF NOT EXISTS Personnel (
    id INT PRIMARY KEY,
    id_personnel INT NOT NULL,
    FOREIGN KEY (id) REFERENCES Utilisateur(id),
    FOREIGN KEY (id_personnel) REFERENCES Utilisateur(id)
);

CREATE TABLE IF NOT EXISTS Adherent (
    id INT PRIMARY KEY,
    numeroTelephone VARCHAR(100) NOT NULL,
    dateNaissance DATE NOT NULL,
    statut VARCHAR(20) NOT NULL CHECK (statut IN ('active', 'expiré', 'suspendue', 'blacklisté')),
    FOREIGN KEY (id) REFERENCES Utilisateur(id)
);

CREATE TABLE IF NOT EXISTS Pret (
    id INT PRIMARY KEY,
    id_exemplaire INT NOT NULL,
    id_adherent INT NOT NULL,
    id_responsable INT NOT NULL,
    datePret DATE NOT NULL,
    duree INT NOT NULL,
    dateRetour DATE NOT NULL,
    etatRetour VARCHAR(20) NOT NULL CHECK (etatRetour IN ('neuf', 'bon', 'abîmé', 'perdu')),
    FOREIGN KEY (id_exemplaire) REFERENCES Exemplaire(id),
    FOREIGN KEY (id_adherent) REFERENCES Adherent(id),
    FOREIGN KEY (id_responsable) REFERENCES Personnel(id)
);

CREATE TABLE IF NOT EXISTS Sanction (
   id_sanction INT PRIMARY KEY,
   DateSanction DATE,
   DateFinSanction DATE,
   motif VARCHAR(20) NOT NULL CHECK (motif IN ('Retard', 'Détérioration', 'Perte')),
   montant FLOAT,
   FOREIGN KEY (id_sanction) REFERENCES Adherent(id)
);

CREATE VIEW LivreDetails AS
SELECT
    L.id_livre,
    R.titre AS titre_livre,
    R.dateApparition,
    R.editeur,
    R.genre,
    R.codeClassification,
    L.ISBN,
    L.resume,
    L.langue
FROM Livre L
JOIN Ressource R ON L.id_livre = R.id;

CREATE VIEW LivreExemplaires AS
SELECT
    L.id_livre,
    R.titre AS titre_livre,
    E.etat,
    E.disponible,
    R.dateApparition,
    R.editeur,
    R.genre,
    R.codeClassification,
    L.ISBN,
    L.resume,
    L.langue
FROM Livre L
JOIN Ressource R ON L.id_livre = R.id
JOIN Exemplaire E ON E.id_ressource = R.id;

CREATE VIEW MusiqueDetails AS
SELECT
    M.id_musique,
    R.titre AS titre_musique,
    R.dateApparition,
    R.editeur,
    R.genre,
    R.codeClassification,
    M.longueur
FROM Musique M
JOIN Ressource R ON M.id_musique = R.id;

CREATE VIEW MusiqueExemplaires AS
SELECT
    M.id_musique,
    R.titre AS titre_musique,
    E.etat,
    E.disponible,
    R.dateApparition,
    R.editeur,
    R.genre,
    R.codeClassification,
    M.longueur
FROM Musique M
JOIN Ressource R ON M.id_musique = R.id
JOIN Exemplaire E ON E.id_ressource = R.id;

CREATE VIEW FilmDetails AS
SELECT
    F.id_film,
    R.titre AS titre_film,
    R.dateApparition,
    R.editeur,
    R.genre,
    F.synopsis,
    R.codeClassification,
    F.length,
    F.langue
FROM Film F
JOIN Ressource R ON F.id_film = R.id;

CREATE VIEW FilmExemplaires AS
SELECT
    F.id_film,
    R.titre AS titre_film,
    E.etat,
    E.disponible,
    R.dateApparition,
    R.editeur,
    R.genre,
    F.synopsis,
    R.codeClassification,
    F.length,
    F.langue
FROM Film F
JOIN Ressource R ON F.id_film = R.id
JOIN Exemplaire E ON E.id_ressource = R.id;

CREATE VIEW PrêtExemplaire AS
SELECT
    P.id,
    P.id_exemplaire,
    P.id_adherent,
    E.disponible,
    P.datePret,
    P.dateRetour,
    P.etatRetour
FROM Pret P
JOIN Exemplaire E ON E.id = P.id_exemplaire
JOIN Adherent A ON A.id = P.id_adherent;

