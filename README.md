# Nuit de l'info 2022 !

## Qui sommes-nous ?
5 jeunes de première année d'IUT informatique de Lyon 1 qui ont décidés de participer à la nuit de l'info 2022 et de tout 
gagner !

## Notre infrastructure
Pour l'un de nos défis nous avons besoin de dévelloper une infrastructure basée sur des microservices.
Nous avons donc décidé de déployer notre infrastructure sur un cluster Kubernetes.
On y retrouve :
- Une BD PostgreSQL
- Le site web de l'application
- Une API codé en python

Tous les services sont déployés en mode HPA (Horizontal Pod Autoscaler) pour pouvoir supporter une charge importante
mais aussi limiter les coûts en énergie et en ressources lorsque la charge est faible.

## API FastAPI
L'API est codée en python avec le framework [FastAPI](https://fastapi.tiangolo.com/)

FastAPI est un framework moderne et rapide qui permet de développer des API en python de manière simple et efficace.
Il devient de plus en plus populaire et est utilisé par de nombreuses entreprises comme Spotify, Netflix, notament pour
la gestion de microservices.


Vous pouvez retrouver toute l'api dans le dossier `app` et les fichiers Kubernetes dans le dossier `k8s`.

Pour faciliter le deploiement de l'API, nous avons utilisé des workfolows GitHub Actions.
Ainsi, l'api est conteunerisée et déployée sur le cluster Kubernetes à chaque push sur la branche `main`.
Vous pouvez retrouver le workflow dans le dossier `.github/workflows`.

## PostgreSQL
Pour la base de donnée nous avons choisis PostgreSQL HA.

Déployé sur le cluster Kubernetes grâce à un [Helm Chart Postgres HA](https://github.com/bitnami/charts/tree/main/bitnami/postgresql-ha) 
qui facilite la configuration et le déploiement de l'application. 
Cette version de PostgreSQL permet de gérer des clusters de plusieurs noeuds et de gérer la haute disponibilité ainsi 
que la gestion de la sauvegarde en cas de défaillance d'un noeud. 

## Site web
Le site web est codé en HTML, CSS et Javascript.
De la même manière que l'API, le site web est déployé sur le cluster Kubernetes à chaque push sur la branche `main`.
