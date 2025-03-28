# Planejamento para Tarefas

### Estrutura geral do site

| Elmento | Class - Id - Data |                                                                Descrição |
| :------ | :---------------: | -----------------------------------------------------------------------: |
| div     |   .css-1jyoemj    | Header, container de infomações sobre a Atividade (id, professor, aluno) |
| div     |   .css-1mpla7o    |                                                        Texto, para apoio |
| div     |   .css-1oc0937    |                         Seção, container onde mostra a seção que estamos |
| div     |    .css-b200pa    |                                  Questão, container da questão (div pai) |

<br>

### Estrutura do Header

| Elmento | Class - Id - Data |                                                                Descrição |
| :------ | :---------------: | -----------------------------------------------------------------------: |
| div     |   .css-18qy6g8    |                                        Header (Título - Nome da matéria) |
| h6      |    .css-yq44kw    |                                                 Título (Nome da matéria) |
| div     |    .css-i8nh6i    |                                         Container (Conteúdo/Informações) |
| p       |    .css-zscg42    |                                                                Subtítulo |
| p       |   .css-10auemp    |                                                             Espaço vazio |
| p       |    .css-dyxuuh    |                                   Linha de conteúdo (Pergunta e Respota) |
| p       |   .css-18c049f    |                                                                 Pergunta |
| div     |   .MuiCollapse    |                     (hidden ou entered).css-c4sutr - Conteúdo colapsavel |
| div     |    .css-hboir5    |                                                    Container do conteúdo |
| p       |    .css-dyxuuh    | Linha de conteúdo (Pergunta e Respota - Mesmo esquema do div.css-i8nh6i) |
| p       |   .css-18c049f    |                                                                 Pergunta |

### Notação

~~~html
div.css-1jyoemj - Header
	div.css-18qy6g8 - Header (Título - Nome da matéria)
		h6.css-yq44kw - Título (Nome da matéria)
	div.css-i8nh6i - Container (Conteúdo/Informações)
		p.css-zscg42 - Subtítulo
		p.css-10auemp - Espaço vazio
		p.css-dyxuuh - Linha de conteúdo (Pergunta e Respota)
			p.css-18c049f - Pergunta
	div.MuiCollapse-(hidden ou entered).css-c4sutr - Conteúdo colapsavel
		div.css-hboir5 - Container do conteúdo
			p.css-dyxuuh - Linha de conteúdo (Pergunta e Respota - Mesmo esquema do div.css-i8nh6i)
				p.css-18c049f - Pergunta
~~~

<br>

### Estrutura do Texto de apoio

| Elmento | Class - Id - Data |               Descrição |
| :------ | :---------------: | ----------------------: |
| h6      |   .css-18a53hf    |               Container |
| div     |    .css-axw7ok    | Container para Conteúdo |
| div     |    .css-8atqhb    |      Contianer Conteúdo |
| p       |                   |                conteúdo |

### Notação

~~~html
div.css-1mpla7o - Texto
	h6.css-18a53hf - Container
		div.css-axw7ok - Container para Conteúdo
			div.css-8atqhb - Contianer Conteúdo
				p - conteúdo
~~~

<br>

### Estrutura da Seção

| Elmento |                 Class - Id - Data                 |                 Descrição |
| :------ | :-----------------------------------------------: | ------------------------: |
| div     |                   .css-1oc0937                    |                     Seção |
| div     |                    .css-cocwl3                    |        Container - Título |
| div     |                   .css-18pljz1                    |        Container conteúdo |
| p       |                    .css-6906ai                    |     Título (Seção número) |
| div     | .MuiCollapse-(hidden ou entered) <br> .css-c4sutr |       Conteúdo colapsavel |
| div     |                    .css-hboir5                    |     Container do conteúdo |
| div     |                    .css-iftemt                    |     container do conteúdo |
| div     |                    .css-8atqhb                    | container para o conteúdo |
| h2      |                                                   |  Título (Nome da Matéria) |

~~~html
div.css-1oc0937 - Seção
	div.css-cocwl3 - Container - Título
		div.css-18pljz1 - Container conteúdo
			p.css-6906ai - Título (Seção número)
	div.MuiCollapse-(hidden ou entered).css-c4sutr - Conteúdo colapsavel
		div.css-hboir5 - Container do conteúdo
			div.css-iftemt - container do conteúdo
				div.css-8atqhb - container para o conteúdo
					h2 - Título (Nome da Matéria)
~~~

<br>

### Estrutura da questão (div.css-b200pa)

| Elmento |                Class - Id - Data                 |                                                             Descrição |
| :------ | :----------------------------------------------: | --------------------------------------------------------------------: |
| div     |                   .css-rnebx4                    | Header da questão (Questão Atual, Total Questões, Importancia e Nota) |
| h6      |                   .css-wjosgp                    |                      Info de questão (Questão Atual e Total Questões) |
| p       |                   .css-m576f2                    |                                 <b>Questão Atual</b> e Total Questões |
| div     |                   .css-bxvhhl                    |                                         Importancia da questão e Nota |
| p       | .css-sz9ejl <br> data-testid="sinal-obrigatorio" |                                                  Sinal de obrigatório |
| p       |                   .css-1wgaj9w                   |                                                     Pontos da questão |
| div     |                   .css-rcuo3b                    |                                        Instruções da questão (Título) |
| div     |                   .css-1a4wlpz                   |                                 Conteúdo da questão (Texto do título) |
| p       |                                                  |                                                              Conteúdo |
| span    |          .ql-formula <br> data-value=""          |                               Formulas (data-value é a formula em si) |
| div     |    .(Tipo de alternativas) <br> .css-1h7anqn     |                                   Alternativas e Tipo de alternativas |
| div     |                   .css-9whsf3                    |                                                           Alternativa |
| div     |                   .css-10zfeld                   |                 Conteúdo da alteranativa (Btn e Valor da alternativa) |
| label   |                   .css-dpvp45                    |                                                Btn selecionar questão |
| input   |                   .css-1m9pwf3                   |                                               Input do Btn selecionar |
| div     |                   .css-1p78i1z                   |                                               Conteúdo da alternativa |
| p       |                                                  |                               Conteúdo da alternativa (Letra e texto) |
| span    |                      Letra                       |                                                                       |
| span    |          .ql-formula <br> data-value=""          |                               Formulas (data-value é a formula em si) |

### Notação

~~~html
div.css-b200pa - Questões
	div.css-rnebx4 - Header da questão (Questão Atual, Total Questões, Importancia e Nota)
		h6.css-wjosgp - Info de questão (Questão Atual e Total Questões)
			p.css-m576f2 - <b>Questão Atual</b> e Total Questões
		div.css-bxvhhl - Importancia e Nota
			p.css-sz9ejl data-testid="sinal-obrigatorio" - Sinal de obrigatório
			p.css-1wgaj9w - Pontos da questão
	div.css-rcuo3b - Instruções da questão (Título)
		div.css-1a4wlpz - Conteúdo da questão (Texto do título)
			p - Conteúdo
				span.ql-formula data-value="" - Formulas
	div.(Tipo de alternativas).css-1h7anqn - Alternativas e Tipo de alternativas
		div.css-9whsf3 - Alternativa
			div.css-10zfeld - Conteúdo da alteranativa (Btn e Valor da alternativa)
				label.css-dpvp45 - Btn selecionar questão
					input.css-1m9pwf3 - Input do Btn selecionar
				div.css-1p78i1z - Conteúdo da alternativa
					p - Texto
						span - Letra
						span.ql-formula data-value="" - Formula
~~~

<br><br>

<hr>

<br><br>

# Notação original

~~~html
div.css-1jyoemj - Header
	div.css-18qy6g8 - Header (Título - Nome da matéria)
		h6.css-yq44kw - Título (Nome da matéria)
	div.css-i8nh6i - Container (Conteúdo/Informações)
		p.css-zscg42 - Subtítulo
		p.css-10auemp - Espaço vazio
		p.css-dyxuuh - Linha de conteúdo (Pergunta e Respota)
			p.css-18c049f - Pergunta
	div.MuiCollapse-(hidden ou entered).css-c4sutr - Conteúdo colapsavel
		div.css-hboir5 - Container do conteúdo
			p.css-dyxuuh - Linha de conteúdo (Pergunta e Respota - Mesmo esquema do div.css-i8nh6i)
				p.css-18c049f - Pergunta
div.css-1mpla7o - Texto
	h6.css-18a53hf - Container
		div.css-axw7ok - Container para Conteúdo
			div.css-8atqhb - Contianer Conteúdo
				p - conteúdo
div.css-1oc0937 - Seção
	div.css-cocwl3 - Container - Título
		div.css-18pljz1 - Container conteúdo
			p.css-6906ai - Título (Seção número)
	div.MuiCollapse-(hidden ou entered).css-c4sutr - Conteúdo colapsavel
		div.css-hboir5 - Container do conteúdo
			div.css-iftemt - container do conteúdo
				div.css-8atqhb - container para o conteúdo
					h2 - Título (Nome da Matéria)
div.css-b200pa - Questões
	div.css-rnebx4 - Header da questão (Questão Atual, Total Questões, Importancia e Nota)
		h6.css-wjosgp - Info de questão (Questão Atual e Total Questões)
			p.css-m576f2 - <b>Questão Atual</b> e Total Questões
		div.css-bxvhhl - Importancia e Nota
			p.css-sz9ejl data-testid="sinal-obrigatorio" - Sinal de obrigatório
			p.css-1wgaj9w - Pontos da questão
	div.css-rcuo3b - Instruções da questão (Título)
		div.css-1a4wlpz - Conteúdo da questão (Texto do título)
			p - Conteúdo
				span.ql-formula data-value="" - Formulas
	div.(Tipo de alternativas).css-1h7anqn - Alternativas e Tipo de alternativas
		div.css-9whsf3 - Alternativa
			div.css-10zfeld - Conteúdo da alteranativa (Btn e Valor da alternativa)
				label.css-dpvp45 - Btn selecionar questão
					input.css-1m9pwf3 - Input do Btn selecionar
				div.css-1p78i1z - Conteúdo da alternativa
					p - Texto
						span - Letra
						span.ql-formula data-value="" - Formula
~~~
