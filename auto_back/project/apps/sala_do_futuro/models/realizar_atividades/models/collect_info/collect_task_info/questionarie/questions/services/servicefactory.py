from .checkbox_service import CheckboxService
from .radios_service import RadiosService

class ServiceFactory:
    _services = {
        'Radios': RadiosService,
        'Checkbox': CheckboxService,
    }

    ''''''
    @classmethod
    def get_service(cls, question_type: str):
        service_class = cls._services.get(question_type)
        if not service_class:
            raise ValueError(f'Serviço não implementado para o tipo: {question_type}')
        return service_class()
