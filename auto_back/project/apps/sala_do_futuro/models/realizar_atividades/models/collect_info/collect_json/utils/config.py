from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[4]

DATA_DIR = BASE_DIR / 'data'
JSON_PATH = DATA_DIR / 'data.json'

DATA_DIR.mkdir(parents=True, exist_ok=True)
