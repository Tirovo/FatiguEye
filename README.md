# 👁️ EyeTrackR – Détection de fatigue par webcam

> 🧠 Détection de micro-somnolence et de fatigue oculaire en temps réel grâce au suivi du regard via une webcam standard.

---

## 🎯 Objectif

**EyeTrackR** est un projet de vision par ordinateur qui permet d'analyser l'état de vigilance d'une personne en utilisant une simple webcam. Le système détecte :
- Le clignement des yeux
- La durée de fermeture des paupières
- Les signes de micro-sommeil ou de baisse d'attention

Il est conçu pour fonctionner en temps réel et fournir des **alertes intelligentes** en cas de fatigue détectée.

---

## 🔧 Technologies utilisées

| Composant        | Rôle                                      |
|------------------|-------------------------------------------|
| Python           | Langage principal                         |
| OpenCV           | Capture vidéo & affichage                 |
| Mediapipe        | Suivi précis des yeux et du visage        |
| NumPy            | Calculs mathématiques (EAR, stats)        |
| Streamlit        | Interface web minimaliste et réactive     |

---

## 🧠 Fonctionnement

Le système repose sur le **EAR (Eye Aspect Ratio)** :
- Mesure la hauteur/largeur de l’œil à partir des landmarks faciaux.
- Un ratio faible indique un œil fermé.

**Pipeline principal** :
1. Détection du visage et des yeux (landmarks)
2. Calcul du EAR en temps réel
3. Suivi des clignements + durées de fermeture
4. Affichage + Alerte si seuils dépassés

---

## 🚀 Lancer l'application

```bash
git clone https://github.com/ton-user/eyetrackr.git
cd eyetrackr
pip install -r requirements.txt
streamlit run app.py
