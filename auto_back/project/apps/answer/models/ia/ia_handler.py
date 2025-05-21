from .chatgpt import ChatGPT
from .grok import Grok

class IAHandler:
    def __init__(self):
        self.ia_classes = [ChatGPT, Grok]

    def get_ias(self):
        return [cls() for cls in self.ia_classes]
