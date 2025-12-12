import subprocess
import sys
import os
import webbrowser
import time

ROOT_DIR = os.getcwd()

# ---------- Install dependencies ----------
requirements_path = os.path.join(ROOT_DIR, "requirements.txt")
print("🔹 Installing dependencies...")
subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", requirements_path])

print("🔹 Starting Wordle Solver project...")

# ---------- Start FastAPI (Api_wordle/main.py) ----------
fastapi_cmd = [
    sys.executable,
    "-m",
    "uvicorn",
    "Api_wordle.main:app",
    "--host", "127.0.0.1",
    "--port", "5000",
    "--reload"
]

fastapi_proc = subprocess.Popen(
    fastapi_cmd,
    cwd=ROOT_DIR
)

# ---------- Wait for server ----------
time.sleep(3)

# ---------- Open frontend ----------
frontend_path = os.path.join(ROOT_DIR, "frontend", "index.html")
webbrowser.open(f"file:///{frontend_path}")

print("\n✅ Project running!")
print("🌐 Frontend: file:///" + frontend_path)
print("🚀 API: http://127.0.0.1:5000")
print("🛑 Press CTRL+C to stop\n")

# ---------- Keep alive ----------
try:
    fastapi_proc.wait()
except KeyboardInterrupt:
    print("\n❌ Shutting down...")
    fastapi_proc.terminate()
