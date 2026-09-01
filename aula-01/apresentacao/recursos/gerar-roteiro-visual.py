# -*- coding: utf-8 -*-
"""Gera a pagina com os 22 slides renderizados e o roteiro de cada um."""
import base64
import json
import os

SLIDES = [
    (1, "Desenvolvimento Mobile", "2 min", "Abertura", [
        ("fala", "Boa noite, pessoal. Eu sou o Emanuel Nascente e vou acompanhar vocês na disciplina de Desenvolvimento Mobile. Hoje eu não quero que vocês saiam daqui decorando código. Quero que saiam entendendo o que é desenvolvimento mobile e quais caminhos podemos usar para construir um aplicativo."),
        ("foco", "Acolhimento · reduzir ansiedade · avisar que há prática sem cobrança de sintaxe."),
        ("transicao", "“Antes de falar de tecnologia, quero mostrar como organizei nosso primeiro encontro.”"),
    ]),
    (2, "Plano da primeira aula", "3 min", "Abertura", [
        ("fala", "A aula está dividida em duas partes. Na primeira, nos apresentamos e vemos as diferenças entre Web e Mobile, depois Nativo e Híbrido. Depois do intervalo entramos na parte prática."),
        ("meta", "“No final da aula eu quero perguntar a qualquer um de vocês qual a diferença entre Web, Mobile nativo e híbrido — e vocês conseguirem explicar com suas palavras.”"),
        ("evitar", "Não explicar cada tecnologia do semestre aqui. O slide é só um mapa."),
    ]),
    (3, "Apresentação do professor", "6–8 min", "Abertura", [
        ("fala", "Gosto de trabalhar a programação entendendo primeiro o problema que estamos resolvendo. Vocês vão perceber que eu não quero mostrar só qual código escrever, mas por que escolhemos determinada solução."),
        ("foco", "Fluxo das aulas: conceito → demonstração → prática. Errar faz parte."),
        ("evitar", "Transformar em currículo profissional longo."),
    ]),
    (4, "Apresentação dos alunos", "~30 min", "Diagnóstico", [
        ("fala", "Vamos manter aproximadamente um minuto por pessoa. Não é entrevista e não existe resposta certa. Quero descobrir o que vocês já viram nos módulos anteriores."),
        ("anotar", "Recorrências: Java · JavaScript · PHP · Python · HTML/CSS · banco de dados · OO · Git · APIs · quem já tentou criar apps."),
        ("atencao", "O slide prevê 25 min. Conte com ~30 — alunos passam do minuto. Use o material “Mapa da Turma” para manter a turma ativa enquanto os colegas falam."),
    ]),
    (5, "O que vamos aprender no semestre", "6 min", "Panorama", [
        ("fala", "Hoje começamos pelo primeiro bloco: entender o ecossistema mobile e as formas de construir uma aplicação. Mais adiante: Android nativo com Kotlin, o papel do Java, React Native e Flutter, UX, testes e publicação."),
        ("foco", "Mostrar continuidade sem aprofundar nenhum item."),
    ]),
    (6, "Pergunta de partida", "7–8 min", "Conceito", [
        ("fala", "Um site aberto no celular é um aplicativo mobile? — Pare e espere. Peça dois ou três argumentos antes de seguir."),
        ("foco", "A pergunta separa duas coisas: o dispositivo onde o usuário está e a forma como o software foi construído e entregue."),
        ("atencao", "Não diga que aplicações web “não acessam recursos do aparelho”. Navegadores modernos acessam vários. O ponto certo é que apps instalados têm integração mais direta e controlada pelo sistema."),
    ]),
    (7, "Aplicação Web × Aplicação Mobile", "10 min", "Conceito", [
        ("fala", "Usuário → navegador → aplicação web → servidor/API. Quando falamos de app instalado, existe outra camada: ele executa dentro do Android ou iOS e segue as regras daquele sistema."),
        ("pergunta", "“Pensem em um app bancário. O que muda quando eu tenho o aplicativo instalado em vez de entrar pelo navegador?” — biometria, notificações, câmera para QR Code."),
        ("foco", "Não é que Web seja inferior. São ambientes de execução e distribuição diferentes."),
    ]),
    (8, "E o meio-termo? PWA", "5 min", "Conceito", [
        ("novo", "Slide novo. Fecha uma lacuna real: os slides 7 e 9 tratavam Web × Mobile como binário."),
        ("fala", "Existe um meio-termo que vocês conhecem na prática: o site que pede “adicionar à tela de início” e depois abre sem a barra do navegador."),
        ("foco", "Reforça a tese do slide 6 em vez de enfraquecê-la: a diferença está em como o software é executado e distribuído, não no aparelho onde aparece."),
        ("atencao", "Alguém da turma vai levantar isso de qualquer jeito. Melhor ter a resposta preparada."),
    ]),
    (9, "Recursos que tornam o mobile diferente", "7 min", "Conceito", [
        ("fala", "Quando desenvolvemos para mobile, olhamos o aparelho como parte da aplicação: câmera, GPS, biometria, Bluetooth, notificações, sensores."),
        ("pergunta", "“Qual desses recursos vocês usaram hoje?” — WhatsApp, Uber, banco, fones."),
        ("foco", "Preparar a ideia: quanto mais o projeto depende de integração específica, mais isso influencia a escolha tecnológica."),
    ]),
    (10, "Aplicativo nativo", "8 min", "Conceito", [
        ("fala", "Nativo é construir com tecnologias diretamente ligadas à plataforma. No Android, Kotlin é a principal hoje, com Java ainda presente em muitos projetos. No iOS, Swift."),
        ("chave", "“Nativo não significa automaticamente melhor. Significa que estou trabalhando diretamente com o ecossistema daquela plataforma.”"),
        ("design", "Os ícones de Kotlin, Android e Apple estão nas telas dos aparelhos — ajudam o aluno a associar marca e plataforma."),
    ]),
    (11, "Aplicativo híbrido / multiplataforma", "8 min", "Conceito", [
        ("fala", "Uma abordagem em que compartilhamos parte importante da base entre plataformas, em vez de manter um projeto totalmente separado para cada uma."),
        ("chave", "“Compartilhar código não significa que tudo será 100% igual. Em projetos reais ainda existem adaptações por plataforma.”"),
        ("transicao", "“Então qual é melhor? Essa pergunta, do jeito que está, é a pergunta errada.”"),
    ]),
    (12, "Comparação simples", "7 min", "Conceito", [
        ("fala", "Não quero que vocês terminem dizendo “nativo é melhor” ou “React Native é melhor”. Quero que perguntem: melhor para qual problema?"),
        ("criterios", "1. Plataformas · 2. Equipe · 3. Prazo · 4. Integração · 5. Manutenção"),
        ("atencao", "Não ensine como regra absoluta. São tendências e trade-offs, não leis."),
    ]),
    (13, "Mitos que vamos desfazer", "6 min", "Conceito", [
        ("novo", "Slide novo. Traz para a turma a seção 8 do roteiro, que até então existia só para o professor."),
        ("fala", "Percorra os seis mitos. Pergunte se alguém já ouviu alguma dessas frases — provavelmente vários já ouviram."),
        ("foco", "É o slide mais fotografável da aula. O aluno leva essas seis frases para a entrevista de estágio."),
        ("chave", "“Nenhuma dessas frases é regra. Todas são trade-offs que dependem do contexto.”"),
    ]),
    (14, "Atividade relâmpago", "5–7 min", "Prática", [
        ("fala", "Cenário A: delivery para Android e iPhone, equipe pequena, pouco tempo. Depois mude: câmera, sensores, Bluetooth passam a ser centrais. Mantêm a escolha?"),
        ("foco", "Pergunte sempre: “qual requisito fez você escolher isso?”"),
    ]),
    (15, "Intervalo", "10–15 min", "Pausa", [
        ("planoA", "“Na volta vamos direto para os computadores. Primeiro uma verificação rápida do ambiente.”"),
        ("planoB", "“Na volta vocês vão trabalhar em equipes, cada uma com um cenário de projeto.”"),
        ("atencao", "Ponto de decisão. Faça o health check em no máximo 5 minutos."),
    ]),
    (16, "Laboratório 01", "5 min", "Plano A", [
        ("fala", "Vamos criar dois projetos que mostram praticamente a mesma coisa na tela. A diferença está no caminho que usamos para chegar lá."),
        ("foco", "Não tentem entender cada arquivo. Observem ferramenta, linguagem, estrutura e forma de execução."),
    ]),
    (17, "Antes de começar: checklist", "5 min", "Plano A", [
        ("fala", "Android Studio abre? Existe SDK? Temos emulador ou celular? node -v funciona? Temos internet?"),
        ("atencao", "Acrescente uma verificação que não está no slide: se ~/.gradle/caches estiver vazio, a primeira build leva ~15 minutos por máquina. Vazio na maioria → vá para o Plano B."),
        ("evitar", "Não comece a instalar Android Studio ou SDK durante a aula."),
    ]),
    (18, "Parte A — Criando um app nativo", "35 min", "Plano A", [
        ("corrigido", "O código deste slide foi corrigido. O trecho anterior mostrava a MainActivity inteira e não compilava — faltavam os imports do Compose."),
        ("fala", "Neste momento quero que reconheçam duas coisas: isso é Kotlin, e a interface está sendo declarada com Jetpack Compose."),
        ("atencao", "Avise a turma que o slide é ilustrativo. A alteração real é trocar só o texto dentro da função Greeting gerada pelo template."),
        ("ordem", "Execução: 1) emulador pronto · 2) celular autorizado · 3) Compose Preview, se estiver demorando."),
    ]),
    (19, "Parte B — Criando um app híbrido", "30 min", "Plano A", [
        ("corrigido", "O comando foi corrigido para incluir --template blank. Sem ele, o Expo gera projeto com expo-router e o App.js que aparece no slide não existe."),
        ("fala", "Aqui aparece JavaScript, componentes como View e Text, e uma estrutura completamente diferente da que acabamos de ver no Android Studio."),
        ("pergunta", "“Onde está o Android Studio neste fluxo?” — é a pergunta mais importante do slide."),
        ("dica", "Sem emulador e sem celular: npx expo start --web resolve a Parte B inteira no navegador."),
    ]),
    (20, "Comparando os dois projetos", "15 min", "Plano A", [
        ("novo", "Foi acrescentada a linha “tempo até a primeira tela”, que não existia."),
        ("fala", "Para o usuário, as duas telas parecem iguais. Para nós, o caminho foi completamente diferente."),
        ("foco", "A diferença de tempo eles acabaram de sentir esperando o Gradle. Nomear isso logo depois fixa mais que qualquer explicação teórica."),
        ("pergunta", "“Se o resultado visual é parecido, onde está a diferença?”"),
    ]),
    (21, "Fechamento da aula", "10 min", "Encerramento", [
        ("fala", "Tentem explicar com as próprias palavras, sem definição de livro."),
        ("dica", "Use a Folha de Fechamento impressa. Dita em voz alta, você ouve 3 alunos; impressa, você leva 25 diagnósticos para planejar a aula 02."),
        ("atencao", "Se muitos ainda responderem “nativo é melhor porque é mais rápido”, retome a ideia de contexto antes de encerrar."),
    ]),
    (22, "Obrigado + próxima aula", "5 min", "Encerramento", [
        ("novo", "O slide era só “Obrigado!”. Agora carrega a prévia da aula 02 e uma pergunta para levar para casa."),
        ("fala", "Hoje o objetivo era abrir o mapa da disciplina. Na próxima aula avançamos na base técnica do ecossistema Android."),
        ("foco", "Este é o slide que fica projetado enquanto a turma guarda as coisas. Agora ele trabalha nesse tempo."),
    ]),
]

ROTULOS = {
    "fala": ("Fala sugerida", "fala"),
    "foco": ("Foco", "foco"),
    "transicao": ("Transição", "foco"),
    "meta": ("Meta do encontro", "foco"),
    "evitar": ("Evitar", "alerta"),
    "atencao": ("Atenção", "alerta"),
    "anotar": ("Anotar", "foco"),
    "pergunta": ("Pergunta para a turma", "fala"),
    "chave": ("Mensagem-chave", "chave"),
    "criterios": ("Critérios", "foco"),
    "novo": ("Novidade nesta versão", "novo"),
    "corrigido": ("Correção aplicada", "novo"),
    "design": ("Design", "foco"),
    "dica": ("Dica", "foco"),
    "ordem": ("Ordem de execução", "foco"),
    "planoA": ("Se for Plano A", "foco"),
    "planoB": ("Se for Plano B", "foco"),
}


def build():
    b64 = json.load(open("slides_b64.json"))

    partes = []
    for num, titulo, tempo, bloco, itens in SLIDES:
        chave = f"{num:02d}"
        img = b64.get(chave, "")

        blocos = []
        for tipo, texto in itens:
            rot, cls = ROTULOS.get(tipo, ("Nota", "foco"))
            blocos.append(
                f'<div class="nota {cls}"><span class="rot">{rot}</span>'
                f'<p>{texto}</p></div>'
            )

        novo = any(t in ("novo", "corrigido") for t, _ in itens)
        selo = '<span class="selo">alterado</span>' if novo else ""

        partes.append(f"""
<article class="slide" id="s{num}">
  <header class="cab">
    <span class="num">{num:02d}</span>
    <div class="tit">
      <h2>{titulo}{selo}</h2>
      <p class="meta"><span class="bloco">{bloco}</span> · {tempo}</p>
    </div>
  </header>
  <div class="corpo">
    <figure><img src="data:image/png;base64,{img}" alt="Slide {num}: {titulo}" loading="lazy"></figure>
    <div class="notas">{''.join(blocos)}</div>
  </div>
</article>""")

    html = """<title>Roteiro Visual Aula 01</title>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,600;9..144,700&family=Inter:wght@400;500;600&family=JetBrains+Mono:wght@500&display=swap">
<style>
:root{
  --tinta:#14181F; --texto:#3D4653; --fraco:#6C7789;
  --fundo:#FBFAF8; --papel:#FFFFFF; --linha:#E6E3DE;
  --marca:#D71920; --ouro:#FFD322;
  --fala:#0B5C63; --falaBg:#EEF6F6;
  --alerta:#8A4B00; --alertaBg:#FFF6EA;
  --novo:#1F5F3A; --novoBg:#EDF7F0;
  --chaveBg:#FFF7E8;
}
@media (prefers-color-scheme: dark){:root:not([data-theme="light"]){
  --tinta:#F2F0EC; --texto:#C3C9D4; --fraco:#8B95A6;
  --fundo:#12141A; --papel:#191C24; --linha:#2A2F3A;
  --marca:#FF6B6B; --ouro:#FFD322;
  --fala:#7FD8DF; --falaBg:#122A2C;
  --alerta:#F0B45E; --alertaBg:#2C2214;
  --novo:#83D9A5; --novoBg:#13291D;
  --chaveBg:#2A2415;
}}
:root[data-theme="dark"]{
  --tinta:#F2F0EC; --texto:#C3C9D4; --fraco:#8B95A6;
  --fundo:#12141A; --papel:#191C24; --linha:#2A2F3A;
  --marca:#FF6B6B; --ouro:#FFD322;
  --fala:#7FD8DF; --falaBg:#122A2C;
  --alerta:#F0B45E; --alertaBg:#2C2214;
  --novo:#83D9A5; --novoBg:#13291D;
  --chaveBg:#2A2415;
}
*{box-sizing:border-box}
body{background:var(--fundo);color:var(--texto);
  font:400 16px/1.6 Inter,system-ui,-apple-system,"Segoe UI",sans-serif;}
.wrap{max-width:1180px;margin:0 auto;padding:0 24px 96px}

.topo{padding:64px 0 40px;border-bottom:3px solid var(--marca);margin-bottom:8px;position:relative}
.topo::after{content:"";position:absolute;left:0;bottom:-3px;width:120px;height:3px;background:var(--ouro)}
.kicker{font:500 12px/1 "JetBrains Mono",ui-monospace,monospace;letter-spacing:.14em;
  text-transform:uppercase;color:var(--marca);margin:0 0 14px}
h1{font:700 clamp(32px,5vw,52px)/1.05 Fraunces,Georgia,serif;color:var(--tinta);
  margin:0 0 14px;text-wrap:balance;letter-spacing:-.015em}
.sub{font-size:17px;color:var(--fraco);margin:0;max-width:62ch}

.resumo{display:grid;grid-template-columns:repeat(auto-fit,minmax(150px,1fr));
  gap:1px;background:var(--linha);border:1px solid var(--linha);border-radius:12px;
  overflow:hidden;margin:36px 0 56px}
.resumo div{background:var(--papel);padding:18px 20px}
.resumo b{display:block;font:700 26px/1 Fraunces,Georgia,serif;color:var(--tinta);
  font-variant-numeric:tabular-nums;margin-bottom:6px}
.resumo span{font:500 11px/1.3 "JetBrains Mono",ui-monospace,monospace;
  letter-spacing:.08em;text-transform:uppercase;color:var(--fraco)}

.slide{background:var(--papel);border:1px solid var(--linha);border-radius:14px;
  padding:26px;margin-bottom:26px}
.cab{display:flex;gap:18px;align-items:flex-start;
  padding-bottom:18px;border-bottom:1px solid var(--linha);margin-bottom:22px}
.num{font:700 15px/1 "JetBrains Mono",ui-monospace,monospace;color:var(--marca);
  background:var(--fundo);border:1px solid var(--linha);border-radius:8px;
  padding:9px 11px;flex:none;font-variant-numeric:tabular-nums}
.tit h2{font:600 22px/1.25 Fraunces,Georgia,serif;color:var(--tinta);margin:0 0 6px;
  text-wrap:balance;display:flex;gap:10px;align-items:center;flex-wrap:wrap}
.meta{margin:0;font:500 12px/1 "JetBrains Mono",ui-monospace,monospace;
  letter-spacing:.06em;text-transform:uppercase;color:var(--fraco)}
.bloco{color:var(--marca)}
.selo{font:500 10px/1 "JetBrains Mono",ui-monospace,monospace;letter-spacing:.1em;
  text-transform:uppercase;color:var(--novo);background:var(--novoBg);
  border:1px solid var(--novo);border-radius:99px;padding:4px 9px}

.corpo{display:grid;grid-template-columns:minmax(0,1.25fr) minmax(0,1fr);gap:26px;align-items:start}
@media(max-width:900px){.corpo{grid-template-columns:1fr}}
figure{margin:0}
figure img{width:100%;height:auto;display:block;border:1px solid var(--linha);border-radius:10px}
.notas{display:flex;flex-direction:column;gap:12px}

.nota{border-radius:10px;padding:14px 16px;border:1px solid var(--linha);background:var(--fundo)}
.nota .rot{display:block;font:500 10px/1 "JetBrains Mono",ui-monospace,monospace;
  letter-spacing:.1em;text-transform:uppercase;color:var(--fraco);margin-bottom:8px}
.nota p{margin:0;font-size:14.5px;line-height:1.62;color:var(--texto)}
.nota.fala{background:var(--falaBg);border-color:transparent}
.nota.fala .rot{color:var(--fala)}
.nota.fala p{color:var(--tinta);font-style:italic}
.nota.alerta{background:var(--alertaBg);border-color:transparent}
.nota.alerta .rot{color:var(--alerta)}
.nota.novo{background:var(--novoBg);border-color:transparent}
.nota.novo .rot{color:var(--novo)}
.nota.chave{background:var(--chaveBg);border-color:transparent}
.nota.chave p{color:var(--tinta);font-weight:500}

footer{margin-top:56px;padding-top:26px;border-top:1px solid var(--linha);
  font-size:13.5px;color:var(--fraco)}
footer b{color:var(--tinta)}
</style>

<div class="wrap">
  <header class="topo">
    <p class="kicker">Escola Técnica Mesquita · Curso Técnico em Informática</p>
    <h1>Desenvolvimento Mobile — Aula 01</h1>
    <p class="sub">Os 22 slides da apresentação revisada, com o roteiro de condução de cada um:
    tempo, fala sugerida, o que enfatizar e o que evitar.</p>
  </header>

  <section class="resumo">
    <div><b>22</b><span>slides</span></div>
    <div><b>4h</b><span>duração</span></div>
    <div><b>2</b><span>slides novos</span></div>
    <div><b>3</b><span>correções</span></div>
    <div><b>16</b><span>aparelhos refeitos</span></div>
  </section>

  __SLIDES__

  <footer>
    <p><b>Alterações desta versão:</b> dois slides novos (PWA e Mitos), correção do código Kotlin
    do slide 18 e do comando Expo do slide 19, linha de tempo de build no slide 20, slide final
    com prévia da aula 02, e redesenho dos 16 aparelhos com os ícones reais das tecnologias.</p>
    <p>Identidade visual da Escola Técnica Mesquita preservada.</p>
  </footer>
</div>"""

    html = html.replace("__SLIDES__", "\n".join(partes))
    destino = os.path.join(os.path.dirname(os.path.abspath(__file__)), "roteiro-visual.html")
    open(destino, "w", encoding="utf-8").write(html)
    print(f"gerado: {destino} ({len(html)/1024/1024:.2f} MB)")


if __name__ == "__main__":
    build()
