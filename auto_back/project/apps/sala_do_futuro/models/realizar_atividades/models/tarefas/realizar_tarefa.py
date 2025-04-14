from project import Display
from .collect_info import CollectInfo

class RealizarTarefa:
    def __init__(self):
        self.display = Display
        self.collectInfo = CollectInfo

    def run(self):
                
        self.collectInfo.run_collect(self)

        input(f'\n\nPrecione\n\n')