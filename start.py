import os
import subprocess
import venv
import sys

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ENV_DIR = os.path.join(BASE_DIR, "worker_env")
WORKER_SCRIPT = os.path.join(BASE_DIR, "worker", "worker.py")
REQ_FILE = os.path.join(BASE_DIR, "requirements.txt")

if not os.path.exists(ENV_DIR):
    venv.create(ENV_DIR, with_pip=True)

PYTHON_PATH = os.path.join(ENV_DIR, "Scripts", "python.exe") if os.name == "nt" else os.path.join(ENV_DIR, "bin", "python")

if not os.path.exists(WORKER_SCRIPT):
    sys.exit(1)

if os.path.exists(REQ_FILE):
    subprocess.run([PYTHON_PATH, "-m", "pip", "install", "-r", REQ_FILE])

result = subprocess.run([PYTHON_PATH, WORKER_SCRIPT])
sys.exit(result.returncode)
