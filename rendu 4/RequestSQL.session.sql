SELECT * FROM PretDetails
WHERE login LIKE '{login}%' AND dateretour IS NULL;

SELECT * FROM FilmExemplaires
WHERE titre_film LIKE '{titre}%';

SELECT id_film, titre_film, synopsis, langue , COUNT(id_film) FROM FilmExemplaires
WHERE titre_film LIKE '{titre}%' AND disponible = 'true'
GROUP BY id_film, titre_film, synopsis, langue
HAVING COUNT(id_film) >0

SELECT * FROM FilmDetails
WHERE titre_film LIKE '{titre}%';

SELECT * FROM MusiqueExemplaires
WHERE titre_musique LIKE '{titre}%';

SELECT id_musique, titre_musique, editeur, longueur , COUNT(id_musique) FROM musiqueExemplaires
WHERE titre_musique LIKE '{titre}%' AND disponible = 'true'
GROUP BY id_musique, titre_musique, editeur, longueur
HAVING COUNT(id_musique) >0;

SELECT * FROM MusiqueDetails
WHERE titre_musique LIKE '{titre}%';

SELECT * FROM LivreExemplaires
WHERE titre_livre LIKE '{titre}%';

SELECT id_livre, titre_livre, editeur, langue , COUNT(id_livre) FROM livreExemplaires
WHERE titre_livre LIKE '{titre}%' AND disponible = 'true'
GROUP BY id_livre, titre_livre, editeur, langue
HAVING COUNT(id_livre) >0;

SELECT * FROM LivreDetails
WHERE titre_livre LIKE '{titre}%';

SELECT * FROM AdherentDetails
WHERE login LIKE '{login}%';

SELECT * FROM PersonnelDetails
WHERE login LIKE '{login}%';

SELECT * FROM AuteurDetails
WHERE id_livre = {id_livre};

SELECT * FROM InterpreteDetails
WHERE id_musique = {id_musique};

SELECT * FROM CompositeurDetails
WHERE id_musique = {id_musique};

SELECT * FROM ActeurDetails
WHERE id_film = {id_film};

SELECT * FROM RealisateurDetails
WHERE id_film = {id_film};

SELECT * FROM Exemplaire
WHERE id_ressource = {ressource[0]};

SELECT * FROM Exemplaire
WHERE id_ressource = {ressource[0]} AND disponible = 'true';

SELECT * FROM AuteurDetails
WHERE nom = '{nom}' AND prenom = '{prenom}' AND datenaissance = '{date_naissance}' AND nationalite = '{nationalite}' AND id_livre = '{livre[0]}';

SELECT * FROM CompositeurDetails
WHERE nom = '{nom}' AND prenom = '{prenom}' AND datenaissance = '{date_naissance}' AND nationalite = '{nationalite}' AND id_musique = '{musique[0]}';

SELECT * FROM interpreteDetails
WHERE nom = '{nom}' AND prenom = '{prenom}' AND datenaissance = '{date_naissance}' AND nationalite = '{nationalite}' AND id_musique = '{musique[0]}';

SELECT * FROM Contributeur
WHERE nom = '{nom}' AND prenom = '{prenom}' AND datenaissance = '{date_naissance}' AND nationalite = '{nationalite}';

SELECT * FROM realisateurDetails
WHERE nom = '{nom}' AND prenom = '{prenom}' AND datenaissance = '{date_naissance}' AND nationalite = '{nationalite}' AND id_film = '{film[0]}';

SELECT * FROM ActeurDetails
WHERE nom = '{nom}' AND prenom = '{prenom}' AND datenaissance = '{date_naissance}' AND nationalite = '{nationalite}' AND id_film = '{film[0]}';

SELECT * FROM AdherentDetails
WHERE login = '{login}' AND statut = 'active';

SELECT * FROM PersonnelDetails
WHERE login = '{login}';

SELECT id FROM Adresse
WHERE rue = '{values["rue"]}' AND numero = '{values["numero"]}' AND codepostal = '{values["codePostal"]}' AND ville = '{values["ville"]}';

SELECT id FROM Utilisateur
WHERE login = '{login}';