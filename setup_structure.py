import os


folders = [
    "backend",
    "backend/services",
    "frontend",
    "tests"
]

files = [
    "backend/__init__.py",
    "backend/main.py",      
    "backend/database.py",  
    "backend/models.py",    
    "backend/schemas.py",   
    "backend/crud.py",      
    "backend/services/__init__.py",
    "backend/services/scraper.py", 
    "frontend/__init__.py",
    "frontend/app.py",      
    "tests/test_main.py",   
    ".env",                 
    ".gitignore",           
    "README.md",            
    "requirements.txt",     
]


print(" Mappák létrehozása...")
for folder in folders:
    os.makedirs(folder, exist_ok=True)
    print(f"   - {folder} kész.")


print("\nFájlok létrehozása...")
for file in files:
    
    if not os.path.exists(file):
        with open(file, 'w') as f:
            pass 
    print(f"   - {file} kész.")


gitignore_content = """
venv/
__pycache__/
*.pyc
.env
.DS_Store
"""
with open(".gitignore", "w") as f:
    f.write(gitignore_content.strip())
