### Introduction :

Notre objectif est de créer une base de donnée qui gère les ressources stockées dans une bibliothèque, leurs emprunts et les utilisateurs de la bibliothèque.

### Liste des objets:
	- Ressources (comprend Films, Musiques, Livres)
	- Exemplaires
	- Utilisateurs (comprend les Membres et les Adhérents)
	- Contributeurs
	- Prêts
	- Sanctions


### Héritages:
	- Films, Musiques et Livres héritent des caractéristiques des Ressources
	- Membres et Adhérents héritent des caractéristiques des Utilisateurs
	- Ces deux héritages seront exclusifs


### Liste des classes objets avec propriétés, associations et contraintes:

	>Ressources:
		- Code (clé): int
		- Titre: varchar
		- Date apparition: date
		- Editeur: varchar
		- Genre: varchar
		- Code classification: varchar

		*Association:
		    - Composé par des Exemplaires (composition)


	>Livres:
		- ISBN: varchar
		- Résumé: varchar
		- Langue: varchar

		*Associations:
		    - En collaboration avec une liste de (Contributeurs) auteurs (*-*)
			- Un Livre est une Ressource (hérédité)


	>Films:
		- Langue: varchar
        - Synopsis: varchar
        - Durée: int

		*Associations:
		    - En collaboration avec une liste de (Contributeurs) réalisateurs (*-*)
            - En collaboration avec une liste de (Contributeurs) acteurs (*-*)
			- Un Film est une Ressource (hérédité)

		*Contraintes:
		    - Durée >=0


	>Musiques:
		- Durée: int

		*Associations:
		    - En collaboration avec une liste de (Contributeurs) compositeurs (*-*)
            - En collaboration avec une liste de (Contributeurs) interprètes (*-*)
			- Une Musique est une Ressource (hérédité)

		*Contraintes:
		    - Durée >=0


	> Contributeurs:
		- Nom: varchar
		- Prenom: varchar
        - Date naissance: date
        - Nationalité: varchar
			
		*Contraintes:
		    - Date naissance < aujourd'hui
		

	> Exemplaires:
		- Etat: appartient à {neuf, bon, abîmé, perdu} enumerate

		
	>Utilisateurs:
		- Login (clé): varchar
        - Mdp: varchar
        - Nom: varchar
        - Prenom: varchar
        - Adresse: varchar
        - Mail: varchar


	>Membres:
	    + gestionPrets()
        + gestionUtilisateurs()

		*Associations:
			- Un Membre est un Utilisateur (hérédité)


	>Adhérents:
		- Tel: varchar
		- NumeroTelephone: String
		- DateNaissance: Date
		- Statut: {active, expiré,suspendue,blackliste}
		+ HistoriqueDePrets(): List<Pret>


		*Associations:
		    - Un Adhérent est un Utilisateur (hérédité)
		    - Réalise des Prêts (1-0..n)
			- Est sanctionné (1-0..n)


    >Sanctions:
		- DateSanction: Date
		- DateFinSanction: Date
		- motif: {Retard, Deterioration, Perte}
		- montant: double
		+ payerSanction()
		+ prolongerSanction()
		+ annulerSanction()


	>Prêts:
		- Date prêt: date
		- Durée prêt: int
        - Date retour: date
        - Etat retour: appartient à {neuf, bon, abîmé, perdu} enumerate

		*Associations:
		    - Concerne un Exemplaire (0..n-1)

		*Contraintes:
		    - Date prêt >= aujourd'hui
			- Durée prêt >= 0
			- Date retour >= date prêt


### Classe supplémentaire qui sera gérée directement par l'affichage des données:

	>Vue Exemplaires Disponibles:
		- Jointure tables Ressources, Exemplaires, Contributeurs, Prêts (conditions: date dernier rendu de l'exemplaire < date du jour ET etat dernier rendu = neuf OU bon)
    

Un contrôle utilisateur sera en plus ajouté de telle manière à ce que les adhérents aient uniquement accès à des vues des tables alors que les membres peuvent modifier les tables.