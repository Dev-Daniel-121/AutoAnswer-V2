from project.apps.sala_do_futuro.models.realizar_atividades.models.collect_info.collect_media import TranscriptYoutube, ExtractImg
from project.apps.sala_do_futuro.models.realizar_atividades.models.collect_info.collect_task_info import TaskInfo
from project import types
import os

class CollectMedia:
    def __init__(self, page, card, video_media_selector, img_media_selector):
        if hasattr(card, 'element_handle'): card = card.element_handle()
        self.page = page
        self.card = card
        self.content = {
            'video': {},
            'image': {},
            'gif': {}
        }
        self.video_media_selector = video_media_selector
        self.img_media_selector = img_media_selector
        self.transcriber = TranscriptYoutube()
        self.task_info = TaskInfo(
            page=self.page, activity_status='',
            activity_type_class=':nth-match(li.MuiBreadcrumbs-li, 2)',
            material_activity_class='h6.css-yq44kw',
            activity_title_class='p.css-zscg42'
        )

        user, author, class_school, expires_in, site_activity_id = self.task_info.get_activity_infos()

        base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
        img_path = os.path.join(base_dir, 'data', 'img', str(site_activity_id))

        self.image_downloader = ExtractImg(img_path)

    def extract_media(self):
        self._extract_videos()
        self._extract_images()
        return self.content

    def _extract_videos(self):
        try:
            video_elements = self.card.query_selector_all(self.video_media_selector)
            for idx, iframe in enumerate(video_elements):
                try:
                    src = iframe.get_attribute('src')
                    if not src:
                        continue

                    transcription = None
                    if 'youtube.com' in src or 'youtu.be' in src:
                        try:
                            transcription = self.transcriber.get_transcript(src)
                        except Exception as e:
                            print(f'[{types[4]}] Erro na transcrição do vídeo ({src}): {e}')

                    self.content['video'][str(idx)] = {
                        'type': 'video',
                        'src': src,
                        'transcription': transcription
                    }
                except Exception as e:
                    print(f'[{types[4]}] Erro ao processar iframe do vídeo: {e}')
        except Exception as e:
            print(f'[{types[4]}] Erro ao coletar vídeos: {e}')

    def _extract_images(self):
        try:
            img_elements = self.card.query_selector_all(self.img_media_selector)
            if not img_elements:
                return

            has_valid_image = False
            for idx, img in enumerate(img_elements):
                try:
                    src = img.get_attribute('src')
                    if not src:
                        continue

                    if src.endswith('.gif'):
                        self.content['gif'][str(idx)] = {'type': 'gif', 'src': src}
                    else:
                        if not has_valid_image:
                            os.makedirs(self.image_downloader.download_path, exist_ok=True)
                            has_valid_image = True

                        local_path = self.image_downloader.download_image(src, idx)
                        self.content['image'][str(idx)] = {
                            'type': 'image',
                            'src': src,
                            'local_path': local_path
                        }
                except Exception as e:
                    print(f'[{types[4]}] Erro ao processar imagem: {e}')
        except Exception as e:
            print(f'[{types[4]}] Erro ao coletar imagens: {e}')
