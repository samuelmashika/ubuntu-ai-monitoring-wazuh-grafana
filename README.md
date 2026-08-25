cat > README.md << 'EOF'
# 🛡️ Surveillance Intelligente Ubuntu – Lab Académique M1 SSI

> Projet personnel réalisé dans le cadre du Master 1 Sécurité des Systèmes d'Information (ESMT 2025-2026)  
> Auteur : Kasongo Mashika Samuel Evariste

## 🎯 Objectif
Plateforme de surveillance combinant **Wazuh** (SIEM), **Grafana** (visualisation) et un **module IA Python** pour détecter automatiquement les anomalies comportementales sur un serveur Ubuntu.

## 🏗️ Architecture du Lab
- **VM1 (192.168.86.137)** : Ubuntu Server cible + Wazuh Agent
- **VM2 (192.168.86.139)** : Wazuh Manager + Indexer + Dashboard  
- **VM3 (192.168.86.141)** : Grafana + Module IA Python

![Architecture](screenshots/01_screenshot.png)

## 📊 Résultats Clés
| Scénario | Wazuh | IA | Temps |
|----------|-------|-----|-------|
| CPU >90% | ✅ Level 8 | ✅ Score 0.92 | <15s |
| Bruteforce SSH | ✅ Level 10 | N/A | <5s |
| Processus suspect | ⚠️ Partiel | ✅ Score 0.87 | <30s |

## 📁 Structure
- `docs/` – Documentation technique complète
- `scripts/` – Scripts Bash/Python reproductibles
- `config/` – Configurations Wazuh exportées
- `screenshots/` – Preuves visuelles du lab

## 🎓 Compétences Démontrées
- SIEM Operations (Wazuh tuning, règles personnalisées)
- Security Monitoring (Grafana dashboards temps réel)
- Anomaly Detection (IA comportementale complémentaire)
- Linux Administration (hardening, scripting, systemd)
EOF
