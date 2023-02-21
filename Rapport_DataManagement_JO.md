
# Projet de DATA MANAGEMENT
## Les médailles aux Jeux Olympiques modernes
#### Réalisé par : BOUTELEUX Florian, FOTSING MOUAFO Loic, GAULTIER William, PRADEAU Thomas, SAM-DOW-WEGAN Jérémy
###### MASTER 2 MIAGE 2021/2022 - Apprentissage

## Pré-requis

> Version Python utilisée : 3.10.4

>Il est nécessaire d'avoir à jour les modules suivants : 
    - matplotlib : 3.5.2 ou supérieur
    - seaborn : 0.11.2 ou supérieur
    - numpy : 1.16.5 ou supérieur

## Introduction

Tout d’abord, avant d’analyser l’ensemble de notre jeu de données, il est nécessaire d’avoir une connaissance des données, des différentes colonnes ainsi que des résultats que l'on pourrait obtenir.

Pour débuter notre analyse, nous utiliserons un éditeur de code Python, et JupyterLab avec Anaconda. A chaque étape, des extraits de code pertinents, ainsi que les résultats obtenus, graphiques, seront ajoutés au rapport, afin d’illustrer l’analyse.

Le dataset que nous avons choisi pour cette étude est **“120 years of Olympic history: athletes and results”**. Il s'agit d'un ensemble de données historiques sur les Jeux olympiques modernes, comprenant tous les Jeux, d'Athènes 1896 à Rio 2016.

*Lien vers le dataset : https://www.kaggle.com/datasets/heesoo37/120-years-of-olympic-history-athletes-and-results*

Notons que les Jeux d'hiver et d'été ont eu lieu la même année jusqu'en 1992. Par la suite, ils ont été échelonnés de telle sorte que les Jeux d'hiver ont lieu sur un cycle de quatre ans à partir de 1994, puis les Jeux d'été en 1996, puis les Jeux d'hiver en 1998, et ainsi de suite. Une erreur courante commise lors de l'analyse de ces données est de supposer que les Jeux d'été et d'hiver ont toujours été décalés.


## Préparation du jeu de données

Dans cette première partie, nous allons préparer notre jeu de données afin de pouvoir y porter des analyses.

### Dimension du jeu de données

Dans un premier temps, nous chargeons l’ensemble des données avec la bibliothèque Pandas et nous vérifions leur dimension  (nombre de lignes, nombre de colonnes). Pour cela, nous utilisons la fonction "**shape**".

#### Code :
```python=1
import pandas as pd
import seaborn as sns
import numpy as np
 
df = pd.read_csv('athlete_events.csv')
df.shape
```

#### Résultat obtenu:

```
(271116, 15)
```

Cela nous permet d’identifier la forme du tableau du jeu de données. Ici, notre jeu de données possède 271 116 lignes et 15 colonnes différentes. Ces lignes correspondent chacune à une participation, soit un athlète individuel participant à une épreuve olympique. Un athlète ayant participé à plusieurs épreuves sur des mêmes ou des différents jeux représentera ainsi autant de lignes que d'épreuves auxquelles il aura participé.

### Caractéristiques du jeu de données

Dans un second temps, nous allons nous intéresser aux différentes caractéristiques (colonnes) qui composent le jeu de données.


#### Code :
```python=7
list(df)
```
#### Résultat obtenu:
```
['ID',
 'Name',
 'Sex',
 'Age',
 'Height',
 'Weight',
 'Team',
 'NOC',
 'Games',
 'Year',
 'Season',
 'City',
 'Sport',
 'Event',
 'Medal']
 ```

Ces différentes caractéristiques vont nous permettre de réaliser des analyses intéressante, notamment grâce à l'année de participation de chaque athlète, permettant une analyse par éditions.

### Vérification des données vides

Avant d'analyser les données, nous allons vérifier que le jeu de données est complet ou non. C'est-à-dire qu'il est possible que certaines données de participation d'un athlète soit vide. Cela va nous servir afin de s'interroger sur la cause de ces absences de données. Nous allons donc utiliser la fonction **“count”** de Pandas sur chaque colonne du jeu de données et retourner le % de complétion de la colonne :

#### Code :
```python=8
#Renvoie le pourcentage des valeurs incomplètes
def NaN_percent(df, column_name) :
    row_count = df[column_name].shape[0]
    empty_values = row_count - df[column_name].count()
    return (100.0*empty_values)/row_count
for i in list(df):
    print(i + ": " + str(round(NaN_percent(df,i)), 2)+"%")
```
#### Résultat obtenu:
```
ID: 0.0%
Name: 0.0%
Sex: 0.0%
Age: 3.49%
Height: 22.19%
Weight: 23.19%
Team: 0.0%
NOC: 0.0%
Games: 0.0%
Year: 0.0%
Season: 0.0%
City: 0.0%
Sport: 0.0%
Event: 0.0%
Medal: 85.33%
```

Nous pouvons observer que certaines colonnes sont incomplètes. En effet, nous pouvons retrouver les colonnes : **Age, Height, Weight et Medals** (Age, Taille, Poids et Médailles).

L'absence de données dans la colonne **Medals**, s’explique par le fait que seuls les athlètes ayant gagné une médaille ont une donnée de renseignée.
On observe que sur le total des participations, seules 15% d'entre elles ont abouti à une médaille.

## Analyse des données

### Athlètes médaillés depuis 1900

Nous cherchons ici à déterminer combien d'athlètes ont été médaillés depuis 1900, en montrant le nombre de participation, le nombre d'athlètes et le nombre moyen de participations par athlètes.

#### Code :
```python=15
nb_rows = df.shape[0]
nb_athlete = len(df.Name.unique())
part_p_athl = round(nb_rows/nb_athlete, 1)
nb_medailles = len(df[df.Medal.fillna("None") != "None"].Name.unique())
ratio_athl_med = round((nb_medailles/nb_athlete)*100, 1)

print("Nombre participations : ", nb_rows,
      "\nNombre athletes : ", nb_athlete,
      "\nNombre moyen de participations par athlètes : ", part_p_athl,
      "\nNombre athletes medaillés : ", nb_medailles,
      "\nRatio athletes medaillés sur total athlètes : ", ratio_athl_med, "%")
```

#### Résultat obtenu:
```
Nombre participations :  271116 
Nombre athletes :  134732 
Nombre moyen de participations par athlètes :  2.0 
Nombre athletes medaillés :  28202 
Ratio athletes medaillés sur total athlètes :  20.9 %
```

On a un total de 134 732 athlètes sur 271 116 participations, ce qui nous fait une moyenne de 2 participations à une épreuve par athlète.
Il y a donc eu 28 202 athlètes médaillés depuis le début des années 1900, pour 134 732 athlètes au total. Cela fait un ratio de 21% d'athlètes médaillés par rapport au nombre d'athlètes total.

### Nombre de médailles distribués par type

Nous voulons désormais connaître le nombre de médailles distribuées par type depuis le début des années 1900.

#### Code :
```python=26
medals_type = df[df.Medal.fillna("None") != "None"].Medal.value_counts()
medals_type = medals_type.reset_index(name='count').sort_values(['count'], ascending=False) 

ax = sns.barplot(
    data=medals_type,
    x="index", y="count", palette="flare"
)

for container in ax.containers:
    ax.bar_label(container)

nb_medailles_dist = df[df.Medal.fillna("None") != "None"].shape[0]
print("Nombre de médailles distribués : ",nb_medailles_dist)
print("Nombre de médailles par athlète : ", round(nb_medailles_dist/nb_medailles,2))
```

#### Résultat obtenu:
![](https://i.imgur.com/N1RxVdu.png)

Les médailles distribuées sont sans surprise équilibrées, et si nous mettons les 39783 médailles distribuées par rapport au nombre d'athlètes médaillés, un athlète reçoit environ 1,41 médailles.

### Pays les plus médaillés

A présent, nous allons nous intéresser à la distribution des médailles par pays.
Afin de l'obtenir, nous allons afficher sous forme de graphique les pays ayant été les plus médaillés en séparant les trois types de médailles possibles (or, argent, bronze).

#### Code :
```python=30
medailles_par_equipe = df.groupby(['Team','Medal']).Medal.agg('count')
medailles_par_equipe = medailles_par_equipe.reset_index(name='count').sort_values(['count'], ascending=False).head(23) 

g = sns.catplot(
    data=medailles_par_equipe, kind="bar", hue="Medal",
    y="Team", x="count", palette="flare"
)
g.set_axis_labels("Nombre de médailles", "Pays")
```

#### Résultat obtenu:
![](https://i.imgur.com/xGyjBhR.png)

On observe que les **Etats-Unis** est le pays ayant obtenu le plus de médailles, tous types de médaille confondus. De plus, nous pouvons noter que **l'union sovietique**, n'étant plus participante depuis 30 ans, est à la seconde place de ce classement par pays.

Grâce à cette fonction, nous allons pouvoir obtenir les résultats pour le pays souhaité. Ici, nous allons nous intéresser aux valeurs concernant la **France**.

#### Code :
```python=38
stats_france = medailles_par_equipe[medailles_par_equipe.Team=="France"]

g = sns.catplot(
    data=stats_france, kind="bar", hue="Medal",
    x="Team", y="count", palette="flare"
)
g.set_axis_labels("Nombre de médailles", "Pays")
ax = g.facet_axis(0, 0)

for c in ax.containers:
    labels = [f'{(v.get_height())}' for v in c]
    ax.bar_label(c, labels=labels, label_type='edge')
```

#### Résultat obtenu:
![](https://i.imgur.com/64GI4DK.png)

Concernant la **France**, nous pouvons observer que le pays se classe 5^ème^ au rang d'obtention total des médailles. (Voir graphique ci-dessus)

La nation a obtenu plus de médailles de bronze que de médailles d'or.

## Nombre de participations et de médailles aux Jeux d'été par pays

Nous allons maintenant nous intéresser au nombre de participants par pays lors des Jeux Olympiques d'été. Il s'agit de s'intéresser sur la corrélation entre le nombre de participations et le nombres de médailles obtenus.

#### Code :

```python=67
pays_participants = df[["ID", "Games", "Medal", "NOC", "Season"]]
summer_pays_participants = pays_participants[pays_participants.Season=="Summer"]
summer_pays_participants = summer_pays_participants.groupby("NOC", as_index = False).agg({"ID": "count", "Games": pd.Series.nunique, "Medal" : "count"})

ax = sns.scatterplot(x="ID", y="Medal", size="Games", hue="NOC", data=summer_pays_participants)
ax.legend_.remove()
for line in range(0,summer_pays_participants.shape[0]):
     ax.text(summer_pays_participants.ID.iloc[line], summer_pays_participants.Medal.iloc[line], "  "+summer_pays_participants.NOC.iloc[line]+"-"+str(summer_pays_participants.Games.iloc[line]), horizontalalignment='left', size='small', color='black', weight='medium')
ax.set(xlabel='Nombre de participations', ylabel='Nombre de médailles')
ax.legend(["Pays-Jeux participés"], loc= 'upper left')
```

#### Résultat obtenu:
![](https://i.imgur.com/X5ECwXy.png)



Nous pouvons constater qu'une tendance se dessine. En effet, plus le nombre de participants est élevé et plus le nombre total de médailles remporté par le pays est élevé. De plus, nous pouvons observer que les pays qui ont un grand nombre de participations, ont obtenu le plus de médailles.


Notons les USA en tête de course avec 28 participations aux jeux d'été pour environ 5 000 médailles.

## Nombre de participations et de médailles aux Jeux d'hiver par pays

Nous allons maintenant nous intéresser au nombre de participants par pays lors des Jeux olympiques d'hiver.

Nous reprenons les mêmes principes de calcul que pour le Jeux olympiques d'été.

#### Code :

```python=78
pays_participants = df[["ID", "Games", "Medal", "NOC", "Season"]]
winter_pays_participants = pays_participants[pays_participants.Season=="Winter"]
winter_pays_participants = winter_pays_participants.groupby("NOC", as_index = False).agg({"ID": "count", "Games": pd.Series.nunique, "Medal" : "count"})

ax = sns.scatterplot(x="ID", y="Medal", size="Games", hue="NOC", data=winter_pays_participants)
ax.legend_.remove()
for line in range(0,winter_pays_participants.shape[0]):
     ax.text(winter_pays_participants.ID.iloc[line], winter_pays_participants.Medal.iloc[line], "  "+winter_pays_participants.NOC.iloc[line]+"-"+str(winter_pays_participants.Games.iloc[line]), horizontalalignment='left', size='small', color='black', weight='medium')
ax.set(xlabel='Nombre de participations', ylabel='Nombre de médailles')
ax.legend(["Pays-Jeux participés"], loc= 'upper left')
```

#### Résultat obtenu:
![](https://i.imgur.com/2Rfk0fM.png)



Nous pouvons constater que la tendance est moins "marquée" que pour les Jeux d'été. Pour autant, cela nous confirme que le nombre d'athlètes pour un pays influx sur le nombre de médailles obtenus.
On observe toujours une dominance des USA.
On retrouve les pays dit "nordique" comme le Canada, la Norvège ou bien la Suède dans le haut du "Classement".


### Répartition des hommes et des femmes aux jeux olympiques

Nous allons à présent nous intéresser au nombre de femmes et d'hommes participant aux Jeux Olympiques.

#### Code :
```python=50
nb_femme = len(df[df.Sex=="F"].Name.unique())
nb_homme = len(df[df.Sex=="M"].Name.unique())
medailles_femme = df[df.Sex=="F"].Medal.count()
medailles_hommes = df[df.Sex=="M"].Medal.count()

print("nombre athlètes femme : {}".format(nb_femme))
print("médailles obtenues femme : {}".format(medailles_femme))
print("nombre athlètes homme : {}".format(nb_homme))
print("médailles obtenues homme : {}".format(medailles_hommes))
print("Depuis l'année : ")
df[df.Sex=="F"].Year.min()
```

#### Résultat obtenu:
```
nombre athlètes femme : 33808
médailles obtenues femme : 11253
nombre athlètes homme : 100979
médailles obtenues homme : 28530

Depuis l'année : 
1900
```

L'analyse suivante permet d'observer le nombre de femmes et d'hommes ayant participé aux Jeux Olympiques, par année.

#### Code :
```python=61
nb_femme_per_year = df[df.Sex=="F"].groupby("Year").agg("count").Name
nb_homme_per_year = df[df.Sex=="M"].groupby("Year").agg("count").Name
nb_femme = sns.scatterplot(data=nb_femme_per_year)
nb_homme = sns.scatterplot(data=nb_homme_per_year)
nb_all = (nb_homme, nb_femme)
nb_all
nb_homme.set(xlabel='Année', ylabel='Nombre d\'athlètes')
nb_homme.legend(["Femmes", "Hommes"], loc= 'upper right')
```

#### Résultat obtenu:
![](https://i.imgur.com/2X0dMdw.png)

Nous pouvons noter que les femmes ont commencé à participer aux Jeux Olympiques depuis 1900 mais un peu plus tard que les hommes.

Nous pouvons constater que la participation a augmenté rapidement durant les dernières décennies, passant de **0 en 1896 à plus de 4000 à partir des années 90**. De plus, on voit que l'écart entre le nombre d'athlètes hommes et femmes diminue depuis les dernières années.

Ajoutons que les points se situant en bas à droite concernent les Jeux Olympiques d'Hiver. En effet, comme mentionné dans l'introduction, ceux-ci ont été dissociés de l'année des Jeux d'été à partir de 1994.

## Répartition des médailles selon l'âge et le sexe des athlètes

Nous allons à présent nous intéresser au nombre de médailles obtenues selon l'âge et le sexe des athlètes.


#### Code
```python=80
medal_femme_per_age = df[df.Sex=="F"].groupby("Age").agg("count").Medal
medal_homme_per_age = df[df.Sex=="M"].groupby("Age").agg("count").Medal
nb_femme = sns.scatterplot(data=medal_femme_per_age)
nb_homme = sns.scatterplot(data=medal_homme_per_age)
nb_all = (nb_homme, nb_femme)
nb_all
nb_homme.set(xlabel='Age', ylabel='Nombre de médailles')
nb_homme.legend(["Femmes", "Hommes"], loc= 'upper right')
```
#### Résultat
![](https://i.imgur.com/WY7cORn.png)


On observe donc ici un pic de médaillés (féminin et masculin) pour les personnes entre 20 et 30 ans.
On peut voir qu'il y a un gros écart entre les plus jeunes et vieux médaillés.
Ceci s'explique du fait qu'avant il n'y avait pas d'âge limite pour les épreuves et qu'il y avait des disciplines artistiques tels que la sculpture, la peinture... qui étaient accessibles aux personnes âgées voir très agées (le médaillé le plus agé avait 97 ans lors de sa partcipation).
On voit ausi qu'à 18 ans le nombre de medaillé hommes et femmes est le  plus proche. 
On sait que le nombre de participations total pour les femmes est bien moins élevé que celui des hommes ce qui explique l'écart, il pourrait être intéréssant de faire le rapport nombre médailles / participation au lieu du nombre de médailles pour avoir une tendance plus équilibrée.


## Rapport poids par sport chez les hommes
Après avoir analysé les données concernant les médailles, nous avons determiné que des données pouvant être intéressantes à analyser sont celles liées à la taille et au poids d'un athlète.

Nous allons donc afficher pour chaque sport, le poids minimum et maximum observé chez un athlète et calculer la taille moyenne dans ces sports.

 
#### Code :

```python=64
hommes = df[df.Sex=='M']
poids_taille_par_sport_hommes = hommes.groupby(['Sport'])[['Weight','Height']].agg(['min','max','mean'])
```
```python=66
poids_taille_par_sport_hommes.Weight.dropna().sort_values('mean', ascending=False)[:5]
```

#### Résultat obtenu:
![](https://i.imgur.com/CeqW2yo.png)

> La colonne "Mean" correspond à la moyenne du poids.

Les 5 sports ayant la moyenne du poids la plus élevée sont : le Tir à la corde, le Basketball, le Rugby à 7, le Bobsleigh ainsi que le Beach Volley.

Si nous prennons comme exemple le Rugby à 7, on voit que l'athlète le plus léger est de 65 Kg, l'athlète le plus lourd est de 113 Kg pour une moyenne de 91 Kg sur ce sport.

#### Code :

```python=67
poids_taille_par_sport.Weight.dropna().sort_values('mean', ascending=True)[:5]
```

#### Résultat obtenu:
![](https://i.imgur.com/hsgel6a.png)

> La colonne "Mean" correspond à la moyenne du poids.

Ces résultats reprennent les mêmes informations, mais il s'agit ici, des 5 sports ayant les moyennes les plus basses.

Pour la boxe, l'athlète le plus léger, pèse 46 Kg et le plus lourd 140 Kg. Nous retrouvons une moyenne de 65,3 Kg.

## Rapport poids par sport chez les femmes

La même analyse est faite sur la population des femmes athlètes.

#### Code :

```python=64
femmes = df[df.Sex=='F']
poids_taille_par_sport_femmes = femmes.groupby(['Sport'])[['Weight','Height']].agg(['min','max','mean'])
```
```python=66
poids_taille_par_sport_femmes.Weight.dropna().sort_values('mean', ascending=False)[:5]
```

#### Résultat obtenu:
![](https://i.imgur.com/aIlpiCn.png)

> La colonne "Mean" correspond à la moyenne du poids.

Les 5 sports ayant la moyenne du poids la plus élevée sont : le Basketball, le Bobsleigh, le Water Polo, le Rowing et le Volleyball.

Si nous prenons comme exemple le Rugby à 7, on voit que l'athlète la plus légère est de 65 Kg, l'athlète la plus lourde est de 113 Kg pour une moyenne de 91 Kg sur ce sport.


#### Code :

```python=67
poids_taille_par_sport_femmes.Weight.dropna().sort_values('mean', ascending=True)[:5]
```

#### Résultat obtenu:
![](https://i.imgur.com/iac6Rvk.png)

> La colonne "Mean" correspond à la moyenne du poids.

Ces résultats reprennent les mêmes informations, mais il s'agit ici des 5 sports ayant les moyennes les plus basses.

Nous remarquons que pour la gymnastique, le poids minimum observé est de 25 Kg, ce qui est vraiment très peu !

## Conclusion

Pour conclure, nous pouvons dire que les Jeux Olympiques modernes ont énormément évolué en 120 ans d'existence, notamment au niveau de la parité Homme Femme mais aussi sur les épreuves. En effet au cours de cette étude nous avons appris l'existence d'épreuves dites "artistiques" (architecture, peinture, littérature ou encore sculpture). Il serait en effet intéréssant de faire une étude détaillée sur l'évolution des épreuves au fil des années.

