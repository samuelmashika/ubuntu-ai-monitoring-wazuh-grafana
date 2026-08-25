6. SCÉNARIOS DE TESTS ET RÉSULTATS 

Après l’implémentation de Wazuh, la mise en place de Grafana et l’intégration du module de détection d’anomalies, une phase de tests est nécessaire afin d’évaluer le fonctionnement global de la solution. 

Les tests sont réalisés dans l’environnement de laboratoire présenté dans les chapitres précédents. Ils ont pour objectif de provoquer différents comportements contrôlés sur le serveur Ubuntu cible et d’observer la réaction des différents composants de la plateforme. 

Les scénarios retenus correspondent aux principaux comportements anormaux définis lors de la conception : 

Surcharge du processeur ; 

Forte utilisation de la mémoire ; 

Apparition d’un processus inhabituel ; 

Activité réseau ou port inhabituel ; 

Erreurs système ; 

Modification d’un fichier sensible ; 

Échecs d’authentification. 

Pour chaque scénario, l’analyse porte sur les informations visibles dans Wazuh, les métriques représentées dans Grafana et, lorsque cela est applicable, le résultat produit par le module de détection d’anomalies. 

L’objectif n’est pas uniquement de vérifier si une alerte apparaît, mais également d’évaluer la cohérence entre le comportement provoqué sur le serveur et les informations remontées par la plateforme. 

6.1 Méthodologie de test 

Afin de rendre les résultats comparables, chaque scénario suit une méthodologie similaire. 

Étape 1 — État initial 

Le serveur Ubuntu est observé avant la réalisation du test afin de vérifier son état dans des conditions normales. 

Les principales métriques sont relevées à partir du tableau de bord Grafana et les éventuels événements présents dans Wazuh sont observés. 

 

 

Figure 65-67 — État initial du serveur avant l’exécution du scénario. 

Étape 2 — Génération du comportement 

Une action contrôlée est exécutée sur le serveur cible afin de provoquer le comportement étudié. 

L’action est réalisée exclusivement dans l’environnement de laboratoire. 

Étape 3 — Observation 

La réaction de la plateforme est ensuite observée. 

Les données sont recherchées dans Wazuh et les variations des métriques sont observées dans Grafana. Le module IA est également vérifié lorsqu’il exploite la métrique concernée. 

Étape 4 — Analyse 

Les résultats obtenus sont comparés au comportement attendu. 

Cette analyse permet de déterminer si le comportement a été correctement observé, s’il a généré une alerte Wazuh et si le module IA l’a identifié comme une anomalie. 

6.2 Scénario 1 — Surcharge du processeur 

Objectif 

Le premier scénario consiste à provoquer une utilisation importante du processeur afin de vérifier la capacité de la plateforme à détecter une surcharge CPU. 

Ce test permet notamment d’évaluer la visualisation de Grafana et la capacité du module IA à identifier une variation importante de l’utilisation du processeur. 

Action 

Une charge CPU contrôlée est générée sur le serveur Ubuntu cible. 

Commandes : stress --cpu 2 --timeout 60s 

Figure 68 — Génération d’une charge CPU contrôlée. 

Détection 

Pendant l’exécution du test, l’évolution de l’utilisation du processeur est observée dans Grafana. 

 

Figure 69 — Augmentation de l’utilisation du processeur observée dans Grafana. 

Le résultat produit par le module IA est également observé. 

 

Figure 70 — Résultat du module de détection d’anomalies lors de la surcharge CPU. 

Analyse 

Le comportement observé est comparé à l’état normal du serveur. 

Le scénario permet de vérifier si l’augmentation importante de l’utilisation CPU est correctement représentée dans Grafana et si le module IA identifie cette variation comme un comportement inhabituel. Ce qui est le cas ici !  

 

6.3 Scénario 2 — Forte utilisation de la mémoire 

Objectif 

Le deuxième scénario vise à provoquer une forte utilisation de la mémoire vive afin d’évaluer la capacité de la plateforme à identifier une situation de pression mémoire. 

Action 

Une charge mémoire contrôlée est générée sur le serveur cible. 

Commandes : stress --vm 1 --vm-bytes 1G --timeout 60s 

Figure 72 — Génération d’une charge mémoire contrôlée. 

Détection 

L’évolution de l’utilisation de la mémoire est observée dans Grafana. 

Figure 73 — Évolution de l’utilisation de la mémoire pendant le scénario. 

Le résultat du module IA est ensuite vérifié. 

 

Figure 74 — Résultat du module de détection d’anomalies lors de la forte utilisation mémoire. 

Analyse 

L’analyse porte sur l’évolution de la RAM et éventuellement du Swap ainsi que sur le résultat produit par le module. 

L'augmentation de la consommation RAM est correctement visualisée. L'IA identifie cet état comme inhabituel par rapport à la phase d'apprentissage. 

Ce scénario permet de déterminer si une augmentation inhabituelle de la consommation mémoire est correctement observable et interprétée par la solution. 

 

6.4 Scénario 3 — Processus inhabituel 

Objectif 

Ce scénario consiste à introduire un processus inhabituel sur le serveur afin de vérifier si son apparition peut être observée par les mécanismes de supervision. 

L’objectif est notamment de vérifier la capacité à identifier une modification de l’activité des processus. 

Action 

Un processus contrôlé est lancé sur le serveur cible. 

 

Figure 75 — Lancement d’un processus contrôlé sur le serveur cible. 

Détection 

La liste des processus est observée afin de vérifier l’apparition du processus. 

Commande : python3 -c "import time; time.sleep(300)" & 

ps aux | grep python3 

Figure 76 — Vérification du processus généré lors du test. 

Les informations disponibles dans Wazuh et les métriques éventuellement représentées dans Grafana sont ensuite analysées. 

 

Figure 77-78 — Observation du comportement du processus dans la plateforme de supervision. 

Analyse 

Wazuh inventorie les processus en temps réel. Bien qu'il ne génère pas toujours une alerte 'critique' pour un processus inconnu sans règle spécifique, il permet à l'administrateur de le voir via l'inventaire. 

Le test permet d’évaluer dans quelle mesure l’apparition d’un processus inhabituel peut être observée et corrélée avec les autres informations disponibles. 

 

6.5 Scénario 4 — Port ou activité réseau inhabituelle 

Objectif 

Ce scénario vise à provoquer une modification contrôlée de l’activité réseau du serveur. 

L’objectif est de vérifier si l’ouverture d’un port ou une variation de l’activité réseau peut être observée par les outils de supervision. 

Action 

Une activité réseau contrôlée est générée sur le serveur cible. 

Commande : python3 -m http.server 8888 & 

Figure 79 — Génération d’une activité réseau contrôlée. 

Détection 

La liste des ports en écoute et l’activité réseau sont vérifiées. 

 

Figure 80 — Vérification de l’activité des ports réseau du serveur. 

L’évolution de l’activité réseau peut également être observée dans Grafana. 

 

Figure 81 — Évolution de l’activité réseau observée dans Grafana. 

 

Analyse 

Ce scénario permet de déterminer si une modification de l’activité réseau est correctement observable et si elle peut constituer un indicateur utile pour la supervision. L'ouverture d'un port est visible via les outils système. Wazuh peut également remonter cette information via son module d'inventaire réseau. 

 

6.6 Scénario 5 — Erreurs système 

Objectif 

Le cinquième scénario consiste à provoquer ou observer des erreurs système contrôlées afin de vérifier leur remontée vers Wazuh. 

L’objectif est de déterminer si les événements générés dans les journaux du système peuvent être collectés et analysés par la plateforme. 

Action 

Un événement générant une erreur contrôlée est réalisé sur le serveur cible. 

Commande : srv-cible@srv-cible:~$ sudo logger "CRITICAL TEST ERROR: System failure simulation" 

Figure 82 — Génération d’un événement système contrôlé. 

 

Détection 

Les journaux et événements remontés par l’agent sont ensuite consultés dans Wazuh. 

 

Figure 83 — Événement système détecté par Wazuh. 

Analyse 

Wazuh collecte efficacement les journaux système. Toute erreur critique écrite dans syslog est centralisée et consultable. 

Ce scénario permet de vérifier le fonctionnement de la collecte des journaux et la capacité de Wazuh à analyser les événements générés sur le serveur. 

6.7 Scénario 6 — Modification d’un fichier sensible 

Objectif 

Ce scénario vise à vérifier la capacité de la plateforme à détecter une modification apportée à un fichier considéré comme sensible. 

La modification d’un fichier important peut constituer un indicateur intéressant dans le cadre de la surveillance d’un serveur. 

Action 

Un fichier sélectionné pour le test est modifié dans l’environnement de laboratoire. 

Commade : echo "Modification détectée" >> /home/srv-cible/fim-surveillance/test.txt 

Figure 84 — Modification contrôlée d’un fichier surveillé. 

Détection 

La plateforme est ensuite consultée afin de vérifier si la modification est détectée. 

Figure 85-86 — Détection de la modification du fichier dans Wazuh. 

Analyse 

Ce scénario permet d’évaluer le mécanisme de surveillance des fichiers et de vérifier que les modifications peuvent être identifiées par la plateforme. 

6.8 Scénario 7 — Échecs d’authentification 

Objectif 

Le dernier scénario porte sur les événements d’authentification. 

L’objectif est de vérifier si plusieurs tentatives d’authentification échouées peuvent être collectées et analysées par Wazuh. 

Ce scénario est particulièrement intéressant dans le contexte de la sécurité d’un serveur Linux, car une répétition d’échecs d’authentification peut constituer un indicateur d’activité suspecte. 

Action 

Plusieurs tentatives d’authentification volontairement incorrectes sont réalisées dans l’environnement de laboratoire. 

 

Figure 87 — Génération contrôlée d’échecs d’authentification. 

Détection 

Les événements correspondants sont ensuite recherchés dans Wazuh. 

 

      						Figure 87-91 — Détection des échecs d’authentification par Wazuh et le module ia. 

Analyse 

Ce scénario permet de vérifier que les événements d’authentification sont correctement collectés et que Wazuh peut identifier une répétition de tentatives échouées. 

6.9 Synthèse des résultats 

Les différents scénarios permettent d’évaluer la solution selon plusieurs dimensions : surveillance des ressources, collecte des événements, détection des comportements inhabituels et visualisation des résultats. 

Une synthèse des tests réalisés peut être présentée sous la forme suivante : 

 

 

 

Scénario 

Wazuh 

Grafana 

Module IA 

Résultat 

Surcharge CPU 

Faible (pas d'alerte sécu) 

Excellent (Courbe 100%) 

Détection Anomalie 

Succès 

Forte RAM 

Faible 

Excellent (Barre pleine) 

Détection Anomalie 

Succès 

Processus 

Inventaire (Visible) 

Moyen (Load average) 

Moyen 

Partiel 

Port Réseau 

Inventaire (Visible) 

Moyen (Trafic) 

Moyen 

Partiel 

Erreurs Logs 

Excellent (Centralisation) 

Non applicable 

Moyen 

Succès 

Fichier Modifié 

Excellent (FIM) 

Non applicable 

Non applicable 

Succès 

Auth Échouée 

Excellent (Corrélation) 

Non applicable 

Détection Anomalie 

Succès  

Grafana ne voit pas les fichiers modifiés. 

Wazuh ne voit pas les pics de CPU "légitimes" mais suspects. 

L'IA donne un contexte "statistique" que les autres n'ont pas. 

Cette synthèse permettra de comparer rapidement les capacités des différents composants de la plateforme. 

6.10 Analyse globale 

Les tests réalisés permettent d’évaluer la plateforme dans différentes situations contrôlées. 

Les trois composants apportent une supervision complémentaire : 

Wazuh : collecte et analyse des événements de sécurité ;  

Grafana : visualisation des principales métriques système ;  

Module IA : identification des comportements s’écartant du fonctionnement normal.  

L’analyse des résultats porte notamment sur la qualité des détections, les faux positifs et négatifs, les délais de détection et la complémentarité entre les différents mécanismes. 

Ces résultats servent de base au bilan présenté dans le chapitre suivant. 

 

6.11 Conclusion du chapitre 

Les scénarios réalisés ont permis de confronter la solution à différents comportements pouvant affecter un serveur Ubuntu. 

Cette phase expérimentale permet ainsi de valider le fonctionnement pratique de l’architecture et d’évaluer l’atteinte des objectifs définis au début du projet. 
