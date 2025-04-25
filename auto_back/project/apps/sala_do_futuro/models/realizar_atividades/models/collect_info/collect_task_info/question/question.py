class Question:
    def __init__(self, page):
        self.page = page

    def get_activity_score(self):
        activity_score_class = 'p.css-1wgaj9w'
        activity_score = self.page.locator(f'{activity_score_class}').text_content()
        return activity_score

    def run(self):
        pass

"""
{
   task_info: {
      status_atividade: "",
      id_da_atividade_do_site: "",
      id_da_atividade_gerado_automaticamente: "",
      tipo_atividade: "",
      matéria: "",
      titulo_atividade: "",
      usuario: "",
      autor: "",
      turma: "",
      data_expiracao: "",
      tempo_gasto: "",
      rascunho: "",
      enviado: "",
      tipos_de_questões: {
         card-img":"",
         card-gif": "",
         card-video": "",
         Text": "",
         Radios": "",
         Checkbox": "",
         Dragable": "",
         Order": "",
         Textarea": "",
         Select": "",
      }
   }
   questionnaire: {
      general: {
         pontuação_da_atividade: "",
         pontuação_adiquirida: "",
         num_de_textos: "",
         num_de_questoes: "",
         num_de_secoes: "",
         secoes: {
            0: "",
            1: "",
         },
         num_de_chutes: "",
         num_de_user_resposta: "",
         feedback_usuario: "",
         dificuldade: "",
         historico_tentativas: {
            0: { quest: "", "autor": "", "resultado": "", "tempo": "" },
            1: { quest: "", "autor": "", "resultado": "", "tempo": "" }
         },
         ia: {
             ia1: {
                desempenho_geral: "",
                questoes: ['', '', '']
                sugestoes: {
                   0: "",
                   1: ""
                }
             },
             ia2: {
                desempenho_geral: "",
                questoes: ['', '', '']
                sugestoes: {
                   0: "",
                   1: ""
                }
             }
         },
         num_de_erros: "",
         tipos_de_erros: ["", "", ""],
         logs_de_erros: {
            0: {
               tipo: "",
               detalhes: "",
               questao: "",
               timestamp: ""
            }
         }
      },
      questions: {
         0: {
            quest_info {
               pontuação_da_questao: "",
               pontuação_adiquirida: "",
               secao: "",
               num_de_chutes: "",
               num_de_user_resposta: "",
               feedback_usuario: "",
               dificuldade: "",
               historico_tentativas: {
                  0: { quest: "", "autor": "", "resultado": "", "tempo": "" },
                  1: { quest: "", "autor": "", "resultado": "", "tempo": "" }
               },
               num_de_erro: "",
               tipos_de_erro: ["", "", ""],
               logs_de_erro: {
                  0: {
                     tipo: "",
                     detalhes: "",
                     questao: "",
                     timestamp: ""
                  }
               },
               ia: "",
               tempo_gasto: "",
            },
            quest: {
               tipo: "",
               enunciado: "",
               alternativas: ['', '', '', '', ''],
               "resposta": ""
            }
         },
      },
   }
}
"""