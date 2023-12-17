CREATE TABLE IF NOT EXISTS Ressource (
    id SERIAL PRIMARY KEY,
    titre VARCHAR(100),
    dateApparition DATE,
    editeur VARCHAR(100),
    genre VARCHAR(100),
    codeClassification INT,
    contributeur JSON NOT NULL
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
    sanctions JSON,
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
    CHECK(dateRetour>=datePret),
    FOREIGN KEY (id_exemplaire) REFERENCES Exemplaire(id) ON DELETE CASCADE,
    FOREIGN KEY (id_adherent) REFERENCES Adherent(id) ON DELETE CASCADE,
    FOREIGN KEY (id_responsable) REFERENCES Personnel(id) ON DELETE CASCADE
);
