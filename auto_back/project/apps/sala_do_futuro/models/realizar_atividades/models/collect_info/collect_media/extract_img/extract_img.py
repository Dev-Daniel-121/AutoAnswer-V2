from urllib.parse import urlparse
from project import types
import os, requests

class ExtractImg:
    def __init__(self, download_path):
        self.download_path = download_path

    def download_image(self, url, idx=None):
        try:
            os.makedirs(self.download_path, exist_ok=True)

            filename = os.path.basename(urlparse(url).path)
            if not filename:
                filename = f'image_{idx or 'unknown'}.jpg'

            filepath = os.path.join(self.download_path, filename)

            response = requests.get(url, stream=True, timeout=10)
            response.raise_for_status()

            with open(filepath, 'wb') as f:
                for chunk in response.iter_content(1024):
                    f.write(chunk)

            return filepath
        except Exception as e:
            print(f'[{types[4]}] Falha ao baixar imagem ({url}): {e}\n\n')
            return None
