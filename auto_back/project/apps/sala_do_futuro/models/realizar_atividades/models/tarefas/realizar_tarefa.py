from project.apps.sala_do_futuro.models.realizar_atividades.models import CollectInfo
# from project import types
class RealizarTarefa:
    def __init__(self, page):
        self.page = page
        self.collect_info = CollectInfo(page=self.page)

    def run(self, user, id_usuario):
        self.collect_info.run(user=user, id_usuario=id_usuario)

        input(f'\n\nPrecione\n\n')