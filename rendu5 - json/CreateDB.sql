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
    contributeur JSON NOT NULL,
    exemplaires JSON NOT NULL
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
    contributeur JSON NOT NULL,
    exemplaires JSON NOT NULL
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
    contributeur JSON NOT NULL,
    exemplaires JSON NOT NULL
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
