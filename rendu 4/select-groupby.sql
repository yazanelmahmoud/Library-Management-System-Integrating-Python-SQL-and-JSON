SELECT genre, COUNT(*) as nombre_ressources
FROM Ressource
GROUP BY genre;

SELECT genre, COUNT(*) as nombre_ressources
FROM Ressource
GROUP BY genre;

SELECT id_adherent, COUNT(*) as nombre_prets
FROM Pret
GROUP BY id_adherent;

SELECT etat, AVG(duree) as duree_moyenne
FROM Pret
JOIN Exemplaire ON Pret.id_exemplaire = Exemplaire.id
GROUP BY etat;

SELECT motif, COUNT(*) as nombre_sanctions
FROM Sanction
GROUP BY motif;
