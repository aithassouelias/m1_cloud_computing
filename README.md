# TalentTracker - Détectez les Étoiles Montantes du Football 🎯

**TalentTracker** est une application interactive conçue pour analyser les statistiques des joueurs et nations de football afin d’identifier les meilleurs talents. Que vous soyez sélectionneur national ou recruteur de club, cet outil vous aide à repérer les profils idéaux pour renforcer votre équipe.  

**Lien de l'application déployée** : [TalentTracker sur Azure](https://talent-tracker.azurewebsites.net/Accueil)  

---

### 🚀 **Fonctionnalités**
Analyser et découvrir des talents dans le monde du football grâce à des outils de visualisation et d’analyse avancés.

#### 1. **Explorez les talents de chaque nation**
- **Objectif** : Identifier des talents spécifiques dans une nation.  
- **Comment ?** :  
  - Appliquez des filtres par pays et par poste.  
  - Consultez des statistiques détaillées telles que la moyenne d’âge, la note générale moyenne, le nombre de joueurs par poste.
- **Exemple pratique** :  
  *Le sélectionneur d’une équipe nationale peut rechercher des joueurs pour des postes clés avant une compétition majeure comme la Coupe du Monde.*  

#### 2. **Trouvez le joueur qu'il vous faut**
- **Objectif** : Rechercher des joueurs similaires à un profil donné.  
- **Comment ?** :  
  - Sélectionnez un joueur.  
  - L’algorithme **K-Nearest Neighbors (K-NN)** compare ses caractéristiques à d'autres joueurs et propose les 5 profils les plus proches.  
- **Exemple pratique** :  
  *Identifier un remplaçant pour Kylian Mbappé au PSG en analysant des profils similaires.*  

---

## 🛠️ **Technologies Utilisées**
- **Langage principal** : Python  
- **Framework** : Streamlit  
- **Déploiement** : Azure App Service  
- **Bibliothèques clés** :  
  - `pandas` : Manipulation des données.  
  - `plotly-express` : Visualisations interactives.  
  - `scikit-learn` : Algorithmes de Machine Learning (K-NN).  

---

## ⚡ **Démo Rapide**
1. **Choisissez un pays** dans le filtre et explorez les talents disponibles.  
2. **Sélectionnez un joueur** pour trouver des profils similaires grâce à l'algorithme K-NN.  
3. Analysez les statistiques et comparez les options pour trouver la meilleure recrue.   

---

## 🏗️ **Installation et Exécution Locale**
1. Clonez ce dépôt :  
   ```bash
   git clone https://github.com/aithassouelias/scooting-football-app.git
   ```

2. Installez les dépendences :  
   ```bash
   pip install -r requirements.txt
   ```

3. Lancez l'application :  
   ```bash
   streamlit run app.py
   ```

---
## Sources de données :
- Male players FC25 : https://www.kaggle.com/datasets/nyagami/ea-sports-fc-25-database-ratings-and-stats
- Flags DataSet : https://www.kaggle.com/datasets/zhongtr0n/country-flag-urls