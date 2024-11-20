from cx_Freeze import setup, Executable

# Remplacez 'votre_script.py' par le nom de votre script principal
script = "script.py"  # Assurez-vous de mettre le bon nom ici

# Définir les options pour la construction
build_options = {
    "packages": ["pandas"],
    "include_files": []  # Ajoutez ici d'autres fichiers nécessaires si nécessaire
}

# Configuration de l'application
setup(
    name="ExcelToJsonViewer",
    version="0.1",
    description="Une application pour afficher le contenu JSON d'un fichier Excel",
    options={"build_exe": build_options},
    executables=[Executable(script, base="Win32GUI")]  # Utilisez base="Win32GUI" pour une interface graphique sans console
)