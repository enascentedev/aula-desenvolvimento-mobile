# Roteiro slide a slide — Aula 01

> Leia antes: [analise-apresentacao.md](analise-apresentacao.md), que lista duas
> correções obrigatórias nos slides 16 e 17.

---

## Slide 1 — Desenvolvimento Mobile · 2 min

**Objetivo:** acolher a turma e apresentar a ideia central do encontro.

> "Boa noite, pessoal. Eu sou o Emanuel Nascente e vou acompanhar vocês na
> disciplina de Desenvolvimento Mobile. Como é nosso primeiro encontro, hoje a
> aula vai ter um formato um pouco diferente. Primeiro quero conhecer vocês e
> entender o que já estudaram no curso. Depois vamos começar a entrar no
> conteúdo e, na segunda parte, vamos fazer uma atividade prática. Hoje eu não
> quero que vocês saiam daqui decorando código. Quero que saiam entendendo o que
> é desenvolvimento mobile e quais caminhos podemos usar para construir um
> aplicativo."

**Foco:** acolhimento · reduzir ansiedade · haverá prática sem cobrança de
sintaxe · introduzir "caminhos diferentes para construir um app".

**Transição:** *"Antes de falar de tecnologia, quero mostrar rapidamente como
organizei nosso primeiro encontro."*

---

## Slide 2 — Plano da primeira aula · 3 min

**Objetivo:** dar previsibilidade à turma.

> "A aula está dividida em duas partes. Na primeira, vamos nos apresentar,
> conhecer a disciplina e entender algumas diferenças importantes: Web e Mobile,
> depois Nativo e Híbrido. Depois do intervalo entramos na parte prática. Se a
> apresentação da turma for mais rápida, ótimo: ganhamos tempo para conversar
> sobre os conceitos. Se levar mais tempo, sem problema; eu ajusto o ritmo."

**Destaque a meta do encontro:**

> "No final da aula, eu quero conseguir perguntar a qualquer um de vocês: 'qual a
> diferença entre Web, Mobile nativo e uma solução híbrida/multiplataforma?' e
> vocês conseguirem me explicar com suas próprias palavras."

**Evitar:** explicar cada tecnologia do semestre. O slide é apenas um mapa.

---

## Slide 3 — Apresentação do professor · 6–8 min

> "Meu nome é Emanuel Nascente. Minha área é desenvolvimento de software e eu
> gosto de trabalhar a programação tentando entender primeiro o problema que
> estamos resolvendo. Vocês vão perceber que nas nossas aulas eu não quero
> mostrar somente 'qual código escrever', mas também **por que** estamos
> escolhendo determinada solução."

> "As aulas seguem normalmente um fluxo parecido: primeiro um conceito, depois
> uma demonstração e, sempre que fizer sentido, uma prática. Errar durante a
> prática faz parte. Se algo não funcionar, a gente tenta entender por quê."

> "O que eu espero de vocês é participação. Não precisam saber tudo e não
> precisam ter vergonha de perguntar. Às vezes uma dúvida que parece simples é
> exatamente o ponto que metade da turma também não entendeu."

**Evitar:** transformar em currículo profissional longo.

---

## Slide 4 — Apresentação dos alunos · ~30 min

**Objetivo:** conhecer a turma e diagnosticar conhecimentos prévios.

> "Agora quero conhecer vocês. Como a turma é grande, vamos tentar manter
> aproximadamente um minuto por pessoa. Não é entrevista e não existe resposta
> certa. Quero principalmente descobrir o que vocês já viram nos módulos
> anteriores e o que esperam dessa disciplina."

Leia as perguntas do slide e **dê um exemplo rápido de resposta**, para calibrar
o nível de detalhe esperado.

### Anote as recorrências

Java · JavaScript · PHP · Python · HTML/CSS · banco de dados · orientação a
objetos · Git/GitHub · APIs · quem já tentou criar apps.

### Perguntas para a turma toda (sem resposta individual)

> "Quem aqui já usou Java?"
> "Quem já trabalhou com JavaScript?"
> "Quem já ouviu falar em Kotlin, React Native ou Flutter?"

> ⏱️ O slide prevê 25 min (25 × 1 min). Na prática, conte com ~30. Alunos
> costumam passar do minuto.

---

## Slide 5 — O que vamos aprender no semestre · 6 min

> "Esses são os grandes assuntos que vamos percorrer. Hoje começamos pelo
> primeiro bloco: entender o ecossistema mobile e as diferentes formas de
> construir uma aplicação."

> "Mais adiante vamos trabalhar Android nativo, principalmente com Kotlin, o
> papel do Java, abordagens híbridas/multiplataforma como React Native e
> Flutter, e também UX, testes, depuração e publicação."

> "O importante é perceber que isso forma um ciclo. Um aplicativo não é somente
> código. Existe ideia, interface, regras, integração com o dispositivo, teste e
> entrega."

**Foco:** mostrar continuidade, sem aprofundar nenhum item.

**Transição:** *"Antes de falar em Kotlin, React Native ou Flutter, precisamos
responder uma pergunta mais básica."*

---

## Slide 6 — Pergunta de partida · 7–8 min

> ### "Um site aberto no celular é um aplicativo mobile?"

**Pare e espere respostas.** Peça dois ou três argumentos antes de seguir.

> "A pergunta parece simples, mas é útil porque nos obriga a separar duas coisas:
> o **dispositivo** em que o usuário está e a **forma como o software foi
> construído e entregue**."

> "Eu posso abrir um sistema web no celular. Ele continua sendo uma aplicação web
> executada pelo navegador. Também posso ter um aplicativo instalado, executado
> dentro do ecossistema Android ou iOS."

### ⚠️ Cuidado conceitual

Evite dizer que aplicações web "não acessam recursos do aparelho". Navegadores
modernos acessam vários recursos, conforme plataforma e permissões. O ponto
correto: **apps instalados costumam ter integração mais direta e controlada pelo
sistema operacional.**

---

## Slide 7 — Aplicação Web × Aplicação Mobile · 10 min

> "Em uma aplicação web temos, de forma simplificada, o usuário, o navegador, a
> aplicação feita com tecnologias web e, muitas vezes, um servidor ou API atrás.
> O usuário normalmente entra por uma URL."

Aponte visualmente: **Usuário → navegador → aplicação web → servidor/API**

> "Quando falamos de um app instalado, existe uma camada diferente. O aplicativo
> é instalado no dispositivo, executa dentro de Android ou iOS e precisa seguir
> as regras daquele sistema operacional."

### Pergunta para a turma

> "Pensem em um app bancário. O que muda na experiência quando eu tenho o
> aplicativo instalado em vez de entrar só pelo navegador?"

Explore: biometria · notificações · câmera para QR Code · acesso mais direto ·
experiência otimizada.

**Foco:** não é que Web seja inferior. São **ambientes de execução e distribuição
diferentes**.

---

## Slide 8 — Recursos que tornam o Mobile diferente · 7 min

> "Quando desenvolvemos para mobile, começamos a olhar o aparelho como parte da
> aplicação. O telefone tem câmera, GPS, biometria, Bluetooth, armazenamento,
> notificações e vários sensores."

> "Qual desses recursos vocês usaram hoje através de algum aplicativo?"

Explore: WhatsApp → câmera, microfone, armazenamento, notificações · Uber → GPS ·
banco → biometria, câmera · fones e relógios → Bluetooth.

**Não** entrar em código de permissões. A ideia a preparar é:

> "Quanto mais nosso projeto depende de uma integração específica com a
> plataforma, mais essa necessidade influencia a escolha tecnológica."

---

## Slide 9 — Aplicativo nativo · 8 min

> "Desenvolvimento nativo é construir o aplicativo com tecnologias diretamente
> ligadas à plataforma. No Android, hoje o Kotlin é a principal linguagem, embora
> Java tenha muita importância histórica e continue em muitos projetos. No iOS,
> temos Swift e o ecossistema da Apple."

> "O ponto principal: cada plataforma tem suas próprias ferramentas, APIs,
> convenções e formas de construir a interface."

**Exemplo:** *"Se uma empresa decide construir Android e iOS de forma totalmente
nativa, ela pode acabar mantendo duas frentes."*

### Mensagem-chave

> "Nativo não significa automaticamente melhor. Significa que estou trabalhando
> diretamente com o ecossistema daquela plataforma."

**Transição:** *"Mas imagine uma empresa pequena que precisa lançar para Android
e iPhone ao mesmo tempo."*

---

## Slide 10 — Aplicativo híbrido / multiplataforma · 8 min

> "A ementa usa o termo 'híbrido' e cita React Native e Flutter. Nesta primeira
> aula vou tratar de forma simplificada como uma abordagem em que conseguimos
> compartilhar uma parte importante da base de desenvolvimento entre plataformas."

> "Em vez de um projeto totalmente separado para Android e outro para iOS,
> frameworks como React Native e Flutter permitem compartilhar bastante coisa."

### ⚠️ Cuidado conceitual

> "Mais adiante podemos diferenciar melhor os termos híbrido e multiplataforma.
> Hoje o objetivo é entender o contraste geral pedido pela ementa."

### Mensagem-chave

> "Compartilhar código não significa que tudo será 100% igual. Em projetos reais
> ainda podem existir adaptações específicas para Android ou iOS."

**Transição:** *"Então qual é melhor? Essa pergunta, do jeito que está, é a
pergunta errada."*

---

## Slide 11 — Comparação simples · 7 min

> "Eu não quero que vocês terminem esta aula dizendo 'nativo é melhor' ou 'React
> Native é melhor'. Quero que perguntem: **melhor para qual problema?**"

Leia a tabela relacionando-a aos cinco critérios:

| # | Critério | Pergunta |
|---|---|---|
| 1 | Plataformas | Android apenas ou Android e iOS? |
| 2 | Equipe | Qual tecnologia a equipe domina e quantas pessoas temos? |
| 3 | Prazo | Precisamos chegar rápido a mais de uma plataforma? |
| 4 | Integração | Dependemos de APIs específicas, hardware ou comportamento da plataforma? |
| 5 | Manutenção | Queremos compartilhar código ou aceitamos projetos separados? |

### ⚠️ Não ensine como regra absoluta

- ~~"Bluetooth exige nativo"~~
- ~~"híbrido é sempre mais lento"~~
- ~~"multiplataforma é sempre mais barato"~~
- ~~"nativo sempre entrega melhor UX"~~

São **tendências e trade-offs**, não leis.

---

## Slide 12 — Atividade relâmpago · 5–7 min

> "Cenário A: uma pequena empresa precisa lançar um delivery para Android e
> iPhone em pouco tempo. Equipe pequena. O que vocês tenderiam a escolher?"

Ouça argumentos. Depois:

> "Agora eu mudo o problema: câmera, sensores, Bluetooth e recursos muito
> específicos do aparelho passam a ser centrais. Vocês mantêm a mesma escolha?"

**Pergunte sempre:** *"Qual requisito fez você escolher isso?"*

- **Se for usar Plano A:** *"Depois do intervalo vamos ver como esses dois
  caminhos começam na prática."*
- **Se for usar Plano B:** *"Depois do intervalo vocês vão assumir o papel da
  equipe que precisa tomar essa decisão."*

---

## Slide 13 — Intervalo · 10–15 min

- **Plano A:** *"Na volta vamos direto para os computadores. Primeiro uma
  verificação rápida do ambiente. Se a estrutura estiver disponível, criaremos
  dois projetos simples."*
- **Plano B:** *"Na volta vocês vão trabalhar em equipes. Cada equipe recebe um
  cenário e terá que defender uma decisão técnica."*

---

# 🔀 Ponto de decisão

Health check de **no máximo 5 minutos**. Detalhes e critérios em:

- ▶️ [plano-a-laboratorio/](plano-a-laboratorio/) — se o ambiente estiver pronto
- ▶️ [plano-b-dinamica/](plano-b-dinamica/) — se não estiver

---

## Slide 19 — Fechamento · 10 min

> "Antes de encerrar, quero fazer uma checagem rápida do que ficou da aula. Não
> precisa responder com definição de livro. Tentem explicar com as próprias
> palavras."

- **Se usou Plano A:** *"Qual diferença vocês perceberam entre criar o projeto no
  Android Studio e criar com Expo?"*
- **Se usou Plano B:** *"Qual critério foi mais difícil de avaliar na dinâmica?"*

### ⚠️ O que observar

Se muitos alunos ainda responderem *"nativo é melhor porque é mais rápido"* ou
*"híbrido é melhor porque serve para tudo"*, **retome a ideia de contexto antes
de encerrar**.

---

## Slide 20 — Obrigado · 5 min

> "Hoje o objetivo era abrir o mapa da disciplina. Vimos que um software usado no
> celular pode ter caminhos diferentes e começamos a entender o que influencia
> uma decisão entre nativo e híbrido/multiplataforma."

> "Na próxima aula vamos avançar na base técnica do ecossistema Android e,
> conforme eu tiver as respostas de vocês e perceber o nível da turma, ajustamos
> o ritmo."

Finalize:

> "Antes de irmos embora: ficou alguma dúvida que vocês gostariam que eu
> retomasse na próxima aula?"

---

# Pontos conceituais que o professor deve proteger

1. **Web no celular não vira automaticamente Mobile nativo.** O ambiente de
   execução continua importando.
2. **Web também acessa alguns recursos do aparelho.** A divisão não é absoluta.
3. **Nativo não é sempre melhor.** É uma escolha com vantagens e custos.
4. **Multiplataforma não significa 100% de código compartilhado.** Pode haver
   código específico por plataforma.
5. **React Native e Flutter acessam muitos recursos nativos.** Não ensine que
   câmera, GPS ou Bluetooth obrigam desenvolvimento nativo.
6. **Performance é contextual.** Evite "nativo é sempre rápido, híbrido é sempre
   lento".
7. **Prazo e custo dependem da equipe.** Uma equipe especialista em Kotlin pode
   entregar Android nativo mais rápido do que aprender um framework novo.
8. **A escolha é um conjunto de trade-offs.** Esta é a principal mensagem da
   primeira aula.
