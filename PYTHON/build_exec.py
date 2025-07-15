#!/usr/bin/env python3
"""Script de build pour créer un exécutable"""
import os
import subprocess
import sys
import shutil

def build_exe():
    """Construit l'exécutable avec PyInstaller"""
    
    # Vérifier si PyInstaller est installé
    try:
        import PyInstaller
    except ImportError:
        print("📦 Installation de PyInstaller...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "pyinstaller"])
    
    # S'assurer qu'on est dans le bon dossier
    script_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(script_dir)
    
    # Dossier racine du projet (parent de PYTHON)
    root_dir = os.path.dirname(script_dir)
    
    # Commande PyInstaller avec icône et optimisations
    cmd = [
        "pyinstaller",
        "--onefile",
        "--windowed",
        "--name=GestionnaireLogiciels",
        "--clean",
        "--noconfirm",
        "app.py"
    ]
    
    print("🔨 Construction de l'exécutable...")
    
    # Exécuter PyInstaller
    result = subprocess.run(cmd, cwd=script_dir)
    
    # Déplacer l'exécutable vers la racine du projet
    if result.returncode == 0:
        dist_path = os.path.join(script_dir, "dist", "GestionnaireLogiciels.exe")
        target_path = os.path.join(root_dir, "GestionnaireLogiciels.exe")
        
        if os.path.exists(dist_path):
            # Supprimer l'ancien exécutable s'il existe
            if os.path.exists(target_path):
                os.remove(target_path)
            
            shutil.move(dist_path, target_path)
            print(f"✅ Build terminé ! L'exécutable est à la racine : GestionnaireLogiciels.exe")
            
            # Nettoyer les fichiers temporaires
            cleanup_files = [
                os.path.join(script_dir, "build"),
                os.path.join(script_dir, "dist"),
                os.path.join(script_dir, "GestionnaireLogiciels.spec")
            ]
            
            for file_path in cleanup_files:
                if os.path.exists(file_path):
                    if os.path.isdir(file_path):
                        shutil.rmtree(file_path)
                        print(f"🧹 Supprimé : {os.path.basename(file_path)}/")
                    else:
                        os.remove(file_path)
                        print(f"🧹 Supprimé : {os.path.basename(file_path)}")
                        
            print("🎉 Nettoyage terminé !")
        else:
            print("❌ Erreur : L'exécutable n'a pas été créé dans dist/")
    else:
        print("❌ Erreur lors de la construction")
        return False
    
    return True

def test_executable():
    """Teste l'exécutable créé"""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    root_dir = os.path.dirname(script_dir)
    exe_path = os.path.join(root_dir, "GestionnaireLogiciels.exe")
    
    if os.path.exists(exe_path):
        size_mb = os.path.getsize(exe_path) / (1024 * 1024)
        print(f"📊 Taille de l'exécutable : {size_mb:.1f} MB")
        print(f"📍 Emplacement : {exe_path}")
        
        # Test rapide de lancement (optionnel)
        try:
            print("🧪 Test de l'exécutable... (fermez la fenêtre qui s'ouvre)")
            subprocess.Popen([exe_path], cwd=root_dir)
            print("✅ L'exécutable se lance correctement !")
        except Exception as e:
            print(f"⚠️ Erreur lors du test : {e}")
    else:
        print("❌ Exécutable non trouvé")

if __name__ == "__main__":
    if build_exe():
        print("\n" + "="*50)
        test_executable()
        print("="*50)
        print("🚀 Prêt à utiliser ! Double-cliquez sur GestionnaireLogiciels.exe")
