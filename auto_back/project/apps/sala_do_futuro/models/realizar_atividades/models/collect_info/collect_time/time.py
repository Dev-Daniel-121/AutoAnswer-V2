from datetime import datetime, timedelta
from project import LogType

class Time:
    def __init__(self):
        self.tempo_final = None

    def timer(self, seconds):
        now = datetime.now()
        self.tempo_final = now + timedelta(seconds=seconds)

        print(f'[{LogType.INFO}] Duração: {seconds}s')
        print(f'[{LogType.INFO}] Tempo ini: {now.strftime('%H:%M:%S')}')
        print(f'[{LogType.INFO}] Tempo fim: {self.tempo_final.strftime('%H:%M:%S')}\n')

    def tempo_restante(self):
        if self.tempo_final is None:
            print('Você ainda não iniciou o timer.')
            return

        now = datetime.now()
        restante = self.tempo_final - now

        if restante.total_seconds() <= 0:
            print('O tempo já terminou!')
        else:
            minutos, segundos = divmod(int(restante.total_seconds()), 60)
            print(f'[{LogType.INFO}] Tempo restante: {minutos} min {segundos} s\n')
