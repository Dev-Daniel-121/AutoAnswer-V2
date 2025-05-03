from .collect_json import CollectJson
from .collect_provas import CollectProvas
from .collect_redacoes import CollectRedacoes
from .collect_tarefas import CollectTarefas, CollectTaskInfos
from .collect_task_info import General, QuestionInfo, Questions, AnswerCheckbox, GetCheckbox, Checkbox, AnswerRadios, GetRadios, Radios, Questionarie, TaskInfo, CollectTaskInfo
from .collect_time import Time
from .collect_info import CollectInfo

__all__ = [
    'CollectJson',
    'CollectProvas',
    'CollectRedacoes',
    'CollectTarefas', 'CollectTaskInfos',
    'General', 'QuestionInfo', 'Questions', 'AnswerCheckbox', 'GetCheckbox', 'Checkbox', 'AnswerRadios', 'GetRadios', 'Radios', 'Questionarie', 'TaskInfo', 'CollectTaskInfo',
    'Time',
    'CollectInfo'
]