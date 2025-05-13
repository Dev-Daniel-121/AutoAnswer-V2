from project.utils.logger import log
from datetime import datetime
import os, shutil, re, json
from project import LogType

class DeleteMedia:
    def __init__(self, base_path, max_age_days=7, metadata_filename='metadata.json'):
        self.base_path = base_path
        self.max_age_days = max_age_days
        self.metadata_filename = metadata_filename
        self.metadata_path = os.path.join(
            os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
            'data',
            self.metadata_filename
        )

    def load_metadata(self):
        if os.path.exists(self.metadata_path):
            try:
                with open(self.metadata_path, 'r') as f:
                    return json.load(f)
            except json.JSONDecodeError:
                log(LogType.ERROR, f'Erro ao carregar metadata.json: arquivo inválido.')
                return {}
        return {}

    def save_metadata(self, metadata):
        try:
            with open(self.metadata_path, 'w') as f:
                json.dump(metadata, f, indent=4)
        except Exception as e:
            log(LogType.ERROR, f'Erro ao salvar metadata.json: {e}')

    def remove_metadata_entry(self, activity_id):
        metadata = self.load_metadata()
        if str(activity_id) in metadata:
            del metadata[str(activity_id)]
            self.save_metadata(metadata)
            log(LogType.INFO, f'Removido metadata para atividade \'{activity_id}\'')

    def get_remaining_days_by_json(self, activity_id):
        metadata = self.load_metadata()
        info = metadata.get(str(activity_id))
        if not info:
            return self.max_age_days

        try:
            end_date = datetime.fromisoformat(info['end_date'])
            now = datetime.now()
            delta = (end_date - now).days
            return max(0, delta)
        except Exception as e:
            log(LogType.ERROR, f'Erro ao calcular tempo restante da atividade {activity_id}: {e}')
            return self.max_age_days

    def update_folder_names(self):
        for folder_name in os.listdir(self.base_path):
            match = re.match(r'^(\d+)\s+\((\d+)d\)$', folder_name)
            if not match:
                continue

            activity_id = match.group(1)
            folder_path = os.path.join(self.base_path, folder_name)

            if not os.path.isdir(folder_path):
                continue

            remaining_days = self.get_remaining_days_by_json(activity_id)

            if remaining_days == 0:
                try:
                    shutil.rmtree(folder_path)
                    log(LogType.DELETED, f'Deletado pasta \'{folder_name}\'')
                    self.remove_metadata_entry(activity_id)
                except Exception as e:
                    log(LogType.ERROR, f'Falha ao deletar pasta \'{folder_name}\': {e}')
            else:
                new_folder_name = f'{activity_id} ({remaining_days}d)'
                new_folder_path = os.path.join(self.base_path, new_folder_name)
                if folder_name != new_folder_name:
                    try:
                        os.rename(folder_path, new_folder_path)
                        log(LogType.CHANGED, f'Alterado Nome da pasta \'{folder_name}\' → \'{new_folder_name}\'')
                    except Exception as e:
                        log(LogType.ERROR, f'Falha ao renomear \'{folder_name}\': {e}')
