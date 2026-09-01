# Aula 01 — Introdução ao Desenvolvimento Mobile

**Professor:** Emanuel Nascente
**Curso:** Técnico em Informática — 3º módulo
**Duração:** 4 horas
**Tema:** Web × Mobile e Nativo × Híbrido/Multiplataforma

## O que o aluno deve sair sabendo

Explicar, com as próprias palavras:

- a diferença entre aplicação Web e aplicação Mobile;
- o que caracteriza uma aplicação nativa;
- o que caracteriza uma abordagem híbrida/multiplataforma;
- **por que a escolha entre elas depende do contexto do projeto.**

> Esta aula **não é sobre sintaxe**. A meta é criar o mapa mental da disciplina e
> mostrar que tecnologia se escolhe em função de um problema.

## Material

| Arquivo | Para quê |
|---|---|
| [roteiro.md](roteiro.md) | Roteiro slide a slide, com falas sugeridas |
| [analise-apresentacao.md](analise-apresentacao.md) | Divergências entre os slides e a realidade — **leia antes da aula** |
| [apresentacao/](apresentacao/) | O `.pptx` da aula |
| [plano-a-laboratorio/](plano-a-laboratorio/) | Se o laboratório funcionar |
| [plano-b-dinamica/](plano-b-dinamica/) | Se não funcionar |

## Estrutura das 4 horas

| Parte | Tempo |
|---|---|
| Abertura + apresentações | 40–45 min |
| Visão geral da disciplina | 10 min |
| Web × Mobile | 20–25 min |
| Nativo × Híbrido/Multiplataforma | 30–35 min |
| Atividade relâmpago | 5–10 min |
| Margem para perguntas | 10–15 min |
| **Intervalo** | 10–15 min |
| **Plano A ou Plano B** | 90 min |
| Fechamento | 15 min |

> **Regra de segurança de tempo:** se as apresentações consumirem mais tempo,
> corte exemplos e discussões intermediárias — mas **preserve os slides 6 a 11**,
> que formam a base conceitual da aula.

## A decisão Plano A × Plano B

Faça um health check de **no máximo 5 minutos** após o intervalo.

**Plano A** só se a maioria das máquinas tiver Android Studio abrindo sem
instalar nada, SDK utilizável, emulador ou dispositivo, `node -v` funcionando e
internet suficiente.

**Vá para o Plano B imediatamente se:** várias máquinas exigirem instalação, o
Node faltar em boa parte delas, **ou o cache do Gradle estiver vazio** (a
primeira build leva ~15 minutos por máquina — veja a [análise](analise-apresentacao.md)).

> Não use a primeira aula para instalar Android Studio em 25 máquinas.

## Duas correções obrigatórias durante a aula

Detalhadas em [analise-apresentacao.md](analise-apresentacao.md):

1. **Slide 16** — o Kotlin mostrado não compila se colado (faltam imports).
   Avise: *"esse slide é ilustrativo, não copiem"*.
2. **Slide 17** — use `npx create-expo-app@latest NOME --template blank`.
   Sem `--template blank` o projeto sai com `expo-router` e o `App.js` do slide
   não existe.

## Preparação antes da aula

Se pretende usar o Plano A, teste **numa máquina do laboratório**:

```bash
node -v
npm -v
```

E confirme no Android Studio: SDK presente, Empty Activity cria, Gradle
sincroniza, existe Preview/emulador/dispositivo.

Se isso já começar a consumir tempo, o Plano B é o caminho certo.

**Para o Plano B, leve impresso:** 5 cartões de cenário, 5 de mudança de
requisito, 5 folhas de decisão, canetas e cronômetro.
