import psutil 

import pandas as pd  

import numpy as np  

from sklearn.ensemble import IsolationForest  

import time  

import json 

--- Configuration --- 

HISTORY_SIZE = 50 # Nombre de points de données pour apprendre le "normal" THRESHOLD = -0.5 # Seuil de sensibilité (plus proche de 0 = plus sensible) 

class AnomalyDetector:  

def init(self): self.data_history = [] self.model = IsolationForest(contamination=0.1, random_state=42) self.is_trained = False  

def collect_metrics(self): 
    """Collecte CPU, RAM et Swap en temps réel.""" 
    cpu = psutil.cpu_percent(interval=1) 
    mem = psutil.virtual_memory().percent 
    swap = psutil.swap_memory().percent if psutil.swap_memory().total > 0 else 0 
    return [cpu, mem, swap] 
 
def train_model(self): 
    """Phase d'apprentissage : on collecte des données 'normales'.""" 
    print("🔄 Phase d'apprentissage du comportement normal...") 
    for _ in range(HISTORY_SIZE): 
        metrics = self.collect_metrics() 
        self.data_history.append(metrics) 
        time.sleep(2) # Attendre 2s entre chaque mesure 
     
    df = pd.DataFrame(self.data_history, columns=['CPU', 'RAM', 'Swap']) 
    self.model.fit(df) 
    self.is_trained = True 
    print("✅ Modèle entraîné sur le comportement normal.") 
 
def detect(self): 
    """Analyse une nouvelle observation.""" 
    if not self.is_trained: 
        return "Non entraîné", 0.0 
 
    current_metrics = self.collect_metrics() 
    df_current = pd.DataFrame([current_metrics], columns=['CPU', 'RAM', 'Swap']) 
     
    # Prédiction : -1 pour anomalie, 1 pour normal 
    prediction = self.model.predict(df_current)[0] 
    # Score : plus il est négatif, plus c'est anormal 
    score = self.model.score_samples(df_current)[0]  
 
    status = "ANORMAL ⚠️" if prediction == -1 else "NORMAL ✅" 
    return status, score 
  

--- Exécution --- 

if name == "main": detector = AnomalyDetector() 

# 1. Apprentissage 
detector.train_model() 
 
# 2. Surveillance en continu 
print("\n Démarrage de la surveillance...") 
try: 
    while True: 
        status, score = detector.detect() 
        print(f"[{time.strftime('%H:%M:%S')}] Statut: {status} | Score: {score:.4f}") 
        time.sleep(5) 
except KeyboardInterrupt: 
    print("\n Arrêt du module.") 
