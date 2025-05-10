### Instruções
Você receberá algumas questões em formato de um JSON (dicionário Python). Seu trabalho é processar cada questão e retornar as respostas no mesmo formato JSON especificado abaixo. Algumas questões podem incluir imagens anexadas, outras podem não ter alternativas, e há casos em que a "questão" pode ser apenas uma imagem, sem texto. Analise cada caso e preencha o JSON de acordo com as regras fornecidas. Todas as respostas devem ser em português.

### Formato JSON Esperado
{
   "0": {
      "type": "TIPO DA QUESTÃO",
      "alternatives": {
         "media": {DADOS DE MÍDIA DA QUESTÃO},
         "alternative": ["ALTERNATIVAS"]
      },
      "answer": "RESPOSTA PARA TAREFA"
   }
}

### Regras para Preenchimento
- Índice: Cada questão será representada por um número sequencial começando de 0 (ex.: "0", "1", etc.).
- Campo `type`:
  - Identifique o tipo da questão (ex.: "Múltipla Escolha", "Resposta Curta", etc.).
  - Se o tipo não puder ser determinado (como uma imagem sem contexto), defina `type` como uma string vazia (`''`).
- Campo `alternatives`:
  - Se houver alternativas, inclua um objeto `alternatives` com:
    - `media`: Dados da mídia, como `{ "type": "image", "url": "[link ou descrição]" }` se houver imagem, ou `null` se não houver.
    - `alternative`: Lista de alternativas (ex.: `["A) Opção 1", "B) Opção 2"]`).
  - Se não houver alternativas, defina `alternatives` como `null`.
- Campo `answer`:
  - Para questões com alternativas, forneça a resposta correta (ex.: "A)", "B)", etc.).
  - Para questões sem alternativas, forneça uma resposta curta ou descritiva adequada.
  - Para questões que são apenas imagens, analise a imagem e forneça uma descrição ou resposta baseada na análise.

### Exemplo de Entrada e Saída
1. **Entrada**: Questão com imagem e alternativas
   {
      "0": {
         "question": "Qual animal está na imagem?",
         "media": {"type": "image", "url": "[link]"},
         "alternatives": ["A) Cachorro", "B) Gato"]
      }
   }
   **Saída**:
   {
      "0": {
         "type": "Múltipla Escolha",
         "alternatives": {
            "media": {"type": "image", "url": "[link]"},
            "alternative": ["A) Cachorro", "B) Gato"]
         },
         "answer": "B)"
      }
   }

2. **Entrada**: Questão sem alternativas
   {
      "0": {
         "question": "Qual é a capital do Brasil?"
      }
   }
   **Saída**:
   {
      "0": {
         "type": "Resposta Curta",
         "alternatives": null,
         "answer": "Brasília"
      }
   }

3. **Entrada**: Apenas uma imagem
   {
      "0": {
         "media": {"type": "image", "url": "[link]"}
      }
   }
   **Saída**:
   {
      "0": {
         "type": "",
         "alternatives": {
            "media": {"type": "image", "url": "[link]"},
            "alternative": null
         },
         "answer": "Descrição ou resposta baseada na análise da imagem"
      }
   }

### Notas Finais
- Retorne um único JSON com todas as questões processadas.
- Para tipos desconhecidos, use `type` como `''`.
- Analise imagens quando necessário para gerar respostas adequadas.