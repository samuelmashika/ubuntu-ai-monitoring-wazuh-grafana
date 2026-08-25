2. ARCHITECTURE ET CONCEPTION 

2.1 Architecture globale 

La solution repose sur une architecture composée de plusieurs éléments ayant chacun un rôle spécifique. 

Le serveur Ubuntu cible constitue le système surveillé. Il génère les métriques et événements qui seront collectés et analysés. 

Wazuh assure principalement la collecte, l'analyse et la corrélation des événements de sécurité. Il permet notamment de détecter certains comportements correspondant à des règles prédéfinies et de générer des alertes. 

Le module IA, développé en Python, constitue une couche complémentaire dédiée à la détection d'anomalies. Son objectif est d'identifier des comportements qui s'écartent du fonctionnement habituel du serveur à partir des données collectées. 

Grafana assure la visualisation des informations. Il permet de présenter les métriques, alertes et résultats de détection dans des tableaux de bord destinés à faciliter la supervision et l'analyse. 

La logique générale de fonctionnement est donc la suivante : 

Serveur Ubuntu → collecte des données → analyse et détection → corrélation des événements → visualisation → analyse par l'administrateur. 

 

2.2 Rôle des composants 

Composant 

Rôle dans le projet 

Ubuntu Server 

Serveur cible dont les ressources, processus, événements et activités sont surveillés. 

Wazuh 

Collecte, analyse et corrélation des événements de sécurité et génération d'alertes. 

Module IA 

Détection complémentaire des comportements anormaux à partir des données collectées. 

Grafana 

Visualisation des métriques, alertes et résultats sous forme de tableaux de bord. 

Python 

Automatisation de la collecte et développement du module de détection. 

Principe de complémentarité 

Les trois composants principaux répondent à des besoins différents : 

IA → détecter ce qui est inhabituel 

Wazuh → analyser, corréler et alerter 

Grafana → visualiser et faciliter l'analyse 

Cette complémentarité permet de construire une chaîne de supervision allant de la collecte des données jusqu'à leur interprétation par l'administrateur. 

2.3 Architecture réseau et flux 

Architecture du laboratoire 

L'environnement de travail est constitué de trois machines virtuelles Ubuntu Server, connectées au même réseau de laboratoire. 

Machine 

Rôle 

Système 

Adresse IP 

VM1 

Serveur Ubuntu cible 

Ubuntu Server 

192.168.86.142 

VM2 

Serveur Wazuh 

Ubuntu Server 

192.168.86.145 

VM3 

Serveur Grafana et module IA 

Ubuntu Server 

192.168.86.144 

La VM1 constitue la machine cible. Elle sera surveillée afin de collecter ses métriques système, ses événements et certaines informations relatives à son activité. 

La VM2 hébergera Wazuh et assurera la collecte, l'analyse et la corrélation des événements provenant de la machine cible. 

La VM3 sera dédiée à la visualisation avec Grafana ainsi qu'au module de détection d'anomalies développé en Python. 

	Figure 1 — srv-cible + teste de connectivité avec les deux autres serveurs. 

 	Commandes : ping  -c 2 <ip addr>  

 ip a  

 

 

Figure 2 — srv-wazuh+ teste de connectivité avec les deux autres serveurs. 

 

Figure 3 — srv-grafana+ teste de connectivité avec les deux autres serveurs. 

2.4 Scénarios de détection ciblés 

La solution sera évaluée à travers plusieurs scénarios représentatifs. 

Scénario 

Élément surveillé 

Objectif 

Surcharge CPU 

CPU 

Identifier une utilisation anormalement élevée 

Forte utilisation mémoire 

RAM / Swap 

Détecter une consommation inhabituelle 

Processus inhabituel 

Processus 

Identifier l'apparition d'un processus inattendu 

Port inhabituel 

Réseau 

Identifier une modification de l'activité d'écoute 

Erreurs système 

Journaux 

Détecter une répétition anormale d'événements 

Modification de fichier sensible 

Fichiers 

Vérifier la détection d'une modification 

Échecs d'authentification 

Sécurité 

Détecter une activité d'authentification suspecte 

Ces scénarios seront réalisés dans l'environnement de laboratoire et feront l'objet de preuves techniques et d'une analyse des résultats dans le chapitre 6. 
