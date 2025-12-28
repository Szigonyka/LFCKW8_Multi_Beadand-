import sys
import subprocess
import time
import os

def main():
    print("Rendszer indítása")

    python_cmd = sys.executable 
    
    print(f"(BACKEND) Inditas ezzel a paranccsal: {python_cmd} -m uvicorn")
    backend_process = subprocess.Popen(
        [python_cmd, "-m", "uvicorn", "backend.main:app", "--reload"]
    )

    time.sleep(3)

    print("(FRONTEND) Streamlit inditasa")
    frontend_process = subprocess.Popen(
        [python_cmd, "-m", "streamlit", "run", "frontend/app.py"]
    )

    print("\n Mindket szolgaltatas fut.")

    try:
       
        while True:
            time.sleep(1)
           
            if backend_process.poll() is not None or frontend_process.poll() is not None:
                print("[Valamelyik folyamat varatlanul leallt.")
                break
    except KeyboardInterrupt:
        print("\n Leállítás...")
    finally:
       
        backend_process.terminate()
        frontend_process.terminate()
        print("Program zárva")

if __name__ == "Start":
    main()