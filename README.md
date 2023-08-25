# weather-project

# Projet de Plateforme Météorologique

Ce projet vise à mettre en place une plateforme automatisée pour collecter, stocker et fournir des informations météorologiques en utilisant des technologies telles que Docker, Docker Compose, Python, Flask et Cassandra.

## Table des Matières

- [Introduction](#introduction)
- [Utilisation](#utilisation)
  - [Prérequis](#prérequis)
  - [Déploiement](#déploiement)
- [Structure de la Base de Données](#structure-de-la-base-de-données)
- [API Flask](#api-flask)
- [Personnalisation et Configuration](#personnalisation-et-configuration)
- [Conclusion](#conclusion)

## Introduction

Ce projet propose une solution complète pour collecter et stocker des données météorologiques à partir de l'API OpenWeatherMap dans une base de données Cassandra. L'ensemble de l'infrastructure est orchestré à l'aide de Docker et Docker Compose, ce qui permet un déploiement facile et scalable.

## Utilisation

### Prérequis

Avant de démarrer, assurez-vous d'avoir les éléments suivants installés sur votre système :

- Docker
- Docker Compose
- Python 3.6 ou supérieur

### Déploiement

1. Clonez ce dépôt GitHub sur votre machine.

```bash
git clone https://github.com/iammerouane/weather-project/
cd weather-api-project
```

2. Assurez-vous que Docker est en cours d'exécution sur votre système.

3. Ouvrez un terminal et naviguez vers le répertoire principal du projet.

4. Exécutez la commande suivante pour lancer l'infrastructure à l'aide de Docker Compose.

```bash
docker-compose up -d
```

Cela lancera les services Cassandra et Python dans des conteneurs Docker.

5. Accédez à l'API Flask en ouvrant votre navigateur à l'adresse suivante :

```
http://localhost:5000/weather
```

## Structure de la Base de Données

La base de données Cassandra est conçue pour stocker les données météorologiques collectées. La structure de la base de données est la suivante :

- Keyspace : mon_projet
  - Table : climat
    - id (UUID) : Identifiant unique de l'enregistrement
    - temperature (float) : Température en degrés Celsius
    - humidite (float) : Pourcentage d'humidité
    - pression (float) : Pression en hPa

## API Flask

L'application Flask sert d'interface pour accéder aux données météorologiques stockées dans la base de données Cassandra. L'endpoint "/weather" renvoie les informations météorologiques au format JSON. L'API peut être consultée en utilisant l'URL suivante :

```
http://localhost:5000/weather
```

## Personnalisation et Configuration

- Pour collecter des données pour une autre ville ou pays, modifiez les valeurs de CITY et COUNTRY dans le fichier "crawler.py".
- Obtenez une clé API valide à partir du site OpenWeatherMap et remplacez la valeur de API_KEY dans le fichier "crawler.py".

## Conclusion

Ce projet démontre comment utiliser Docker, Docker Compose, Python, Flask, Cassandra et d'autres technologies pour créer une plateforme météorologique automatisée. Vous pouvez ainsi collecter, stocker et accéder aux données météorologiques de manière efficace et évolutive.

N'hésitez pas à explorer le dépôt GitHub du projet pour des informations plus détaillées, des contributions ou des questions.

**Note :** Assurez-vous de consulter la documentation officielle des technologies utilisées pour des informations plus détaillées sur les commandes, les fonctionnalités et les meilleures pratiques.
