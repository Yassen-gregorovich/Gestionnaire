#!/usr/bin/env python3
import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import json, os, subprocess, threading
from datetime import datetime

THEME = {
    "PRIMAIRE": "#e1e1e1", "FOND": "#f0f0f0", "TEXTE": "#000000", "SURVOL": "#e5f3ff", 
    "CLIC": "#cce4f7", "TITRES": "#e1e1e1", "CHAMPS": "#ffffff", "BORDURES": "#adadad", 
    "SELECTION": "#0078d4", "TEXTE_SEL": "#ffffff"
}

class GestionnaireApps:
    def __init__(self):
        self.apps = []
        dossier_parent = os.path.dirname(os.path.dirname(__file__))
        self.config_file = os.path.join(dossier_parent, "PRESETS", "default.json")
        self.logs_dir = os.path.join(dossier_parent, "logs")
        os.makedirs(os.path.dirname(self.config_file), exist_ok=True)
        os.makedirs(self.logs_dir, exist_ok=True)
        
        self.root = tk.Tk()
        self.root.title("")
        self.root.geometry("580x360")
        self.root.configure(bg=THEME["FOND"])
        self.configurer_styles()
        self.creer_interface()
        self.charger_config()
        self.ajuster_taille_fenetre()

    def configurer_styles(self):
        self.style = ttk.Style()
        self.style.theme_use('clam')
        
        styles = {
            "P.TButton": {"background": THEME["PRIMAIRE"], "foreground": THEME["TEXTE"], "borderwidth": 1, "relief": "solid", "bordercolor": THEME["BORDURES"], "focuscolor": "none", "padding": (10, 5)},
            "B.TButton": {"background": THEME["PRIMAIRE"], "foreground": THEME["TEXTE"], "borderwidth": 1, "relief": "solid", "bordercolor": THEME["BORDURES"], "focuscolor": "none", "padding": (6, 4), "font": ("Segoe UI", 10)},
            "P.TFrame": {"background": THEME["FOND"]}, 
            "P.TLabelframe": {"background": THEME["FOND"], "bordercolor": THEME["BORDURES"], "borderwidth": 1},
            "P.TLabelframe.Label": {"background": THEME["FOND"], "foreground": THEME["TEXTE"], "font": ("Segoe UI", 9, "bold")},
            "P.TLabel": {"background": THEME["FOND"], "foreground": THEME["TEXTE"], "font": ("Segoe UI", 9)},
            "T.TLabel": {"background": THEME["FOND"], "foreground": THEME["TEXTE"], "font": ("Segoe UI", 16, "bold")},
            "P.TCheckbutton": {"background": THEME["FOND"], "foreground": THEME["TEXTE"], "focuscolor": "none"},
            "P.Vertical.TScrollbar": {"background": THEME["TITRES"], "bordercolor": THEME["BORDURES"], "arrowcolor": THEME["TITRES"], "darkcolor": THEME["TITRES"], "lightcolor": THEME["TITRES"], "troughcolor": THEME["FOND"], "borderwidth": 1},
            "P.Horizontal.TProgressbar": {"background": THEME["SELECTION"], "troughcolor": THEME["FOND"], "bordercolor": THEME["BORDURES"], "borderwidth": 1}
        }
        for style, config in styles.items(): 
            self.style.configure(style, **config)
        
        self.style.configure("P.TEntry", fieldbackground=THEME["CHAMPS"], bordercolor=THEME["BORDURES"], borderwidth=1)
        self.style.configure("P.TCombobox", fieldbackground=THEME["CHAMPS"], bordercolor=THEME["BORDURES"], borderwidth=1, selectbackground=THEME["CHAMPS"], selectforeground=THEME["TEXTE"], arrowcolor=THEME["TEXTE"])
        
        maps = {
            "P.TButton": {"background": [('active', THEME["SURVOL"]), ('pressed', THEME["CLIC"])], "relief": [('pressed', 'sunken')]}, 
            "B.TButton": {"background": [('active', THEME["SURVOL"]), ('pressed', THEME["CLIC"])], "relief": [('pressed', 'sunken')]}, 
            "P.TCombobox": {"fieldbackground": [('readonly', THEME["CHAMPS"]), ('disabled', THEME["CHAMPS"]), ('focus', THEME["CHAMPS"]), ('!focus', THEME["CHAMPS"])], "selectbackground": [('readonly', THEME["CHAMPS"]), ('focus', THEME["CHAMPS"]), ('!focus', THEME["CHAMPS"])], "selectforeground": [('readonly', THEME["TEXTE"]), ('focus', THEME["TEXTE"]), ('!focus', THEME["TEXTE"])], "bordercolor": [('focus', THEME["SELECTION"])]}, 
            "P.TCheckbutton": {"background": [('active', THEME["FOND"])]}, 
            "P.Vertical.TScrollbar": {"background": [('active', THEME["SURVOL"])], "arrowcolor": [('active', THEME["TEXTE"])]}, 
            "P.TEntry": {"selectbackground": [('focus', THEME["SELECTION"]), ('!focus', THEME["SELECTION"])], "selectforeground": [('focus', THEME["TEXTE_SEL"]), ('!focus', THEME["TEXTE_SEL"])], "fieldbackground": [('focus', THEME["CHAMPS"])], "bordercolor": [('focus', THEME["SELECTION"])]}
        }
        for style, mapping in maps.items():
            for prop, values in mapping.items(): 
                self.style.map(style, **{prop: values})

    def creer_interface(self):
        header = ttk.Frame(self.root, style="P.TFrame")
        header.pack(fill="x", padx=10, pady=5)
        ttk.Label(header, text="Gestionnaire Logiciels Windows", style="T.TLabel").pack(side="left")
        admin_text = "🛡️ Administrateur" if self.est_admin() else "⚠️ Utilisateur standard"
        ttk.Label(header, text=admin_text, style="P.TLabel").pack(side="right")
        
        main = ttk.Frame(self.root, style="P.TFrame")
        main.pack(fill="both", expand=True, padx=10, pady=5)
        
        left = ttk.LabelFrame(main, text="Actions", style="P.TLabelframe", width=140, padding="6")
        left.pack(side="left", fill="y", padx=(0,10), pady=10)
        left.pack_propagate(False)
        
        actions = [("➕ Ajouter", self.ajouter_app), ("✏️ Modifier", self.modifier_app), ("❌ Supprimer", self.supprimer_apps), ("⬆️ Monter", self.monter), ("⬇️ Descendre", self.descendre)]
        for text, cmd in actions:
            ttk.Button(left, text=text, command=cmd, style="P.TButton").pack(fill="x", pady=2)
        
        self.label_statut = ttk.Label(left, text="0 apps", style="P.TLabel")
        self.label_statut.pack(pady=10)
        ttk.Button(left, text="▶️ INSTALLER", command=self.executer_apps, style="P.TButton").pack(fill="x", pady=2)
        
        right = ttk.LabelFrame(main, text="Applications", style="P.TLabelframe", padding="10")
        right.pack(side="right", fill="both", expand=True, pady=10)
        
        toolbar = ttk.Frame(right, style="P.TFrame")
        toolbar.pack(fill="x", pady=(0,5))
        
        left_buttons = ttk.Frame(toolbar, style="P.TFrame")
        left_buttons.pack(side="left")
        ttk.Button(left_buttons, text="☑", command=self.basculer_tout, style="P.TButton", width=3).pack(side="left", padx=2)
        
        right_buttons = ttk.Frame(toolbar, style="P.TFrame")
        right_buttons.pack(side="right")
        fichier_actions = [("Nouveau", self.nouvelle_config), ("Ouvrir", self.ouvrir_config), ("Sauvegarder", self.sauver_config)]
        for text, cmd in fichier_actions:
            ttk.Button(right_buttons, text=text, command=cmd, style="P.TButton").pack(side="left", padx=2)
        
        list_frame = ttk.Frame(right, style="P.TFrame")
        list_frame.pack(fill="both", expand=True, pady=5)
        
        self.canvas = tk.Canvas(list_frame, bg=THEME["FOND"], highlightthickness=0, relief="flat")
        scrollbar = ttk.Scrollbar(list_frame, orient="vertical", command=self.canvas.yview, style="P.Vertical.TScrollbar")
        self.frame_deroulant = ttk.Frame(self.canvas, style="P.TFrame")
        
        self.frame_deroulant.bind("<Configure>", lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))
        self.canvas.create_window((0, 0), window=self.frame_deroulant, anchor="nw")
        self.canvas.configure(yscrollcommand=scrollbar.set)
        self.canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        self.canvas.bind("<MouseWheel>", lambda e: self.canvas.yview_scroll(int(-1*(e.delta/120)), "units"))

    def actualiser_affichage(self):
        for widget in self.frame_deroulant.winfo_children(): 
            widget.destroy()
        
        for i, app in enumerate(self.apps):
            app_frame = ttk.Frame(self.frame_deroulant, style="P.TFrame", padding="5")
            app_frame.pack(fill="x", pady=1)
            
            var = tk.BooleanVar(value=app.get("selected", False))
            ttk.Checkbutton(app_frame, variable=var, style="P.TCheckbutton", command=lambda idx=i, v=var: self.basculer_app(idx, v.get())).pack(side="left", padx=5)
            
            info_text = f"{app['name']} ({app['type']})"
            if len(info_text) > 50: 
                info_text = info_text[:47] + "..."
            ttk.Label(app_frame, text=info_text, style="P.TLabel").pack(side="left", fill="x", expand=True, padx=10)
        
        self.frame_deroulant.update_idletasks()
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        selected = sum(1 for app in self.apps if app.get("selected", False))
        status_text = f"{len(self.apps)} logiciels\n{selected} sélectionné{'s' if selected > 1 else ''}" if selected else f"{len(self.apps)} logiciels\nAucune sélection"
        self.label_statut.configure(text=status_text)

    def basculer_app(self, index, selected):
        self.apps[index]["selected"] = selected
        self.sauver_config_auto()
        selected_count = sum(1 for app in self.apps if app.get("selected", False))
        status_text = f"{len(self.apps)} logiciels\n{selected_count} sélectionné{'s' if selected_count > 1 else ''}" if selected_count else f"{len(self.apps)} logiciels\nAucune sélection"
        self.label_statut.configure(text=status_text)

    def basculer_tout(self):
        all_selected = all(app.get("selected", False) for app in self.apps)
        for app in self.apps: 
            app["selected"] = not all_selected
        self.sauver_config_auto()
        self.actualiser_affichage()

    def ajouter_app(self): 
        self.afficher_dialogue_app()

    def modifier_app(self, index=None):
        if index is None:
            selected = [i for i, app in enumerate(self.apps) if app.get("selected", False)]
            if not selected: 
                return messagebox.showwarning("Sélection", "Veuillez sélectionner un logiciel à modifier")
            index = selected[0]
        self.afficher_dialogue_app(self.apps[index], index)
    
    def afficher_dialogue_app(self, app_data=None, index=None):
        dialog = tk.Toplevel(self.root)
        dialog.title("Ajouter" if app_data is None else "Modifier")
        dialog.geometry("450x250")
        dialog.configure(bg=THEME["FOND"])
        dialog.transient(self.root)
        dialog.grab_set()
        dialog.geometry(f"+{self.root.winfo_rootx()+50}+{self.root.winfo_rooty()+50}")
        
        form = ttk.Frame(dialog, padding="20", style="P.TFrame")
        form.pack(fill="both", expand=True)
        
        champs = [
            ("Nom:", "name_entry", ttk.Entry, {"width": 40, "style": "P.TEntry"}),
            ("Type:", "type_combo", ttk.Combobox, {"values": ["WINGET", "EXE", "MSI", "POWERSHELL", "CMD"], "state": "readonly", "width": 15, "style": "P.TCombobox"}),
            ("Commande:", "command_entry", ttk.Entry, {"width": 35, "style": "P.TEntry"}),
            ("Arguments:", "args_entry", ttk.Entry, {"width": 40, "style": "P.TEntry"})
        ]
        
        widgets = {}
        for i, (label, name, widget_class, kwargs) in enumerate(champs):
            ttk.Label(form, text=label, style="P.TLabel").grid(row=i, column=0, sticky="w", pady=5)
            widget = widget_class(form, **kwargs)
            
            if name == "command_entry":
                widget.grid(row=i, column=1, sticky="ew", padx=(10,5), pady=5)
                ttk.Button(form, text="📁", width=3, style="B.TButton", command=lambda: self.parcourir_fichier(widget)).grid(row=i, column=2, padx=5, pady=5)
            else:
                colspan = 2 if name != "type_combo" else 1
                widget.grid(row=i, column=1, columnspan=colspan, sticky="ew" if colspan > 1 else "w", padx=(10,0), pady=5)
            
            widgets[name] = widget
        
        form.columnconfigure(1, weight=1)
        
        if app_data:
            widgets["name_entry"].insert(0, app_data["name"])
            widgets["type_combo"].set(app_data["type"])
            widgets["command_entry"].insert(0, app_data["command"])
            widgets["args_entry"].insert(0, app_data.get("arguments", ""))
        else: 
            widgets["type_combo"].set("WINGET")
        
        btn_frame = ttk.Frame(form, style="P.TFrame")
        btn_frame.grid(row=len(champs), column=0, columnspan=3, pady=20)
        ttk.Button(btn_frame, text="Annuler", style="P.TButton", command=dialog.destroy).pack(side="right", padx=5)
        ttk.Button(btn_frame, text="Sauvegarder", style="P.TButton", command=lambda: self.sauver_dialogue_app(dialog, widgets, index)).pack(side="right")

    def parcourir_fichier(self, entry):
        file_path = filedialog.askopenfilename(filetypes=[("Exécutables", "*.exe"), ("MSI", "*.msi"), ("Tous", "*.*")])
        if file_path:
            entry.delete(0, tk.END)
            entry.insert(0, file_path)

    def sauver_dialogue_app(self, dialog, widgets, index):
        name, command = widgets["name_entry"].get().strip(), widgets["command_entry"].get().strip()
        if not name or not command:
            return messagebox.showerror("Erreur", "Nom et commande requis")
        
        app_data = {"name": name, "type": widgets["type_combo"].get(), "command": command, "arguments": widgets["args_entry"].get().strip(), "selected": False}
        
        if index is not None:
            app_data["selected"] = self.apps[index].get("selected", False)
            self.apps[index] = app_data
            self.ecrire_log(f"Application modifiée: {name}")
        else: 
            self.apps.append(app_data)
            self.ecrire_log(f"Application ajoutée: {name} ({widgets['type_combo'].get()})")
        
        self.sauver_config_auto()
        self.actualiser_affichage()
        dialog.destroy()

    def supprimer_apps(self):
        selected_count = sum(1 for app in self.apps if app.get("selected", False))
        if selected_count == 0:
            return messagebox.showwarning("Sélection", "Veuillez sélectionner des logiciels à supprimer")
        
        if messagebox.askyesno("Confirmer la suppression", f"Supprimer {selected_count} logiciel(s) de la liste ?"):
            apps_supprimees = [app['name'] for app in self.apps if app.get("selected", False)]
            self.ecrire_log(f"Applications supprimées: {', '.join(apps_supprimees)}")
            self.apps = [app for app in self.apps if not app.get("selected", False)]
            self.sauver_config_auto()
            self.actualiser_affichage()

    def executer_apps(self):
        selected_apps = [app for app in self.apps if app.get("selected", False)]
        if not selected_apps:
            return messagebox.showwarning("Sélection", "Veuillez sélectionner des logiciels à installer")
        self.afficher_dialogue_execution(selected_apps)

    def afficher_dialogue_execution(self, apps_to_execute):
        dialog = tk.Toplevel(self.root)
        dialog.title("Installation")
        dialog.geometry("500x350")
        dialog.configure(bg=THEME["FOND"])
        dialog.transient(self.root)
        dialog.grab_set()
        
        main_frame = ttk.Frame(dialog, padding="20", style="P.TFrame")
        main_frame.pack(fill="both", expand=True)
        
        ttk.Label(main_frame, text=f"Installation de {len(apps_to_execute)} logiciel(s)", font=("Segoe UI", 12, "bold"), style="P.TLabel").pack(pady=10)
        
        progress = ttk.Progressbar(main_frame, mode='determinate', length=400, style="P.Horizontal.TProgressbar")
        progress.pack(pady=10)
        
        current_label = ttk.Label(main_frame, text="Préparation", style="P.TLabel")
        current_label.pack(pady=5)
        
        log_frame = ttk.Frame(main_frame, style="P.TFrame")
        log_frame.pack(fill="both", expand=True, pady=10)
        
        log_text = tk.Text(log_frame, height=12, wrap=tk.WORD, font=("Consolas", 9), bg=THEME["CHAMPS"], fg=THEME["TEXTE"])
        log_scroll = ttk.Scrollbar(log_frame, orient="vertical", command=log_text.yview, style="P.Vertical.TScrollbar")
        log_text.configure(yscrollcommand=log_scroll.set)
        log_text.pack(side="left", fill="both", expand=True)
        log_scroll.pack(side="right", fill="y")
        
        close_btn = ttk.Button(main_frame, text="Fermer", style="P.TButton", command=dialog.destroy, state="disabled")
        close_btn.pack(pady=10)
        
        threading.Thread(target=self.thread_execution, args=(apps_to_execute, progress, current_label, log_text, close_btn), daemon=True).start()

    def thread_execution(self, apps, progress, current_label, log_text, close_btn):
        total = len(apps)
        progress.configure(maximum=total)
        self.ecrire_log(f"Début d'installation de {total} application(s)")
        
        cmd_commands = []
        ps_commands = []
        
        for i, app in enumerate(apps):
            current_label.configure(text=f"Installation: {app['name']}")
            progress.configure(value=i)
            
            log_msg = f"[{datetime.now().strftime('%H:%M:%S')}] Installation de {app['name']}\n"
            log_text.insert(tk.END, log_msg)
            log_text.see(tk.END)
            log_text.update()
            
            self.ecrire_log(f"Installation de {app['name']} ({app['type']}) - Commande: {app['command']}")
            
            try:
                cmd = self.construire_commande(app)
                
                if app["type"] == "CMD":
                    cmd_commands.append(f'echo "Installation de {app["name"]}" && {cmd}')
                    status = "✅ Ajouté au batch CMD"
                    self.ecrire_log(f"{app['name']} - Ajouté au batch CMD")
                elif app["type"] == "POWERSHELL":
                    ps_commands.append(f'Write-Host "Installation de {app["name"]}" -ForegroundColor Green; {cmd}')
                    status = "✅ Ajouté au batch PowerShell"
                    self.ecrire_log(f"{app['name']} - Ajouté au batch PowerShell")
                else:
                    result = subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=60)
                    if result.returncode == 0:
                        status = "✅ Installation réussie"
                        self.ecrire_log(f"{app['name']} - Installation réussie")
                    else:
                        status = f"❌ Échec de l'installation: {result.stderr[:50]}"
                        self.ecrire_log(f"{app['name']} - Échec: {result.stderr[:100]}", "ERROR")
            except Exception as e:
                status = f"❌ Erreur: {str(e)[:50]}"
                self.ecrire_log(f"{app['name']} - Erreur: {str(e)}", "ERROR")
            
            log_text.insert(tk.END, f"{status}\n\n")
            log_text.see(tk.END)
            log_text.update()
            
            if i < len(apps) - 1:
                import time
                for countdown in range(3, 0, -1):
                    current_label.configure(text=f"Attente... {countdown}s")
                    current_label.update()
                    time.sleep(1)
        
        if cmd_commands:
            batch_cmd = ' && '.join(cmd_commands) + ' && pause'
            subprocess.Popen(f'start cmd /k "{batch_cmd}"', shell=True)
            log_text.insert(tk.END, f"✅ Fenêtre CMD ouverte avec {len(cmd_commands)} commande(s)\n\n")
            self.ecrire_log(f"Fenêtre CMD ouverte avec {len(cmd_commands)} commande(s)")
        
        if ps_commands:
            batch_ps = '; '.join(ps_commands) + '; Read-Host "Appuyez sur Entrée pour fermer"'
            subprocess.Popen(f'start powershell -NoExit -Command "{batch_ps}"', shell=True)
            log_text.insert(tk.END, f"✅ Fenêtre PowerShell ouverte avec {len(ps_commands)} commande(s)\n\n")
            self.ecrire_log(f"Fenêtre PowerShell ouverte avec {len(ps_commands)} commande(s)")
        
        progress.configure(value=total)
        current_label.configure(text="Installation terminée")
        close_btn.configure(state="normal")
        self.ecrire_log(f"Installation terminée - {total} application(s) traitée(s)")
        log_text.see(tk.END)

    def construire_commande(self, app):
        cmd, args = app["command"], app.get("arguments", "")
        
        if app["type"] == "CMD":
            return f'{cmd} {args}'
        elif app["type"] == "POWERSHELL":
            return f'{cmd} {args}'
        else:
            commands = {"WINGET": f'winget install "{cmd}" {args}', "EXE": f'"{cmd}" {args}', "MSI": f'msiexec /i "{cmd}" {args}'}
            return commands.get(app["type"], f'{cmd} {args}')

    def nouvelle_config(self):
        if messagebox.askyesno("Nouveau", "Créer une nouvelle configuration ?"):
            self.apps = []
            self.actualiser_affichage()

    def ouvrir_config(self):
        file_path = filedialog.askopenfilename(filetypes=[("JSON", "*.json")], initialdir=os.path.dirname(self.config_file))
        if file_path:
            try:
                with open(file_path, 'r', encoding='utf-8') as f: 
                    self.apps = json.load(f)
                self.config_file = file_path
                self.ecrire_log(f"Configuration ouverte: {os.path.basename(file_path)} ({len(self.apps)} applications)")
                self.actualiser_affichage()
            except Exception as e: 
                messagebox.showerror("Erreur", f"Impossible d'ouvrir: {e}")
                self.ecrire_log(f"Erreur lors de l'ouverture de {file_path}: {str(e)}", "ERROR")

    def sauver_config(self):
        file_path = filedialog.asksaveasfilename(title="Sauvegarder la configuration", defaultextension=".json", filetypes=[("JSON", "*.json"), ("Tous", "*.*")], initialdir=os.path.dirname(self.config_file))
        if file_path:
            try:
                with open(file_path, 'w', encoding='utf-8') as f: 
                    json.dump(self.apps, f, indent=2, ensure_ascii=False)
                self.config_file = file_path
                self.ecrire_log(f"Configuration sauvegardée: {os.path.basename(file_path)} ({len(self.apps)} applications)")
                messagebox.showinfo("Succès", f"Configuration sauvegardée: {os.path.basename(file_path)}")
            except Exception as e: 
                messagebox.showerror("Erreur", f"Impossible de sauvegarder: {e}")
                self.ecrire_log(f"Erreur lors de la sauvegarde: {str(e)}", "ERROR")

    def sauver_config_auto(self):
        try:
            with open(self.config_file, 'w', encoding='utf-8') as f: 
                json.dump(self.apps, f, indent=2, ensure_ascii=False)
        except Exception: 
            pass

    def charger_config(self):
        self.ecrire_log("Chargement de la configuration")
        try:
            if os.path.exists(self.config_file):
                with open(self.config_file, 'r', encoding='utf-8') as f: 
                    self.apps = json.load(f)
                self.ecrire_log(f"Configuration chargée: {len(self.apps)} application(s)")
            else:
                self.apps = [
                    {"name": "Visual Studio Code", "type": "WINGET", "command": "Microsoft.VisualStudioCode", "arguments": "", "selected": False}, 
                    {"name": "Google Chrome", "type": "WINGET", "command": "Google.Chrome", "arguments": "", "selected": False}, 
                    {"name": "7-Zip", "type": "WINGET", "command": "7zip.7zip", "arguments": "", "selected": False}
                ]
                self.sauver_config_auto()
                self.ecrire_log("Configuration par défaut créée")
        except Exception as e: 
            self.apps = []
            self.ecrire_log(f"Erreur lors du chargement de la configuration: {str(e)}", "ERROR")
        self.actualiser_affichage()

    def monter(self):
        selected_indices = [i for i, app in enumerate(self.apps) if app.get("selected", False)]
        if not selected_indices:
            return messagebox.showwarning("Sélection", "Veuillez sélectionner un logiciel à déplacer vers le haut")
        if 0 in selected_indices:
            return messagebox.showinfo("Info", "Le premier élément ne peut pas être monté")
        
        for i in selected_indices:
            if i > 0: 
                self.apps[i], self.apps[i-1] = self.apps[i-1], self.apps[i]
        self.sauver_config_auto()
        self.actualiser_affichage()

    def descendre(self):
        selected_indices = [i for i, app in enumerate(self.apps) if app.get("selected", False)]
        if not selected_indices:
            return messagebox.showwarning("Sélection", "Veuillez sélectionner un logiciel à déplacer vers le bas")
        if len(self.apps) - 1 in selected_indices:
            return messagebox.showinfo("Info", "Le dernier élément ne peut pas être descendu")
        
        for i in reversed(selected_indices):
            if i < len(self.apps) - 1: 
                self.apps[i], self.apps[i+1] = self.apps[i+1], self.apps[i]
        self.sauver_config_auto()
        self.actualiser_affichage()

    def est_admin(self):
        try:
            import ctypes
            return ctypes.windll.shell32.IsUserAnAdmin()
        except: 
            return False

    def ajuster_taille_fenetre(self):
        if len(self.apps) > 6:
            nouvelle_hauteur = min(600, 360 + (len(self.apps) - 6) * 30)
            self.root.geometry(f"580x{nouvelle_hauteur}")

    def ecrire_log(self, message, niveau="INFO"):
        try:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            log_filename = f"gestionnaire_{datetime.now().strftime('%Y%m%d')}.log"
            log_path = os.path.join(self.logs_dir, log_filename)
            
            with open(log_path, 'a', encoding='utf-8') as f:
                f.write(f"[{timestamp}] [{niveau}] {message}\n")
        except Exception:
            pass

    def demarrer(self): 
        self.ecrire_log("Application démarrée")
        self.root.mainloop()

if __name__ == "__main__":
    app = GestionnaireApps()
    app.demarrer()
