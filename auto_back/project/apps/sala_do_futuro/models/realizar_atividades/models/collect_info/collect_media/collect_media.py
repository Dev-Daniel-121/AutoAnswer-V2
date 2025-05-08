from project.apps.sala_do_futuro.models.realizar_atividades.models.collect_info.collect_media import TranscriptYoutube
from project import types

class CollectMedia:
    def __init__(self, card, video_media_selector, img_media_selector):
        if hasattr(card, 'element_handle'): card = card.element_handle()
        self.card = card
        self.content = {
            'video': {},
            'image': {},
            'gif': {}
        }
        self.video_media_selector = video_media_selector
        self.img_media_selector = img_media_selector
        self.transcriber = TranscriptYoutube()

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


{
    0: {
        "quest_info": {
            "required": True,
            "time": {"day": "", "start_time": "", "end_time": ""},
            "activity_score": "",
            "score": "",
            "section": "",
            "number_of_guesses": "",
            "number_of_user_responses": "",
            "user_feedback": "",
            "difficulty": "",
            "media": {"video": {}, "image": {}, "gif": {}},
            "history_of_attempts": {},
            "error_num": "",
            "error_types": ["", "", ""],
            "error_logs": {
                "0": {"type": "", "details": "", "question": "", "timestamp": ""}
            },
            "ia": "",
            "time_spent": "",
        },
        "quest": {
            "type": "Unknown Type",
            "statement": "Calcule quanto as cooperativas pagam por 2 kg de latinhas, 8 kg de revistas e 5 kg de sacolas brancas e preencha a lacuna a seguir.",
            "alternatives": {"media": {}, "alternative": [""]},
            "answer": "",
        },
    },
    1: {
        "quest_info": {
            "required": True,
            "time": {"day": "", "start_time": "", "end_time": ""},
            "activity_score": "",
            "score": "",
            "section": "",
            "number_of_guesses": "",
            "number_of_user_responses": "",
            "user_feedback": "",
            "difficulty": "",
            "media": {"video": {}, "image": {}, "gif": {}},
            "history_of_attempts": {},
            "error_num": "",
            "error_types": ["", "", ""],
            "error_logs": {
                "0": {"type": "", "details": "", "question": "", "timestamp": ""}
            },
            "ia": "",
            "time_spent": "",
        },
        "quest": {
            "type": "Unknown Type",
            "statement": "Considerando \ufeffxxx\ufeff o peso das latinhas, \ufeffyyy\ufeff o peso das revistas e \ufeffzzz\ufeff o peso das sacolas brancas, julgue as afirmativas a seguir e classifique-as como certas ou erradas.",
            "alternatives": {"media": {}, "alternative": [""]},
            "answer": "",
        },
    },
    2: {
        "quest_info": {
            "required": True,
            "time": {"day": "", "start_time": "", "end_time": ""},
            "activity_score": "",
            "score": "",
            "section": "",
            "number_of_guesses": "",
            "number_of_user_responses": "",
            "user_feedback": "",
            "difficulty": "",
            "media": {"video": {}, "image": {}, "gif": {}},
            "history_of_attempts": {},
            "error_num": "",
            "error_types": ["", "", ""],
            "error_logs": {
                "0": {"type": "", "details": "", "question": "", "timestamp": ""}
            },
            "ia": "",
            "time_spent": "",
        },
        "quest": {
            "type": "Radios",
            "statement": "Com base nas três equações lineares da questão anterior, reescreva o sistema na forma escalonada e selecione a alternativa correta.",
            "alternatives": {
                "media": {},
                "alternative": [
                    {
                        "text": "A)",
                        "media": {
                            "video": {},
                            "image": {
                                "0": {
                                    "type": "image",
                                    "src": "https://edusp-static.ip.tv/tms/edusp/tspmat8/xxS7cyVZHUzAB7f94A8hARVuEy5wrX.png",
                                }
                            },
                            "gif": {},
                        },
                    },
                    {
                        "text": "B)",
                        "media": {
                            "video": {},
                            "image": {
                                "0": {
                                    "type": "image",
                                    "src": "https://edusp-static.ip.tv/tms/edusp/tspmat8/VdhHQ4L7Rap8QOZED0w20wipJF0UoE.png",
                                }
                            },
                            "gif": {},
                        },
                    },
                    {
                        "text": "C)",
                        "media": {
                            "video": {},
                            "image": {
                                "0": {
                                    "type": "image",
                                    "src": "https://edusp-static.ip.tv/tms/edusp/tspmat8/GG5oGn3C0XGCCwuADBRIYqYPE0vvz8.png",
                                }
                            },
                            "gif": {},
                        },
                    },
                    {
                        "text": "D)",
                        "media": {
                            "video": {},
                            "image": {
                                "0": {
                                    "type": "image",
                                    "src": "https://edusp-static.ip.tv/tms/edusp/tspmat8/rhEiZDVuVE9hMx8EKcD3A2wUB4MWLA.png",
                                }
                            },
                            "gif": {},
                        },
                    },
                    {
                        "text": "E)",
                        "media": {
                            "video": {},
                            "image": {
                                "0": {
                                    "type": "image",
                                    "src": "https://edusp-static.ip.tv/tms/edusp/tspmat8/MX4Xx0yEMrfl22Xy7ijM4k0eBBy8ai.png",
                                }
                            },
                            "gif": {},
                        },
                    },
                ],
            },
            "answer": "",
        },
    },
    3: {
        "quest_info": {
            "required": True,
            "time": {"day": "", "start_time": "", "end_time": ""},
            "activity_score": "",
            "score": "",
            "section": "",
            "number_of_guesses": "",
            "number_of_user_responses": "",
            "user_feedback": "",
            "difficulty": "",
            "media": {"video": {}, "image": {}, "gif": {}},
            "history_of_attempts": {},
            "error_num": "",
            "error_types": ["", "", ""],
            "error_logs": {
                "0": {"type": "", "details": "", "question": "", "timestamp": ""}
            },
            "ia": "",
            "time_spent": "",
        },
        "quest": {
            "type": "Radios",
            "statement": "(UFPR, 2014 – Adaptado) No processo de preparação de uma mistura, foi necessário estudar o sistema linear: \ufeff{p+2q+r=32p+3r=8p+6q=1 \\begin{cases} p &+& 2q &+& r &=& 3 \\\\ 2p &+& 3r &=& 8 \\\\ p &+& 6q &=& 1 \\end{cases} ⎩⎨⎧\u200bp2pp\u200b+++\u200b2q3r6q\u200b+==\u200br81\u200b=3\ufeff Nesse sistema, \ufeffppp\ufeff, \ufeffqqq\ufeff e \ufeffrrr\ufeff representam as quantidades dos três elementos envolvidos na mistura.Qual a classificação desse sistema linear?",
            "alternatives": {
                "media": {},
                "alternative": [
                    {
                        "text": "A) Sistema Possível e Determinado.",
                        "media": {"video": {}, "image": {}, "gif": {}},
                    },
                    {
                        "text": "B) Sistema Possível e Indeterminado, para todo \ufeffppp\ufeff de 0 a \ufeff16\\frac{1}{6}61\u200b\ufeff.",
                        "media": {"video": {}, "image": {}, "gif": {}},
                    },
                    {
                        "text": "C) Sistema Possível e Indeterminado, para todo \ufeffqqq\ufeff de 0 a \ufeff16\\frac{1}{6}61\u200b\ufeff.",
                        "media": {"video": {}, "image": {}, "gif": {}},
                    },
                    {
                        "text": "D) Sistema Possível e Indeterminado, para todo \ufeffrrr\ufeff de 0 a \ufeff16\\frac{1}{6}61\u200b\ufeff.",
                        "media": {"video": {}, "image": {}, "gif": {}},
                    },
                    {
                        "text": "E) Sistema Impossível.",
                        "media": {"video": {}, "image": {}, "gif": {}},
                    },
                ],
            },
            "answer": "",
        },
    },
}
