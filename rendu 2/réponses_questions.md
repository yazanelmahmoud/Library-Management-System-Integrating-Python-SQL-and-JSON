### Pensez vous qu'on peut modéliser le lien entre la gestion des prêts et le personnel?

On peut modéliser ce lien en ajoutant une relation entre les classes Prêt et Personnel "est-responsable" (1-*) pour permettre de savoir quel membre du personnel a enregistré quel prêt. En MLD ça se manifestera par l'ajout d'une clé étrangère dans la relation Prêt référençant la relation Personnel.

### Dans vos classes d'association prêt (aussi appelés emprunt pour certains groupes), la durée est celle de ce prêt ou bien c'est la durée maximale autorisée pour le prêt?

La durée du prêt est une méthode calculant la durée entre la date d'emprunt et la date de retour. La durée maximum d'emprunt est un attribut de la ressource.

### Pensez vous que la durée maximale de prêt ne serait-elle pas propre à une ressource et non pas à un prêt?

Effectivement, il semble plus cohérent que pour une même ressource tous les exemplaires aient la même durée maximum d'emprunt.