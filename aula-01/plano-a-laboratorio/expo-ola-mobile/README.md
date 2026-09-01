# Parte B — "Olá, Mobile!" com React Native + Expo

Esta pasta contém **apenas o [App.js](App.js)**. O projeto em si os alunos criam
na aula — a ideia é que eles vejam o processo, não recebam tudo pronto.

## Criar o projeto

```bash
npx create-expo-app@latest PrimeiroAppHibrido --template blank
cd PrimeiroAppHibrido
```

> ⚠️ **O `--template blank` é obrigatório.** Sem ele o Expo gera um projeto com
> `expo-router` e pasta `app/`, e o `App.js` que aparece no slide 17 **não
> existe**. O aluno abre o VS Code e não acha o arquivo.

Depois substitua o `App.js` gerado pelo [App.js](App.js) desta pasta.

## Executar

```bash
npx expo start
```

Com emulador disponível, pressione `a` no terminal. Com celular, use o QR Code
e o app **Expo Go**.

### Sem emulador e sem celular

O Expo roda no navegador:

```bash
npx expo install react-dom react-native-web @expo/metro-runtime
npx expo start --web
```

Abre em `http://localhost:8081`. **Verificado e funcionando** — é o caminho mais
seguro para um laboratório com ambiente irregular.

> Ressalva didática: o preview web usa `react-native-web`, que traduz os
> componentes para HTML. Alguns detalhes visuais diferem do app nativo.

## O que mostrar aos alunos — só três coisas

| Arquivo | O que dizer |
|---|---|
| `App.js` | "É aqui que a tela é escrita" |
| `package.json` | "As dependências do projeto" |
| `node_modules` | "Contém as bibliotecas. Não vamos abrir." |

## Perguntas durante a espera

> "Qual linguagem apareceu agora?"
> "Onde está o Android Studio neste fluxo?"
> "Este projeto foi pensado somente para Android?"

A segunda pergunta é a mais importante: **não há Android Studio neste caminho.**

## Fala sobre o código

> "Não vamos estudar React Native hoje. Quero apenas que vocês comparem. Aqui
> aparece JavaScript, componentes como `View` e `Text`, e uma estrutura
> completamente diferente da que acabamos de ver no Android Studio."
