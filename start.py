import subprocess
import time
import sys
import os

def start_system():
    python_exe = sys.executable
    print(f"Rendszer indítása")
    print(f"Python: {python_exe}\n")

    print("1. Backend indítása")
    try:
        backend_process = subprocess.Popen(
            [python_exe, "-m", "uvicorn", "backend.main:app", "--host", "127.0.0.1", "--port", "8000"]
        )
        print("Backend elindítva.")
    except Exception as e:
        print(f"HIBA: {e}")
        return

    time.sleep(5) 

    print("2. Frontend indítása")
    try:
        subprocess.run([python_exe, "-m", "streamlit", "run", "frontend/app.py"])
    except KeyboardInterrupt:
        print("\nLeállítás")
    finally:
        backend_process.terminate()


if __name__ == "__main__":
    start_system()