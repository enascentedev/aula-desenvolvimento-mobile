# Roteiro slide a slide — Aula 01

Referente a `Aula_01_Desenvolvimento_Mobile_v2.pptx` — **22 slides**.

> **Este roteiro já está dentro do arquivo**, nas notas do apresentador. Ative
> em Apresentação de Slides → Usar Modo de Exibição do Apresentador (F5).

> Versão visual navegável, com cada slide renderizado ao lado do seu roteiro:
> https://claude.ai/code/artifact/b6c16db4-6ba3-4f98-9f9a-a7d6b0fcbab1

**Novos nesta versão:** slide 08 (fluxo Mobile) e slide 13 (Mitos).
**Corrigidos:** 18 (Kotlin), 19 (comando Expo), 20 (linha de tempo), 22 (final).

---

## BLOCO 1 — Abertura · ~50 min

### Slide 01 — Desenvolvimento Mobile · 2 min

> "Boa noite, pessoal. Eu sou o Emanuel Nascente e vou acompanhar vocês na
> disciplina de Desenvolvimento Mobile. Hoje eu não quero que vocês saiam daqui
> decorando código. Quero que saiam entendendo o que é desenvolvimento mobile e
> quais caminhos podemos usar para construir um aplicativo."

**Foco:** acolhimento · reduzir ansiedade · avisar que há prática sem cobrança de sintaxe.

---

### Slide 02 — Plano da primeira aula · 3 min

> "A aula está dividida em duas partes. Se a apresentação da turma for mais
> rápida, ganhamos tempo para os conceitos. Se levar mais, eu ajusto o ritmo."

**Meta do encontro:** *"No final da aula eu quero perguntar a qualquer um de
vocês qual a diferença entre Web, Mobile nativo e híbrido — e vocês conseguirem
explicar com as próprias palavras."*

**Evitar:** explicar cada tecnologia do semestre. O slide é só um mapa.

---

### Slide 03 — Apresentação do professor · 6–8 min

> "Gosto de trabalhar a programação entendendo primeiro o problema. Vocês vão
> perceber que eu não quero mostrar só qual código escrever, mas **por que**
> escolhemos determinada solução."

**Foco:** conceito → demonstração → prática. Errar faz parte.
**Evitar:** virar currículo profissional longo.

---

### Slide 04 — Apresentação dos alunos · ~30 min

> "Vamos manter aproximadamente um minuto por pessoa. Não é entrevista e não
> existe resposta certa."

**Use o [Mapa da Turma](impressos/mapa-da-turma.md).** Sem ele, 24 dos 25 alunos
ficam desengajados enquanto um fala. Com ele, a turma constrói no quadro o mural
das tecnologias citadas — e você sai com um diagnóstico real.

**Anotar:** Java · JavaScript · PHP · Python · HTML/CSS · banco · OO · Git · APIs.

⏱️ O slide prevê 25 min. Conte com ~30.

---

### Slide 05 — O que vamos aprender no semestre · 6 min

> "Hoje começamos pelo primeiro bloco. Mais adiante: Android nativo com Kotlin,
> o papel do Java, React Native e Flutter, UX, testes e publicação."

**Gancho do Mapa da Turma:** *"Olhem o quadro. Isso não é o que vocês vão
aprender — é o que vocês já sabem. Quase tudo ali vai reaparecer. O que muda é
o lugar onde o código roda."*

---

## BLOCO 2 — Conceito · ~55 min

### Slide 06 — Pergunta de partida · 7–8 min

> ### "Um site aberto no celular é um aplicativo mobile?"

**Pare e espere.** Peça dois ou três argumentos antes de seguir.

> "A pergunta nos obriga a separar duas coisas: o **dispositivo** onde o usuário
> está e a **forma como o software foi construído e entregue**."

⚠️ Não diga que aplicações web "não acessam recursos do aparelho". Navegadores
modernos acessam vários. O ponto certo: apps instalados têm integração mais
direta e controlada pelo sistema operacional.

---

### Slide 07 — Aplicação Web × Aplicação Mobile · 10 min

Aponte: **Usuário → navegador → aplicação web → servidor/API**

> "Pensem em um app bancário. O que muda quando eu tenho o aplicativo instalado
> em vez de entrar pelo navegador?"

Explore: biometria · notificações · câmera para QR Code · experiência otimizada.

**Foco:** não é que Web seja inferior. São ambientes de execução e distribuição
diferentes.

---

### Slide 08 — Como funciona uma aplicação Mobile? · 8 min 🆕

**Fluxo:** Usuário → App instalado → Sistema Operacional → API → Servidor / Dados

É o **espelho do slide 07**. Lá o caminho era Usuário → Navegador → Web App →
Servidor. Aqui, o mesmo percurso no mundo mobile.

> "No slide anterior vimos o caminho de uma aplicação Web: o usuário abre o
> navegador, acessa uma aplicação e ela conversa com um servidor.
>
> No Mobile, o caminho é outro. O usuário **toca no ícone** de um aplicativo que
> já está instalado no aparelho.
>
> Esse aplicativo pode ser nativo, como um Android feito com Kotlin, ou
> multiplataforma, com React Native ou Flutter.
>
> E isso não significa que ele tenha todos os dados dentro dele. Assim como na
> Web, ele consome uma API e busca informação em um servidor.
>
> A grande diferença que quero que vocês percebam é **o ambiente onde a
> aplicação está sendo executada**. Na Web temos o navegador. Aqui temos um
> aplicativo instalado e integrado ao sistema operacional."

**Frase de fechamento do slide:** *"Não precisamos abrir um navegador. O software
está instalado no dispositivo e pode se integrar diretamente aos recursos do
sistema operacional."*

**Transição para o slide 09:**

> "E quando eu digo que esse aplicativo está integrado ao sistema operacional, o
> que isso significa na prática? É justamente o que vamos ver agora: câmera,
> GPS, notificações, biometria, Bluetooth."

---

### Slide 09 — Recursos que tornam o mobile diferente · 7 min

> "Qual desses recursos vocês usaram hoje através de algum aplicativo?"

WhatsApp → câmera, microfone, notificações · Uber → GPS · banco → biometria.

**Prepara a ideia:** quanto mais o projeto depende de integração específica,
mais isso influencia a escolha tecnológica.

---

### Slide 10 — Aplicativo nativo · 8 min

> "Nativo é construir com tecnologias diretamente ligadas à plataforma. No
> Android, Kotlin é a principal hoje, com Java ainda em muitos projetos. No iOS,
> Swift."

**Mensagem-chave:** *"Nativo não significa automaticamente melhor. Significa que
estou trabalhando diretamente com o ecossistema daquela plataforma."*

---

### Slide 11 — Aplicativo híbrido / multiplataforma · 8 min

> "Uma abordagem em que compartilhamos parte importante da base entre
> plataformas, em vez de manter um projeto totalmente separado para cada uma."

**Mensagem-chave:** *"Compartilhar código não significa que tudo será 100%
igual. Em projetos reais ainda existem adaptações por plataforma."*

---

### Slide 12 — Comparação simples · 7 min

> "Não quero que vocês terminem dizendo 'nativo é melhor'. Quero que perguntem:
> **melhor para qual problema?**"

| # | Critério | Pergunta |
|---|---|---|
| 1 | Plataformas | Android apenas ou Android e iOS? |
| 2 | Equipe | Qual tecnologia dominamos e quantas pessoas somos? |
| 3 | Prazo | Precisamos chegar rápido a mais de uma plataforma? |
| 4 | Integração | Dependemos de APIs específicas ou hardware? |
| 5 | Manutenção | Compartilhar código ou aceitar projetos separados? |

---

### Slide 13 — Mitos que vamos desfazer · 6 min 🆕

Percorra os seis. Pergunte se alguém já ouviu — provavelmente vários já ouviram.

| Mito | O que dizer |
|---|---|
| "Nativo é sempre mais rápido" | Depende do app e de quem escreveu. |
| "Híbrido não acessa câmera nem GPS" | Acessa. React Native e Flutter também. |
| "Bluetooth obriga usar nativo" | Não obriga. Muda o custo da integração. |
| "Multiplataforma é sempre mais barato" | Só se a equipe já dominar o framework. |
| "Site no celular vira app" | O ambiente de execução continua sendo o navegador. |
| "Multiplataforma = 100% do código" | Quase sempre sobra código por plataforma. |

**Fechamento:** *"Nenhuma dessas frases é regra. Todas são trade-offs que
dependem do contexto."*

> É o slide mais fotografável da aula — o aluno leva essas seis frases para a
> entrevista de estágio.

---

### Slide 14 — Atividade relâmpago · 5–7 min

> "Cenário A: delivery para Android e iPhone, equipe pequena, pouco tempo."
>
> Depois mude: *"câmera, sensores e Bluetooth passam a ser centrais. Mantêm a
> escolha?"*

**Pergunte sempre:** *"qual requisito fez você escolher isso?"*

---

### Slide 15 — Intervalo · 10–15 min

- **Plano A:** *"Na volta vamos direto para os computadores."*
- **Plano B:** *"Na volta vocês vão trabalhar em equipes, cada uma com um cenário."*

---

# 🔀 PONTO DE DECISÃO — health check de 5 min

**Plano A** só se a maioria tiver Android Studio abrindo sem instalar nada, SDK
utilizável, emulador ou celular, `node -v` funcionando e internet.

**Vá para o [Plano B](plano-b-dinamica/) se** várias máquinas exigirem instalação,
faltar Node, **ou o cache do Gradle estiver vazio** — a primeira build leva ~15
minutos por máquina.

---

## BLOCO 3A — Laboratório · 90 min

### Slide 16 — Laboratório 01 · 5 min

> "Vamos criar dois projetos que mostram praticamente a mesma coisa na tela. A
> diferença está no caminho que usamos para chegar lá."

---

### Slide 17 — Antes de começar: checklist · 5 min

> "Android Studio abre? Existe SDK? Temos emulador ou celular? `node -v`
> funciona? Temos internet?"

⚠️ **Acrescente ao checklist do slide:** verifique `~/.gradle/caches`. Se estiver
vazio na maioria das máquinas, a primeira build leva ~15 min cada — vá para o
Plano B.

---

### Slide 18 — Parte A: app nativo · 35 min ✅ corrigido

> "Neste momento quero que reconheçam duas coisas: isso é Kotlin, e a interface
> está sendo declarada com Jetpack Compose."

⚠️ **Avise:** *"esse slide é ilustrativo, não copiem."* A alteração real é trocar
só o texto dentro da função `Greeting` gerada pelo template.

**Ordem de execução:** 1) emulador pronto · 2) celular autorizado · 3) **Compose
Preview**, se estiver demorando.

**Mostre só três coisas:** `MainActivity.kt` · `res/` · `AndroidManifest.xml`.

---

### Slide 19 — Parte B: app híbrido · 30 min ✅ corrigido

```bash
npx create-expo-app@latest PrimeiroAppHibrido --template blank
```

⚠️ O `--template blank` é obrigatório. Sem ele o projeto sai com `expo-router` e
o `App.js` do slide não existe.

> "Onde está o Android Studio neste fluxo?" — é a pergunta mais importante daqui.

**Sem emulador nem celular:** `npx expo start --web` resolve a Parte B inteira
no navegador.

---

### Slide 20 — Comparando os dois projetos · 15 min 🆕 linha nova

| Pergunta | Nativo Android | React Native / Expo |
|---|---|---|
| Ferramenta | Android Studio | VS Code + terminal |
| Linguagem | Kotlin | JavaScript |
| Plataforma | Android | multiplataforma |
| **Tempo até a primeira tela** | **minutos (Gradle)** | **segundos** |

A última linha eles **acabaram de sentir** esperando o Gradle. Nomear isso logo
depois fixa mais que qualquer explicação teórica.

---

## BLOCO 3B — Plano B · 90 min

Ver [plano-b-dinamica/](plano-b-dinamica/) — cenários, mudanças de requisito e
folha de decisão.

---

## BLOCO 4 — Encerramento · 15 min

### Slide 21 — Fechamento da aula · 10 min

**Use a [Folha de Fechamento](impressos/folha-fechamento.md).** Perguntado em voz
alta, você ouve 3 alunos. Impresso, você leva 25 diagnósticos.

⚠️ Se muitos ainda responderem *"nativo é melhor porque é mais rápido"*, retome
a ideia de contexto antes de encerrar.

---

### Slide 22 — Obrigado + próxima aula · 5 min 🆕

> "Hoje o objetivo era abrir o mapa da disciplina. Na próxima aula avançamos na
> base técnica do ecossistema Android."

O slide agora carrega a prévia da aula 02 e uma pergunta para levar para casa:
*"escolha um app que você usa todo dia. Ele precisaria ser nativo?"*

---

# Pontos conceituais que o professor deve proteger

1. **Web no celular não vira Mobile nativo.** O ambiente de execução importa.
2. **Web também acessa alguns recursos do aparelho.** A divisão não é absoluta.
3. **Nativo não é sempre melhor.** É escolha com vantagens e custos.
4. **Multiplataforma ≠ 100% de código compartilhado.**
5. **React Native e Flutter acessam muitos recursos nativos.**
6. **Performance é contextual.**
7. **Prazo e custo dependem da equipe.**
8. **A escolha é um conjunto de trade-offs.** — a mensagem central da aula.
