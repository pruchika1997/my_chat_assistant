import os
from dotenv import load_dotenv

load_dotenv()

BACKEND = os.getenv("BACKEND", "ollama")
OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "phi3:mini")