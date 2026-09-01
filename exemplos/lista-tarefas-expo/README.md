# Aplicação 1 — React Native + Expo

Lista de Tarefas em React Native. A mesma aplicação está em Kotlin nativo na pasta
`02-android-nativo`, para comparação em aula.

## Como os alunos executam (zero instalação)

1. Abrir <https://snack.expo.dev> no navegador
2. Apagar o conteúdo do arquivo `App.js` que vem por padrão
3. Colar todo o conteúdo de [App.js](App.js)
4. O preview aparece à direita, com três abas:
   - **Web** — renderiza na hora, via `react-native-web`
   - **Android / iOS** — emulador dentro da página (tem limite de tempo por sessão)
   - **My Device** — QR Code para abrir no app **Expo Go** do celular

Não é preciso criar conta. Para salvar e compartilhar o link com a turma, aí sim é
necessário fazer login.

> **Atenção didática:** o preview **Web** usa `react-native-web`, que traduz os
> componentes para HTML. Alguns detalhes visuais diferem do app nativo real.
> Vale mostrar a diferença abrindo a aba Android depois da Web.

## Rodar localmente (opcional — só na máquina do professor)

Requer apenas Node.js, que já está instalado:

```bash
npx create-expo-app@latest minha-app --template blank
cd minha-app
# substituir o App.js gerado pelo App.js desta pasta
npx expo start --web      # abre no navegador
npx expo start            # gera QR Code para o Expo Go
```

Custo em disco: aproximadamente 1 GB de `node_modules` por projeto.

## Conceitos que a aplicação demonstra

| Conceito | Onde aparece no código |
|---|---|
| Componente de função | `export default function App()` |
| Estado com `useState` | `texto` e `tarefas` |
| Atualização imutável do estado | `setTarefas((atual) => [...atual, nova])` |
| Renderização de lista | `FlatList` com `keyExtractor` |
| Entrada de texto controlada | `TextInput` com `value` + `onChangeText` |
| Eventos de toque | `Pressable` com `onPress` |
| Estilos | `StyleSheet.create` (Flexbox, igual à web) |
| Código condicional por plataforma | `Platform.OS === 'android'` |

## Exercícios sugeridos para a turma

1. Trocar a cor do botão e do tema
2. Adicionar um contador de tarefas concluídas ao lado do de pendentes
3. Criar um botão "Limpar concluídas"
4. Impedir tarefas duplicadas
5. Ordenar a lista deixando as concluídas por último
