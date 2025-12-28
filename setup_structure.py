import os

# A projekt szerkezete
folders = [
    "backend",
    "backend/services",
    "frontend",
    "tests"
]

files = [
    "backend/__init__.py",
    "backend/main.py",      # Itt indul a szerver
    "backend/database.py",  # Adatbázis kapcsolat
    "backend/models.py",    # Adatbázis táblák
    "backend/schemas.py",   # Adatellenőrzés
    "backend/crud.py",      # Adatbázis műveletek
    "backend/services/__init__.py",
    "backend/services/scraper.py", # Háttérfolyamat
    "frontend/__init__.py",
    "frontend/app.py",      # Streamlit kód
    "tests/__init__.py",
    "tests/test_main.py",   # Tesztek
    ".env",                 # Jelszavaknak
    ".gitignore",           # GitHub-hoz
    "README.md",            # Leírás
    "requirements.txt",     # Csomaglista
]

# Mappák létrehozása
print(" Mappák létrehozása...")
for folder in folders:
    os.makedirs(folder, exist_ok=True)
    print(f"   - {folder} kész.")

# Fájlok létrehozása
print("\nFájlok létrehozása...")
for file in files:
    # Ha a fájl nem létezik, létrehozzuk
    if not os.path.exists(file):
        with open(file, 'w') as f:
            pass 
    print(f"   - {file} kész.")

# .gitignore tartalmának beírása
gitignore_content = """
venv/
__pycache__/
*.pyc
.env
.DS_Store
"""
with open(".gitignore", "w") as f:
    f.write(gitignore_content.strip())
