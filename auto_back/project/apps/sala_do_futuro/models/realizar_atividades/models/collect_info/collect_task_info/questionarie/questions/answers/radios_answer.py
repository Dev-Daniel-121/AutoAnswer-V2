class RadiosAnswer:
    def __init__(self):
        pass
    
    def execute(self, question_data):
        # Aqui você usaria PyAutoGUI, simulação ou IA
        print(f"[RadiosAnswer] Respondendo: {question_data['statement']}")
        # Atualiza a resposta, se for o caso:
        question_data["answer"] = "A)"  # Simulado
