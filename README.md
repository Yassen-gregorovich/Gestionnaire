# 🚀 Gestionnaire de Logiciels Windows

![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Platform](https://img.shields.io/badge/platform-Windows-lightgrey.svg)
![Version](https://img.shields.io/badge/version-2.0-brightgreen.svg)
![Branch](https://img.shields.io/badge/branch-main-blue.svg)
![GitHub](https://img.shields.io/badge/GitHub-Yassen--gregorovich%2FGestionnaire-black.svg?logo=github)

Un gestionnaire de logiciels Windows moderne et compact avec interface graphique permettant d'installer et gérer facilement vos applications préférées.

## ✨ Fonctionnalités

- ✅ **Interface moderne** : Thème personnalisé, sélection globale (☑), ajustement auto de taille
- 🛠️ **5 types d'installation** : WINGET, EXE, MSI, PowerShell, CMD avec regroupement intelligent des terminaux
- 📋 **Gestion avancée** : Lots, réorganisation, sauvegarde/chargement de configurations
- 📝 **Logs complets** : Journalisation quotidienne avec traçabilité (`logs/gestionnaire_YYYYMMDD.log`)
- 🛡️ **Robuste** : Gestion d'erreurs, détection admin, installation non-bloquante

## 📦 Installation

### Prérequis
- Windows 10/11, Python 3.8+, Winget

### Installation rapide
```bash
git clone https://github.com/votre-username/Gestionnaires.git
cd Gestionnaires && pip install -r requirements.txt
python PYTHON/app.py
```

## 🎮 Utilisation

1. **Lancer** : `python PYTHON/app.py`
2. **Ajouter** : ➕ → Configurer nom/type/commande
3. **Sélectionner** : ☑ (tout) ou cocher individuellement  
4. **Installer** : ▶️ → Suivre le progrès

### Types supportés

| Type | Exemple | Terminal |
|------|---------|----------|
| 🛠️ **WINGET** | `Microsoft.VisualStudioCode` | Intégré |
| 📦 **EXE/MSI** | `C:\path\to\installer.exe` | Intégré |
| ⚡ **PowerShell/CMD** | `Install-Module Az` | **Regroupé** |

> 💡 **Nouveau** : PowerShell et CMD regroupés dans une seule fenêtre par type !

## 📁 Structure

```
Gestionnaires/
├── PYTHON/app.py           # Application principale
├── PRESETS/               # Configurations (default.json, dev-tools.json...)
├── logs/                  # Logs quotidiens automatiques
└── INFO/                  # Documentation
```

## 🛠️ Développement

### Contribuer
```bash
git checkout -b feature/nom-feature
# Développer avec logging approprié
git commit -m 'Add: nouvelle fonctionnalité'
git push origin feature/nom-feature
# Créer Pull Request
```

### Architecture
- **Framework** : Tkinter + thèmes personnalisés
- **Logging** : Logs rotatifs quotidiens  
- **Threading** : Installation non-bloquante
- **Subprocess** : Terminaux optimisés

## 📈 Roadmap

### Prochaines versions
- [ ] 🌐 Interface web (React + API)
- [ ] 🐧 Support Linux/macOS
- [ ] 🔌 Système de plugins
- [ ] 🤫 Mode silencieux
- [ ] 🎨 Thèmes personnalisables

### Vision long terme  
- [ ] ☁️ Sync cloud des configs
- [ ] 📊 Dashboard avec stats
- [ ] 🤖 IA pour recommandations
- [ ] 👥 Partage communautaire

## 📊 Performance

- ⚡ Démarrage : < 2s | 💾 RAM : ~15-30 MB | 📦 Taille : ~500 KB
- 🔧 Configs : Illimitées | 🖥️ Terminaux : Optimisé (1 par type)

## 🤝 Support

- 🐛 [Issues](https://github.com/votre-username/Gestionnaires/issues)
- 💬 [Discussions](https://github.com/votre-username/Gestionnaires/discussions)
- 📖 Logs : `logs/gestionnaire_YYYYMMDD.log`

## 📄 Licence

MIT License - Libre d'utilisation commerciale et personnelle.

---

<div align="center">

**⭐ Si ce projet vous aide, donnez-lui une étoile ! ⭐**

[![GitHub stars](https://img.shields.io/github/stars/votre-username/Gestionnaires?style=social)](https://github.com/votre-username/Gestionnaires)

*Développé avec ❤️ pour simplifier la gestion de logiciels Windows*

</div>

## ✨ Fonctionnalités

### 🎨 Interface & Expérience Utilisateur
- ✅ Interface graphique moderne avec thème personnalisé
- 🎯 Design compact et épuré sans sacrifier les fonctionnalités
- 🖱️ Sélection/désélection globale avec un seul clic (☑)
- 📊 Indicateur de privilèges administrateur en temps réel
- 🔄 Ajustement automatique de la taille de fenêtre selon le contenu

### 📦 Gestion des Applications
- �️ Support de 5 types d'installation (WINGET, EXE, MSI, PowerShell, CMD)
- 📋 Gestion par lots avec sélection multiple intelligente
- ⬆️⬇️ Réorganisation par glisser-déposer et boutons dédiés
- �️ Sauvegarde et chargement de configurations personnalisées
- � Parcourir et sélectionner des fichiers avec explorateur intégré

### 🚀 Installation & Exécution
- ⚡ Installation en lot avec suivi en temps réel et barre de progression
- 🖥️ **Nouveau** : Regroupement intelligent des terminaux (une seule fenêtre CMD/PowerShell)
- 📝 Journalisation complète avec logs quotidiens automatiques
- ⏱️ Timestamps précis pour chaque action et installation
- 🛡️ Gestion d'erreurs robuste avec rapports détaillés

### 📊 Monitoring & Logs
- 📅 Système de logs quotidiens (`logs/gestionnaire_YYYYMMDD.log`)
- 🔍 Traçabilité complète des actions et installations
- ⚠️ Niveaux de log (INFO, ERROR) pour un débogage facile
- 📈 Suivi des performances et statistiques d'installation

## 📦 Installation

### Prérequis
- 🖥️ Windows 10/11 (x64)
- 🐍 Python 3.8 ou supérieur
- 📦 Winget (inclus dans Windows 11, disponible sur Windows 10)
- 🛡️ Privilèges administrateur recommandés pour certaines installations

### Installation rapide
```bash
# Cloner le repository
git clone https://github.com/votre-username/Gestionnaires.git
cd Gestionnaires

# Installer les dépendances
pip install -r requirements.txt

# Lancer l'application
python PYTHON/app.py
```

### Installation portable
```bash
# Télécharger et extraire le ZIP
# Aucune installation Python requise avec la version portable
# Double-cliquer sur gestionnaire.exe
```

## 🎮 Utilisation

### 🚀 Démarrage rapide
1. **Lancez l'application** : `python PYTHON/app.py`
2. **Ajoutez des logiciels** : Cliquez sur "➕ Ajouter"
3. **Configurez** : Remplissez le nom, type et commande
4. **Sélectionnez** : Utilisez ☑ pour tout sélectionner ou cochez individuellement
5. **Installez** : Cliquez sur "▶️ INSTALLER" et suivez le progrès

### 🎯 Fonctions avancées
- **🔄 Réorganisation** : Utilisez "⬆️ Monter" et "⬇️ Descendre" pour ordonner vos apps
- **💾 Sauvegarde** : "Sauvegarder" pour exporter votre configuration
- **📂 Import** : "Ouvrir" pour charger une configuration existante
- **🗑️ Nettoyage** : Sélectionnez et "❌ Supprimer" les apps non désirées

### Types d'installation supportés

| Type | Description | Exemple | Terminal |
|------|-------------|---------|----------|
| 🛠️ **WINGET** | Gestionnaire de paquets Windows officiel | `Microsoft.VisualStudioCode` | Intégré |
| 📦 **EXE** | Fichiers exécutables standard | `C:\path\to\installer.exe` | Intégré |
| 🔧 **MSI** | Packages Windows Installer | `C:\path\to\package.msi` | Intégré |
| ⚡ **POWERSHELL** | Scripts et commandes PowerShell | `Install-Module -Name Az` | **Regroupé** |
| 🖥️ **CMD** | Commandes système et batch | `choco install firefox` | **Regroupé** |

> 💡 **Nouveau** : Les commandes PowerShell et CMD sont maintenant regroupées dans une seule fenêtre de terminal par type, évitant le spam de fenêtres !

## 📁 Structure du Projet

```
Gestionnaires/
├── 📂 PYTHON/              # 🐍 Code source principal
│   ├── app.py              # Application principale (compact & optimisé)
│   └── Config/             # (Deprecated - migrée vers PRESETS)
├── 📂 PRESETS/             # ⚙️ Configurations prédéfinies
│   ├── default.json        # Configuration par défaut
│   ├── dev-tools.json      # Outils de développement
│   ├── multimedia.json     # Applications multimédia
│   └── office.json         # Suite bureautique
├── 📂 logs/                # 📝 Logs quotidiens automatiques
│   └── gestionnaire_YYYYMMDD.log
├── 📂 INFO/                # 📚 Documentation
│   ├── Projets.txt         # Projets et idées
│   ├── Problèmes.txt       # Issues connues
│   └── Wiki.txt            # Guide utilisateur
├── 📂 EXE/                 # 🚀 Exécutables compilés
├── 📄 README.md            # Ce fichier
└── 📄 .gitignore          # Configuration Git
```

## 📋 Configurations Prédéfinies

### 🛠️ Développement (`dev-tools.json`)
- Visual Studio Code, Git, Node.js, Python, Docker
- Extensions et outils CLI essentiels

### 🎨 Multimédia (`multimedia.json`) 
- VLC, GIMP, OBS Studio, Audacity, HandBrake
- Codecs et plugins multimédia

### 📊 Bureautique (`office.json`)
- LibreOffice, PDF Creator, Notepad++
- Outils de productivité

### 🎮 Gaming & Utilitaires
- Steam, Discord, 7-Zip, CCleaner
- Optimiseurs et outils système

## 🛠️ Développement & Contribution

### Architecture technique
- **Framework** : Tkinter avec thèmes personnalisés
- **Logging** : Système de logs quotidiens rotatifs
- **Configuration** : JSON avec validation de schéma
- **Threading** : Installation non-bloquante en arrière-plan
- **Subprocess** : Gestion optimisée des terminaux externes

### 🤝 Contribuer
1. **Fork** le projet sur GitHub
2. **Clone** votre fork : `git clone https://github.com/votre-username/Gestionnaires.git`
3. **Créez** une branche : `git checkout -b feature/amazing-feature`
4. **Développez** avec les bonnes pratiques :
   - Code compact et lisible
   - Logging approprié
   - Tests sur Windows 10/11
5. **Committez** : `git commit -m 'Add: amazing feature'`
6. **Push** : `git push origin feature/amazing-feature`
7. **Pull Request** avec description détaillée

### 🐛 Debugging
- Consultez les logs dans `logs/gestionnaire_YYYYMMDD.log`
- Activez le mode verbeux en modifiant le niveau de log
- Testez avec privilèges administrateur et utilisateur standard

## 🔄 Changelog & Versions

### Version 2.0 (Actuelle)
- ✅ Regroupement des terminaux CMD/PowerShell
- ✅ Système de logging complet
- ✅ Code ultra-compact sans perte de fonctionnalités
- ✅ Migration vers dossier PRESETS
- ✅ Interface utilisateur optimisée

### Version 1.x
- Interface graphique de base
- Support multi-types d'installation
- Sauvegarde de configurations

## 📝 Licence

Ce projet est sous licence MIT. Voir le fichier [LICENSE](LICENSE) pour plus de détails.

### � Résolution de problèmes
1. **Vérifiez** les logs dans `logs/`
2. **Consultez** les issues existantes
3. **Décrivez** précisément votre problème avec :
   - Version Windows
   - Logs d'erreur
   - Étapes de reproduction

## �📈 Roadmap & Futures Fonctionnalités

### 🎯 Prochaines versions (Q3-Q4 2025)
- [ ] 🌐 Interface web complémentaire (React + API)
- [ ] 🐧 Support Linux/macOS (version multiplateforme)
- [ ] 🔌 Système de plugins pour gestionnaires tiers
- [ ] 📡 API REST pour intégration dans d'autres outils
- [ ] 🤫 Mode silencieux pour déploiements automatiques
- [ ] 🎨 Thèmes personnalisables (sombre, clair, couleurs)

### 🚀 Vision long terme
- [ ] ☁️ Synchronisation cloud des configurations
- [ ] 📊 Tableau de bord avec statistiques avancées
- [ ] 🤖 IA pour recommandations de logiciels
- [ ] 🔄 Auto-update des applications installées
- [ ] 👥 Partage de configurations communautaires

## 📊 Statistiques & Performance

- ⚡ **Temps de démarrage** : < 2 secondes
- 💾 **Empreinte mémoire** : ~15-30 MB
- 📦 **Taille application** : ~500 KB (Python), ~15 MB (portable)
- 🔧 **Configurations supportées** : Illimitées
- 🖥️ **Terminaux simultanés** : Optimisé (1 par type)

---

## 📄 Licence

Ce projet est sous licence MIT. Voir le fichier [LICENSE](LICENSE) pour tous les détails.

```
MIT License - Vous êtes libre de :
✅ Utiliser commercialement
✅ Modifier et distribuer  
✅ Placer sous licence privée
✅ Utiliser à des fins personnelles
```

---

<div align="center">

### 🌟 Remerciements

Merci à tous les contributeurs et utilisateurs qui font vivre ce projet !

**[⬆️ Retour en haut](#-gestionnaire-de-logiciels-windows)**

</div>
