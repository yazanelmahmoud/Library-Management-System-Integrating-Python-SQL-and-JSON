
Introduction :

Notre objectif est de créer une base de donnée qui gère les ressources stockées dans une bibliothèque, leurs emprunts et les utilisateurs de la bibliothèque.

Liste des objets:
	- Ressources (comprend Films, Musiques, Livres)
	- Exemplaires
	- Utilisateurs (comprend les Membres et les Adhérents)
	- Collaborateurs
	- Prêts



Héritages:
	- Films, Musiques et Livres héritent des caractéristiques des Ressources
	- Membres et Adhérents héritent des caractéristiques des Utilisateurs
	- Ces deux héritages seront exclusifs


Liste des classes objets avec propriétés, associations et contraintes:

	>Ressources:
		- Code (clé): int
		- Titre: varchar
		- Date_apparition: date
		- Editeur: varchar
		- Genre: varchar
		- Code_classification: int
		- Prix: float

		*Association 
			- Composé par des Exemplaires (composition)

		*Contraintes:
            -


	>Livres:
		- ISBN: varchar
		- Résumé: varchar
		- Langue: varchar

		*Associations
			- En collaboration avec une liste de (Collaborateurs) auteurs (*-*)

		*Contraintes
		    - 


	>Films:
		- Langue: varchar
        - Synopsis: varchar
        - Durée: int

		*Associations
		    - En collaboration avec une liste de (Collaborateurs) réalisateurs (*-*)
            - En collaboration avec une liste de (Collaborateurs) acteurs (*-*)

		*Contraintes
		    - 


	>Musiques:
		- Durée: int

		*Associations
		    - En collaboration avec une liste de (Collaborateurs) compositeurs (*-*)
            - En collaboration avec une liste de (Collaborateurs) interprètes (*-*)

		*Contraintes
		    - 


	> Collaborateur:
		- Nom: varchar
		- Prenom: varchar
        - Date_naissance: date
        - Nationalité: varchar

		*Associations:
			- 
			
		*Contraintes:
			- 
		

	>Utilisateurs:
		- Login (clé): varchar
        - Mdp: varchar
        - Nom: varchar
        - Prenom: varchar
        - Adresse: varchar
        - Mail: varchar

	>Membres:
		- 

		*Associations
			- Un Membre est un Utilisateur (hérédité)

		*Contraintes:
			- 

	>Adhérents:
		- Tel: varchar
		- Actuel: bool
		- Nbre_sanctions: int
        - Date_fin_suspendu: date
        - Blacklisté: bool

		*Associations:
			- Un Adhérent est un Utilisateur (hérédité)
			- Réalise des Prêts (1-0..n)

		*Contraintes:
			- 


	>Prêts:
		- Date_prêt: date
		- Durée_prêt: int
        - Date_retour: date
        - Etat_retour: appartient à {neuf, bon, abîmé, perdu} enumerate
        - Sanction: bool

		*Associations:
		- Concerne un Exemplaire (0..n-1)


Classe supplémentaire qui sera gérée directement par l'affichage des données:

	>Vue_Exemplaires_Disponibles:
		Jointure tables Ressources, Exemplaires, Collaborateurs, Prêts (conditions: date dernier rendu de l'exemplaire < date du jour ET etat dernier rendu = neuf OU bon)
    

Hypothèses complémentaires:

	- 

Un contrôle utilisateur sera en plus ajouté de telle manière à ce que les adhérents aient uniquement accès à des vues des tables alors que les membres peuvent modifier les tables.
