import os

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
ANSWER_DATA_JSON = os.path.join(BASE_DIR, "data", "answer_data.json")

os.makedirs(os.path.dirname(ANSWER_DATA_JSON), exist_ok=True)
