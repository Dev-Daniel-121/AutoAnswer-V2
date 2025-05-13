from datetime import datetime, timedelta
import os, json

class SaveMetadata:
    def __init__(self, metadata_filename='metadata.json'):
        self.metadata_filename = metadata_filename

    def _get_data_path(self):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        data_dir = os.path.join(os.path.dirname(current_dir), 'data')
        os.makedirs(data_dir, exist_ok=True)
        return os.path.join(data_dir, self.metadata_filename)

    def load_metadata(self):
        path = self._get_data_path()
        if os.path.exists(path):
            try:
                with open(path, 'r') as f:
                    return json.load(f)
            except json.JSONDecodeError:
                from project.utils.logger import log
                from project import LogType
                log(LogType.ERROR, f'Erro ao carregar JSON de metadados: \'{path}\' está vazio ou inválido.')
                return {}
        return {}

    def save(self, activity_id, days_to_expire):
        metadata = self.load_metadata()
        now = datetime.now()
        expires = now + timedelta(days=days_to_expire)

        metadata[str(activity_id)] = {
            'start_date': now.isoformat(),
            'end_date': expires.isoformat()
        }

        with open(self._get_data_path(), 'w') as f:
            json.dump(metadata, f, indent=4)

        return metadata[str(activity_id)]
