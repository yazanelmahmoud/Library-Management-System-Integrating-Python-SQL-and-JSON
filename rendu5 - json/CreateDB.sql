CREATE TABLE IF NOT EXISTS Ressource (
    id SERIAL PRIMARY KEY,
    titre VARCHAR(100),
    dateApparition DATE,
    editeur VARCHAR(100),
    genre VARCHAR(100),
    codeClassification INT,
    contributeur JSON NOT NULL
);
CREATE TABLE IF NOT EXISTS Livre (
    id_livre INT PRIMARY KEY,
    ISBN VARCHAR(100),
    resume VARCHAR(255),
    langue VARCHAR(50),
    FOREIGN KEY (id_livre) REFERENCES Ressource(id) ON DELETE CASCADE
);
CREATE TABLE IF NOT EXISTS Musique (
    id_musique INT PRIMARY KEY,
    longueur INT NOT NULL,
    FOREIGN KEY (id_musique) REFERENCES Ressource(id) ON DELETE CASCADE
);
CREATE TABLE IF NOT EXISTS Film (
    id_film INT PRIMARY KEY,
    langue VARCHAR(50),
    length INT NOT NULL,
    synopsis VARCHAR(255),
    FOREIGN KEY (id_film) REFERENCES Ressource(id) ON DELETE CASCADE
);
CREATE TABLE IF NOT EXISTS Exemplaire (
    id SERIAL PRIMARY KEY,
    id_ressource INT,
    etat VARCHAR(20) CHECK (etat IN ('Neuf', 'Bon', 'Abime', 'Perdu')),
    disponible BOOLEAN,
    FOREIGN KEY (id_ressource) REFERENCES Ressource(id) ON DELETE CASCADE
);
CREATE TABLE IF NOT EXISTS Utilisateur (
    id SERIAL PRIMARY KEY,
    login VARCHAR(150) UNIQUE,
    password VARCHAR(150),
    prenom VARCHAR(100),
    nom VARCHAR(100),
    email VARCHAR(150),
    adresse JSON NOT NULL
);
CREATE TABLE IF NOT EXISTS Personnel (
    id INT PRIMARY KEY,
    FOREIGN KEY (id) REFERENCES Utilisateur(id) ON DELETE CASCADE
);
CREATE TABLE IF NOT EXISTS Adherent (
    id INT PRIMARY KEY,
    numeroTelephone VARCHAR(100) NOT NULL,
    dateNaissance DATE NOT NULL,
    statut VARCHAR(20) NOT NULL CHECK (
        statut IN ('active', 'expire', 'suspendue', 'blackliste')
    ),
    FOREIGN KEY (id) REFERENCES Utilisateur(id) ON DELETE CASCADE
);
CREATE TABLE IF NOT EXISTS Pret (
    id SERIAL PRIMARY KEY,
    id_exemplaire INT NOT NULL,
    id_adherent INT NOT NULL,
    id_responsable INT NOT NULL,
    datePret DATE NOT NULL,
    duree INT NOT NULL,
    dateRetour DATE,
    etatRetour VARCHAR(20) CHECK (etatRetour IN ('Neuf', 'Bon', 'Abime', 'Perdu')),
    FOREIGN KEY (id_exemplaire) REFERENCES Exemplaire(id) ON DELETE CASCADE,
    FOREIGN KEY (id_adherent) REFERENCES Adherent(id) ON DELETE CASCADE,
    FOREIGN KEY (id_responsable) REFERENCES Personnel(id) ON DELETE CASCADE
);
CREATE TABLE IF NOT EXISTS Sanction (
    id_sanction SERIAL PRIMARY KEY,
    id_adherent INT,
    DateSanction DATE,
    DateFinSanction DATE,
    motif VARCHAR(20) NOT NULL CHECK (motif IN ('Retard', 'Deterioration', 'Perte')),
    montant FLOAT,
    paye BOOLEAN,
    FOREIGN KEY (id_adherent) REFERENCES Adherent(id)
);

CREATE VIEW LivreDetails AS
SELECT L.id_livre,
    R.titre AS titre_livre,
    R.dateApparition,
    R.editeur,
    R.genre,
    R.codeClassification,
    R.contributeur,
    L.ISBN,
    L.resume,
    L.langue
FROM Livre L
    JOIN Ressource R ON L.id_livre = R.id;


CREATE VIEW LivreExemplaires AS
SELECT L.id_livre,
    R.titre AS titre_livre,
    E.etat,
    E.disponible,
    R.dateApparition,
    R.editeur,
    R.genre,
    R.codeClassification,
    R.contributeur,
    L.ISBN,
    L.resume,
    L.langue
FROM Livre L
    JOIN Ressource R ON L.id_livre = R.id
    JOIN Exemplaire E ON E.id_ressource = R.id;

CREATE VIEW MusiqueDetails AS
SELECT M.id_musique,
    R.titre AS titre_musique,
    R.dateApparition,
    R.editeur,
    R.genre,
    R.codeClassification,
    R.contributeur,
    M.longueur
FROM Musique M
    JOIN Ressource R ON M.id_musique = R.id;
CREATE VIEW FilmDetails AS
SELECT F.id_film,
    R.titre AS titre_film,
    R.dateApparition,
    R.editeur,
    R.genre,
    F.synopsis,
    R.codeClassification,
    R.contributeur,
    F.length,
    F.langue
FROM Film F
    JOIN Ressource R ON F.id_film = R.id;


CREATE VIEW FilmExemplaires AS
SELECT F.id_film,
    R.titre AS titre_film,
    E.etat,
    E.disponible,
    R.dateApparition,
    R.editeur,
    R.genre,
    F.synopsis,
    R.codeClassification,
    R.contributeur,
    F.length,
    F.langue
FROM Film F
    JOIN Ressource R ON F.id_film = R.id
    JOIN Exemplaire E ON E.id_ressource = R.id;

CREATE VIEW PretDetails AS
SELECT P.id,
    P.datePret,
    P.duree,
    P.dateRetour,
    P.etatRetour,
    A.numeroTelephone,
    A.dateNaissance,
    A.statut,
    U.login,
    U.prenom,
    U.nom,
    U.email,
    U.adresse,
    E.etat,
    E.disponible,
    R.titre,
    R.dateApparition,
    R.editeur,
    R.genre,
    R.codeClassification,
    R.contributeur,
    E.id AS id_exemplaire
FROM Pret P
    JOIN Adherent A ON P.id_adherent = A.id
    JOIN Utilisateur U ON A.id = U.id
    JOIN Exemplaire E ON P.id_exemplaire = E.id
    JOIN Ressource R ON E.id_ressource = R.id;


CREATE VIEW PersonnelDetails AS
SELECT A.id,
    U.login,
    U.password,
    U.prenom,
    U.nom,
    U.email,
    U.adresse,
    P.id AS id_personnel
FROM Personnel P
    JOIN Utilisateur U ON P.id = U.id 
    
CREATE VIEW AdherentDetails AS
SELECT U.login,
    U.password,
    U.prenom,
    U.nom,
    U.email,
    U.adresse,
    P.numeroTelephone,
    P.dateNaissance,
    P.statut
FROM Adherent P
    JOIN Utilisateur U ON P.id = U.id 


CREATE VIEW SanctionDetails AS
SELECT U.login,
    S.id_sanction,
    S.DateSanction,
    S.DateFinSanction,
    S.motif,
    S.montant,
    S.paye
FROM Sanction S
    JOIN Utilisateur U ON U.id = S.id_adherent;


CREATE VIEW RessourceDetails AS
SELECT R.id,
    R.titre,
    R.dateApparition,
    R.editeur,
    R.genre,
    R.codeClassification,
    R.contributeur,
    L.ISBN,
    L.resume,
    L.langue,
    M.longueur,
    F.synopsis,
    F.length,
    F.langue
FROM Ressource R
    LEFT JOIN Livre L ON R.id = L.id_livre
    LEFT JOIN Musique M ON R.id = M.id_musique
    LEFT JOIN Film F ON R.id = F.id_film;
