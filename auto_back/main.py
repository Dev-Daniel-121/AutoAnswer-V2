from project.apps.sala_do_futuro.models.realizar_atividades.models.collect_info.collect_media import DeleteMedia
from project import MenuSystem
import os

def run():
	base_dir = os.path.dirname(os.path.abspath(__file__))
	img_path = os.path.join(
		base_dir,
		'project', 'apps', 'sala_do_futuro', 'models',
		'realizar_atividades', 'data', 'img'
	)

	delete_media = DeleteMedia(base_path=img_path, max_age_days=7)
	delete_media.update_folder_names()
    
	menu_system = MenuSystem()
	menu_system.run()

run()
