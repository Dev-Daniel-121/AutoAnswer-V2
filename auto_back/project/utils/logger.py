from datetime import datetime
from project import LogType
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
LOG_FILE_PATH = os.path.join(BASE_DIR, 'data', 'logs.log')
os.makedirs(os.path.dirname(LOG_FILE_PATH), exist_ok=True)

def log(log_type: LogType, message: str):
    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
    log_line = f"{now} [{log_type.value}] {message}"

    with open(LOG_FILE_PATH, 'a', encoding='utf-8') as f:
        f.write(log_line + '\n')
