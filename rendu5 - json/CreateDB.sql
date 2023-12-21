CREATE TABLE IF NOT EXISTS Livre (
    id SERIAL PRIMARY KEY,
    titre VARCHAR(100) NOT NULL,
    dateApparition DATE NOT NULL,
    editeur VARCHAR(100) NOT NULL,
    genre VARCHAR(100) NOT NULL,
    codeClassification INT NOT NULL,
    dureeMaxPret INT NOT NULL,
    ISBN VARCHAR(20) NOT NULL,
    resume TEXT,
    langue VARCHAR(50),
    contributeur JSON,
    exemplaires JSON
);

CREATE TABLE IF NOT EXISTS Musique (
    id SERIAL PRIMARY KEY,
    titre VARCHAR(100) NOT NULL,
    dateApparition DATE NOT NULL,
    editeur VARCHAR(100) NOT NULL,
    genre VARCHAR(100) NOT NULL,
    codeClassification INT NOT NULL,
    dureeMaxPret INT NOT NULL,
    longueur INT NOT NULL,
    contributeur JSON,
    exemplaires JSON
);

CREATE TABLE IF NOT EXISTS Film (
    id SERIAL PRIMARY KEY,
    titre VARCHAR(100) NOT NULL,
    dateApparition DATE NOT NULL,
    editeur VARCHAR(100) NOT NULL,
    genre VARCHAR(100) NOT NULL,
    codeClassification INT NOT NULL,
    dureeMaxPret INT NOT NULL,
    langue VARCHAR(50) NOT NULL,
    length INT NOT NULL,
    synopsis TEXT,
    contributeur JSON,
    exemplaires JSON
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

CREATE TABLE IF NOT EXISTS Adherent (
    id INT PRIMARY KEY,
    numeroTelephone VARCHAR(100) NOT NULL,
    dateNaissance DATE NOT NULL,
    statut VARCHAR(20) NOT NULL CHECK (
        statut IN ('active', 'expire', 'suspendue', 'blackliste')
    ),
    sanctions JSON,
    prets JSON,
    FOREIGN KEY (id) REFERENCES Utilisateur(id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS Personnel (
    id INT PRIMARY KEY,
    FOREIGN KEY (id) REFERENCES Utilisateur(id) ON DELETE CASCADE
);

CREATE VIEW PersonnelDetails AS
SELECT
    U.id,
    U.login,
    U.password,
    U.prenom,
    U.nom,
    U.email,
    U.adresse
FROM Personnel P
JOIN Utilisateur U ON P.id = U.id;

-- View Pret de l'Adhérent
CREATE VIEW PretAdherent AS
SELECT
    U.id,
    U.login,
    U.password,
    U.prenom,
    U.nom,
    U.email,
    U.adresse,
    A.numeroTelephone,
    A.dateNaissance,
    A.statut,
    A.sanctions,
    A.prets
FROM Adherent A
JOIN Utilisateur U ON A.id = U.id;


CREATE VIEW FilmExemplaires AS
SELECT
    R.id,
    R.titre,
    R.dateApparition,
    R.editeur,
    R.genre,
    R.codeClassification,
    R.dureeMaxPret,
    R.langue,
    R.length,
    R.synopsis,
    R.contributeur,
    E->>'id' AS id_exemplaire,
    E->>'etat' AS etat_exemplaire
FROM Film R, JSON_ARRAY_ELEMENTS(R.exemplaires) E;

CREATE VIEW LivreExemplaires AS
SELECT
    L.id,
    L.titre,
    L.dateApparition,
    L.editeur,
    L.genre,
    L.codeClassification,
    L.dureeMaxPret,
    L.ISBN,
    L.resume,
    L.langue,
    C->>'auteur' AS auteur,
    E->>'id' AS id_exemplaire,
    E->>'etat' AS etat_exemplaire
FROM Livre L, JSON_ARRAY_ELEMENTS(L.exemplaires) E, JSON_ARRAY_ELEMENTS(L.contributeur) C ;

CREATE VIEW MusiqueExemplaires AS
SELECT
    M.id,
    M.titre,
    M.dateApparition,
    M.editeur,
    M.genre,
    M.codeClassification,
    M.dureeMaxPret,
    M.longueur,
    C->>'compositeur' AS compositeur,
    E->>'id' AS id_exemplaire,
    E->>'etat' AS etat_exemplaire
FROM Musique M, JSON_ARRAY_ELEMENTS(M.exemplaires) E , JSON_ARRAY_ELEMENTS(M.contributeur) C;

CREATE VIEW LivreContributeur AS
SELECT
    L.id,
    L.titre,
    L.dateApparition,
    L.editeur,
    L.genre,
    L.codeClassification,
    L.dureeMaxPret,
    L.ISBN,
    L.resume,
    L.langue,
    C->>'auteur' AS auteur,
    E->>'id' AS id_exemplaire,
    E->>'etat' AS etat_exemplaire
FROM Livre L, JSON_ARRAY_ELEMENTS(L.contributeur) C, JSON_ARRAY_ELEMENTS(L.exemplaires) E;
