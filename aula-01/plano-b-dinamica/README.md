# Plano B — Dinâmica "Nativo ou Híbrido?"

**Use quando** o laboratório não tiver condições: Android Studio ausente, SDK
incompleto, Node indisponível em boa parte das máquinas, internet fraca ou
nenhum emulador funcional.

> Esta atividade **não é uma versão inferior da aula**. Ela ataca diretamente o
> objetivo conceitual do primeiro tópico: entender a diferença entre as
> abordagens e decidir quando cada uma faz mais sentido. Em vários aspectos ela
> cumpre o objetivo da aula 01 melhor que o laboratório, porque o aluno pratica
> a **decisão**, que é a mensagem central do encontro.

## Formato

- **Turma:** ~25 alunos
- **Organização:** 5 grupos de 5
- **Tempo:** ~90 minutos

## Cronograma

| Etapa | Tempo | Material |
|---|---|---|
| Apresentar o desafio | 5 min | — |
| Explicar os 5 critérios | 10 min | [folha-decisao.md](folha-decisao.md) |
| Grupos analisam o cenário | 25 min | [cenarios.md](cenarios.md) |
| Mudança de requisito | 15 min | [mudancas-requisito.md](mudancas-requisito.md) |
| Defesa das escolhas | 30 min | ~4 min por grupo + 1 pergunta |
| Síntese no quadro | 5 min | diagrama abaixo |

## Material a levar impresso

- [ ] 5 cartões de cenário (recortados de [cenarios.md](cenarios.md))
- [ ] 5 cartões de mudança de requisito
- [ ] 5 folhas de decisão ([folha-decisao.md](folha-decisao.md))
- [ ] Canetas
- [ ] Cronômetro (celular serve)

## Enquanto circula pela sala

Não dê a resposta. Use perguntas:

- "Quantas plataformas vocês precisam atender?"
- "Qual requisito pesou mais?"
- "O que vocês ganham com essa escolha?"
- **"Qual seria a principal desvantagem da escolha de vocês?"**

A última é a mais importante — força o aluno a reconhecer trade-offs.

## Critério de sucesso

Não é escolher "Nativo" ou "Híbrido". Um grupo teve sucesso quando consegue
formular algo como:

> "Escolhemos híbrido porque precisamos de Android e iOS, a equipe é pequena e
> as funcionalidades são semelhantes nas duas plataformas. O risco é que uma
> integração específica possa exigir código nativo."

ou

> "Escolhemos nativo porque a aplicação roda apenas em Android e depende
> fortemente de um SDK específico do hardware. O custo é que, se iOS entrar
> depois, teremos que rever a arquitetura."

Note que **as duas frases reconhecem o custo da própria escolha**. É isso que
está sendo avaliado.

## Síntese final no quadro

```text
REQUISITOS
    ↓
PLATAFORMAS
    ↓
EQUIPE + PRAZO
    ↓
INTEGRAÇÃO COM DISPOSITIVO
    ↓
MANUTENÇÃO
    ↓
DECISÃO TÉCNICA
```

> "Tecnologia não deve ser escolhida porque está na moda. Ela deve ser
> defendida a partir do contexto."
