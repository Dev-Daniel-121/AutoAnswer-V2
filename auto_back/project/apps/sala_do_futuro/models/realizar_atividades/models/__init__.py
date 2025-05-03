from .collect_info import CollectJson, CollectProvas, CollectRedacoes, CollectTarefas, CollectTaskInfos, General, QuestionInfo, Questions, AnswerCheckbox, GetCheckbox, Checkbox, AnswerRadios, GetRadios, Radios, Questionarie, TaskInfo, CollectTaskInfo, Time, CollectInfo
from .do_provas import DoProvas
from .do_redacao import DoRedacao
from .do_tarefas import DoTarefas
from .provas import RealizarProva
from .redacoes import RealizarRedacao
from .tarefas import RealizarTarefa

__all__ = [
    'CollectJson', 'CollectProvas', 'CollectRedacoes', 'CollectTarefas', 'CollectTaskInfos', 'General', 'QuestionInfo', 'Questions', 'AnswerCheckbox', 'GetCheckbox', 'Checkbox', 'AnswerRadios', 'GetRadios', 'Radios', 'Questionarie', 'TaskInfo', 'CollectTaskInfo', 'Time', 'CollectInfo',
    'DoProvas',
    'DoRedacao',
    'DoTarefas',
    'RealizarProva',
    'RealizarRedacao',
    'RealizarTarefa'
]