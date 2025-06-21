| Status             | Sugestão de definição aprimorada                                           |
| :----------------- | :------------------------------------------------------------------------- |
| Mais Usado         | Prompt com maior número de execuções comparado aos demais.                 |
| Pouco Usado        | Utilizado apenas 1 ou 2 vezes.                                             |
| Nunca Usado        | usage_history está vazio, nunca foi executado.                             |
| Uso Recente        | Última execução (used_at) ocorreu nos últimos X dias (ex: 15 ou 30 dias).  |
| Novo               | Criado recentemente (created_at recente) e sem histórico de uso.           |
| Atualizado         | (Opcional) Atualizado recentemente (campo updated_at presente e recente).  |
| Alta Precisão      | Taxa de acerto (correct / total_answers) igual ou superior a 80%.          |
| Baixa Precisão     | Taxa de acerto inferior a 50%.                                             |
| Revisar            | Baixa precisão (<50%) combinada com alto volume de uso, necessita análise. |
| Estável            | Precisão entre 50% e 80% com uso regular e consistente.                    |
| Em Destaque        | Alta precisão (≥80%) e alta frequência de uso, prompt referência.          |
| Desempenho Crítico | Alto número de erros em componentes sensíveis, requer atenção imediata.    |

<br>

### Exemplos de status no formato desejado

---

**\[1]. Title Prompt 1**                   A: 50 C: 45 W: 5
Prompt for IA

TENDÊNCIA:                     Mate: 60%  Hist: 40%
**Mais Usado** - 50x nesse mês          Rank: 1º de 30
**Alta Precisão** - 90% acertos

---

**\[2]. Title Prompt 2**                   A: 2 C: 2 W: 0
Prompt for IA

TENDÊNCIA:                     Geo: 100%
**Pouco Usado** - 2x nesse mês           Rank: 25º de 30
**Alta Precisão** - 100% acertos

---

**\[3]. Title Prompt 3**                   A: 0 C: 0 W: 0
Prompt for IA

TENDÊNCIA:                     -
**Nunca Usado** - 0x nesse mês            Rank: 30º de 30

---

**\[4]. Title Prompt 4**                   A: 10 C: 6 W: 4
Prompt for IA

TENDÊNCIA:                     Mate: 100%
**Uso Recente** - último uso há 5 dias
**Estável** - 60% acertos

---

**\[5]. Title Prompt 5**                   A: 0 C: 0 W: 0
Prompt for IA

TENDÊNCIA:                     -
**Novo** - criado há 10 dias
**Nunca Usado**

---

**\[6]. Title Prompt 6**                   A: 27 C: 19 W: 8
Prompt for IA

TENDÊNCIA:                     Mate: 66%  Hist: 33%
**Atualizado** - atualizado há 2 dias

---

**\[7]. Title Prompt 7**                   A: 24 C: 20 W: 4
Prompt for IA

TENDÊNCIA:                     Hist: 100%
**Alta Precisão** - 83% acertos

---

**\[8]. Title Prompt 8**                   A: 25 C: 10 W: 15
Prompt for IA

TENDÊNCIA:                     Geo: 100%
**Baixa Precisão** - 40% acertos

---

**\[9]. Title Prompt 9**                   A: 50 C: 20 W: 30
Prompt for IA

TENDÊNCIA:                     Hist: 80%  Mate: 20%
**Revisar** - alta frequência com baixa precisão (40% acertos)

---

**\[10]. Title Prompt 10**                   A: 40 C: 28 W: 12
Prompt for IA

TENDÊNCIA:                     Mate: 100%
**Estável** - 70% acertos

---

**\[11]. Title Prompt 11**                   A: 100 C: 85 W: 15
Prompt for IA

TENDÊNCIA:                     Mate: 50%  Hist: 50%
**Em Destaque** - alta frequência e alta precisão (85% acertos)

---

**\[12]. Title Prompt 12**                   A: 20 C: 10 W: 10
Prompt for IA

TENDÊNCIA:                     Hist: 100%
**Desempenho Crítico** - 50% erros em componente sensível (História)

---

Se quiser, posso ajudar a gerar esses relatórios automaticamente para seus dados reais! Quer?
