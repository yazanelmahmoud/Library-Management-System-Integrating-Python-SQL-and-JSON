### Introduction :

Notre objectif est de créer une base de donnée qui gère les ressources stockées dans une bibliothèque, leurs emprunts et les utilisateurs de la bibliothèque.

### Liste des objets:
	- Ressources (comprend Films, Musiques, Livres)
	- Exemplaires
	- Utilisateurs (comprend les Membres et les Adhérents)
	- Collaborateurs
	- Prêts



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
		- Code classification: int
		- Prix: float

		*Association:
		    - Composé par des Exemplaires (composition)

		*Contraintes:
            - NA


	>Livres:
		- ISBN: varchar
		- Résumé: varchar
		- Langue: varchar

		*Associations:
		    - En collaboration avec une liste de (Collaborateurs) auteurs (*-*)

		*Contraintes:
		    - NA


	>Films:
		- Langue: varchar
        - Synopsis: varchar
        - Durée: int

		*Associations:
		    - En collaboration avec une liste de (Collaborateurs) réalisateurs (*-*)
            - En collaboration avec une liste de (Collaborateurs) acteurs (*-*)

		*Contraintes:
		    - NA


	>Musiques:
		- Durée: int

		*Associations:
		    - En collaboration avec une liste de (Collaborateurs) compositeurs (*-*)
            - En collaboration avec une liste de (Collaborateurs) interprètes (*-*)

		*Contraintes:
		    - NA


	> Collaborateur:
		- Nom: varchar
		- Prenom: varchar
        - Date naissance: date
        - Nationalité: varchar

		*Associations:
		    - NA
			
		*Contraintes:
		    - NA
		

	>Utilisateurs:
		- Login (clé): varchar
        - Mdp: varchar
        - Nom: varchar
        - Prenom: varchar
        - Adresse: varchar
        - Mail: varchar

	>Membres:
		- NA

		*Associations:
			- Un Membre est un Utilisateur (hérédité)

		*Contraintes:
			- NA

	>Adhérents:
		- Tel: varchar
		- Actuel: bool
		- Nbre sanctions: int
        - Date fin suspension: date
        - Blacklisté: bool

		*Associations:
		    - Un Adhérent est un Utilisateur (hérédité)
		    - Réalise des Prêts (1-0..n)

		*Contraintes:
		    - NA


	>Prêts:
		- Date prêt: date
		- Durée prêt: int
        - Date retour: date
        - Etat retour: appartient à {neuf, bon, abîmé, perdu} enumerate
        - Sanction: bool

		*Associations:
		    - Concerne un Exemplaire (0..n-1)

		*Contraintes:
		    - NA


### Classe supplémentaire qui sera gérée directement par l'affichage des données:

	>Vue Exemplaires Disponibles:
		- Jointure tables Ressources, Exemplaires, Collaborateurs, Prêts (conditions: date dernier rendu de l'exemplaire < date du jour ET etat dernier rendu = neuf OU bon)
    

### Hypothèses complémentaires:

	- NA

Un contrôle utilisateur sera en plus ajouté de telle manière à ce que les adhérents aient uniquement accès à des vues des tables alors que les membres peuvent modifier les tables.