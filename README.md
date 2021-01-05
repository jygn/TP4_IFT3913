# TP4_IFT3913

Tout d’abord, le script prend en argument l' URL d’un répertoire git. Ensuite, on vérifie si le
répertoire qu’on veut cloner existe déjà, si oui, on le supprime avant de cloner le nouveau
répertoire. Ensuite, grâce à la librairie git on peut extraire la liste de tous les commits du
répertoire git sur lequel on va itérer pour effectuer un git reset sur chacune des versions à l’aide
de leur identifiant. Ainsi , on va exécuter notre programme du TP1 sur chaque version du
répertoire initial pour obtenir le calcul des métriques pertinentes sur toutes les classes de
chacune des versions. On effectue aussi un comptage de tous les fichiers de type .java pour
obtenir le nombre de classes, c’est-à-dire, la donnée n_classe. Pour chaque CSV créé par notre
programme du TP1, on extrait la donnée qui nous intéresse, soit la colonne de la métrique
classe_BC et on calcul la médiane à partir des données de celle-ci. Finalement, on écrit le
output dans un fichier CSV, soient le id_version, le nombre de classe (n_classes) et la médiane
(m_c_BC) pour chacune des versions du répertoire.

Nous avons opté pour l’option de prendre un échantillon aléatoire de 10% des commits de
Jfreechart, car sinon le programme serait très long à rouler. La raison est simple, pour chaque
commit, il faut parser le code et aller chercher chaque classe. Sachant que jfreechart comporte
environ 1000 classes et que nous devons répéter cette étape plus de 400 fois (10 % de 4000),
il est normal que cela prenne beaucoup de temps de calcul. De plus, dans la boucle qui itère
chaque commit, on exécute 1 process à la fois pour rouler notre programme du TP1,
c’est-à-dire qu’on attend que celui-ci se termine avant d’en exécuter un de nouveau, car il sont
toujours dans le même fichier. On aurait pu exécuter un nombre x de process en parallèle, mais
ceci impliquait plus d’effort à investir sans savoir à quel point qu’on pouvait sauver de temps
d'exécution du script. Ainsi, lancer plus de 400 fois un programme nous prend environ 1h20 à
exécuter.

Pour plus de détails, veuillez lire le rapport.
