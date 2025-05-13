from project.utils.logger import log
from urllib.parse import urlparse
from project import LogType
import os, time, requests

class ExtractImg:
    def __init__(self, download_path, days_to_expire, id_folder, time_remaining):
        self.download_path = download_path
        self.days_to_expire = days_to_expire
        self.id_folder = id_folder
        self.time_remaining = time_remaining

    def download_image(self, url, idx=None):
        try:
            os.makedirs(self.download_path, exist_ok=True)

            filename = os.path.basename(urlparse(url).path)
            if not filename:
                filename = f'image_{idx or 'unknown'}.jpg'

            filepath = os.path.join(self.download_path, filename)

            start_time = time.time()
            response = requests.get(url, stream=True, timeout=10)
            response.raise_for_status()

            with open(filepath, 'wb') as f:
                for chunk in response.iter_content(1024):
                    f.write(chunk)

            duration = time.time() - start_time

            log(LogType.INSTALL, f'Imagem salva em: {filepath} (tempo: {duration:.2f}s)')
            log(
                LogType.WARNING,
                f'Os arquivos de mídia serão armazenados por {self.days_to_expire} dias. '
                f'Verifique \'{self.id_folder}\' ({self.time_remaining} dias restantes)'
            )

            return filepath

        except Exception as e:
            log(
                LogType.ERROR,
                f'Erro ao salvar imagem em: {filepath if 'filepath' in locals() else url}: {e}'
            )
            return None
