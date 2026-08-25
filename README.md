# ubuntu-ai-monitoring-wazuh-grafana
Lab académique M1 SSI - Surveillance intelligente Ubuntu avec Wazuh, Grafana et IA.
# 🛡️ Surveillance Intelligente Ubuntu – Lab Académique M1 SSI

> Projet personnel réalisé dans le cadre du Master 1 Sécurité des Systèmes d'Information (ESMT 2025-2026)  
> Auteur : Kasongo Mashika Samuel Evariste

## 🎯 Objectif
Plateforme de surveillance combinant **Wazuh** (SIEM), **Grafana** (visualisation) et un **module IA Python** pour détecter automatiquement les anomalies comportementales sur un serveur Ubuntu.

## 🏗️ Architecture du Lab
- **VM1 (192.168.86.141)** : Ubuntu Server cible + Wazuh Agent
- **VM2 (192.168.86.145)** : Wazuh Manager + Indexer + Dashboard  
- **VM3 (192.168.86.144)** : Grafana + Module IA Python

##  Démarrage Rapide
```bash
git clone https://github.com/samuelmashika/ubuntu-ai-monitoring-wazuh-grafana.git
cd ubuntu-ai-monitoring-wazuh-grafana

# Installer Wazuh Manager
chmod +x scripts/install_wazuh.sh && ./scripts/install_wazuh.sh

# Lancer le module IA
pip install -r scripts/requirements.txt
python scripts/anomaly_detection.py
