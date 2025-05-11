from datetime import datetime, timedelta
import os, time, shutil, re
from project import types

class DeleteMedia:
    def __init__(self, base_path, max_age_days):
        self.base_path = base_path
        self.max_age_days = max_age_days

    def get_remaining_days(self, folder_path):
        if not os.path.exists(folder_path):
            return None

        dir_mtime = os.path.getmtime(folder_path)
        expiration_date = datetime.fromtimestamp(dir_mtime) + timedelta(days=self.max_age_days)
        remaining = (expiration_date - datetime.now()).days
        return max(0, remaining)

    def delete_expired_media_folders(self, allowed_ids):
        for item in os.listdir(self.base_path):
            for activity_id in allowed_ids:
                if item.startswith(str(activity_id)):
                    folder_path = os.path.join(self.base_path, item)
                    if os.path.isdir(folder_path):
                        remaining_days = self.get_remaining_days(folder_path)
                        if remaining_days == 0:
                            try:
                                shutil.rmtree(folder_path)
                                print(f'[{types[9]}] Pasta expirada deletada: {folder_path}')
                            except Exception as e:
                                print(f'[{types[4]}] Falha ao deletar {folder_path}: {e}')
                        else:
                            print(f'[{types[9]}] Pasta ainda válida ({remaining_days} dias restantes): {folder_path}')

    def update_folder_names(self):
        '''
        Renomeia pastas com base no tempo restante real, considerando o valor original no nome.
        Exemplo: '12345 (7d)' → '12345 (6d)' se passou 1 dia.
        '''
        for folder_name in os.listdir(self.base_path):
            match = re.match(r'^(\d+)\s+\((\d+)d\)$', folder_name)
            if not match:
                continue  # ignora pastas com nomes fora do padrão

            activity_id = match.group(1)
            original_days = int(match.group(2))
            folder_path = os.path.join(self.base_path, folder_name)
            if not os.path.isdir(folder_path):
                continue

            # Usa mtime como base
            dir_mtime = os.path.getmtime(folder_path)
            days_passed = (datetime.now() - datetime.fromtimestamp(dir_mtime)).days
            remaining_days = max(0, original_days - days_passed)

            if remaining_days == 0:
                try:
                    shutil.rmtree(folder_path)
                    print(f'[{types[9]}] Pasta expirada deletada: {folder_path}')
                except Exception as e:
                    print(f'[{types[4]}] Falha ao deletar {folder_path}: {e}')
            else:
                new_folder_name = f'{activity_id} ({remaining_days}d)'
                new_folder_path = os.path.join(self.base_path, new_folder_name)
                if folder_name != new_folder_name:
                    try:
                        os.rename(folder_path, new_folder_path)
                        print(f'[{types[9]}] Pasta renomeada: \'{folder_name}\' → \'{new_folder_name}\'')
                    except Exception as e:
                        print(f'[{types[4]}] Falha ao renomear \'{folder_name}\': {e}')
