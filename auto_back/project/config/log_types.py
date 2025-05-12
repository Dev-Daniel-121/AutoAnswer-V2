from enum import Enum

class LogType(str, Enum):
    QUESTION = 'Question'
    TASK = 'Task'
    OPTION = 'Option'
    ANSWER = 'Answer'
    ERROR = 'Error'
    USER = 'User'
    MSG = 'Msg'
    SUCCESS = 'Success'
    WARNING = 'Warning'
    INFO = 'Info'
    DEBUG = 'Debug'
    INSTALL = 'Install'
    DELETED = 'Deleted'
    CHANGED = 'Changed'

    def __str__(self):
        return self.value
