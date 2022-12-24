# BE-Modelisation

UPSSITECH PROJECT 2ASRI - Modélisation 

Dans ce projet, nous allons modéliser la trajectoire d'un robot RRPR. Pour cela, nous allons afficher différentes courbes telles que les lois de mouvements, la position dans l'espace de l'organe terminal...

Auteurs : JOBERT Pauline, PHAN Quentin, AMBLARD Lucas, TRANI Julian

# Installation & exécution du code 

- Cloner le dépôt sur votre machine 
- Positionnez-vous dans l'arborescence du projet 
- Exécuter le main.py

# Utilisation du code :

Vous pouvez modifier les configurations des longueurs et hauteurs du robot directement dans le fichier data.py contenu dans l'arborescence.

Dans le fichier main.py, vous trouverez des fonctions de tests du MGD-MGI et du MDD-MDI.
De plus, vous pouvez générer une trajectoire à partir de plusieurs paramètres, A, B, thêta et V.

```
A = (2, 2, 2)
B = (2, 3, 2)
V = 1  # V != 0
theta = 0  # en rad
thetaThêtathetathetathetathetatraj = Trajectoire(A, B, theta, V, Te=0.01)
trajtraj.simulation()
traj.display()
```

La fonction display() contient de nombreux paramètres optionnels afin d'activer/désactiver les affichages.
```
traj.display(mvt=False, op=False, O5=False, threeD=False, robot=False, q_n=False)
```

ATTENTION : Il faut que vos points A et B soient atteignables par le robot selon la configuration des longueurs et hauteurs du robot dans le fichier data.py. 
C'est-à-dire que la distance euclidienne entre le centre du repère et vos points sont strictement inférieurs à la somme des longueurs Li du robot. 