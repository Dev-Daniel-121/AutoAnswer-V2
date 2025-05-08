from project.apps.sala_do_futuro.models.realizar_atividades.models.collect_info.collect_media.extract_transcript.transcript_youtube.transcript_youtube import TranscriptYoutube
from project import types

class CollectMedia:
    def __init__(self, card, video_media, img_media):
        if hasattr(card, 'element_handle'):
            card = card.element_handle()
        self.card = card
        self.content = {
            'video': {},
            'image': {},
            'gif': {}
        }
        self.video_media = video_media
        self.img_media = img_media
        self.transcriber = TranscriptYoutube()

    def extract_media(self):
        self._extract_videos()
        self._extract_images()
        return self.content

    def _extract_videos(self):
        try:
            video_elements = self.card.query_selector_all(self.video_media)
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
            img_elements = self.card.query_selector_all(self.img_media)
            for idx, img in enumerate(img_elements):
                try:
                    src = img.get_attribute('src')
                    if not src:
                        continue

                    if src.endswith('.gif'):
                        self.content['gif'][str(idx)] = {'type': 'gif', 'src': src}
                    else:
                        self.content['image'][str(idx)] = {'type': 'image', 'src': src}
                except Exception as e:
                    print(f'[{types[4]}] Erro ao processar imagem: {e}')
        except Exception as e:
            print(f'[{types[4]}] Erro ao coletar imagens: {e}')
