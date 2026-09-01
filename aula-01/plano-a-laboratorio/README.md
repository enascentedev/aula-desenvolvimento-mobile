# Plano A — Laboratório com computadores

**Objetivo:** criar dois projetos que mostram a mesma coisa na tela — "Olá,
Mobile!" — e comparar **o caminho**, não a sintaxe.

Tempo total: ~90 minutos.

## ⚠️ Leia isto antes de escolher o Plano A

O gatilho de abandono no roteiro fala em **instalação**. Existe um segundo
risco, medido nesta máquina em 31/08/2026:

> A primeira build de um projeto Jetpack Compose levou **15 minutos**, num
> computador que **já tinha o SDK instalado**. O gargalo não foi instalar nada —
> foi o Gradle baixar ~1,1 GB de dependências AndroidX e compilar do zero.

Em 25 máquinas baixando isso ao mesmo tempo pela internet da escola, os 35
minutos previstos para a Parte A podem virar 35 minutos de barra de progresso.

**Verifique isto no health check**, em 3 ou 4 máquinas:

```powershell
# Se esta pasta não existir ou estiver vazia, a primeira build vai baixar tudo
dir $env:USERPROFILE\.gradle\caches
```

Se estiver vazia na maioria das máquinas → **vá para o Plano B**.

## Checklist de ambiente (health check, máx. 5 minutos)

| Item | Como verificar | Se falhar |
|---|---|---|
| Node.js | `node -v` | Parte B inviável |
| npm | `npm -v` | Parte B inviável |
| Android Studio | abre sem pedir instalação? | Parte A inviável |
| Android SDK | Studio reclama de SDK ausente? | Parte A inviável |
| Cache do Gradle | `dir %USERPROFILE%\.gradle\caches` | build de 15 min |
| Emulador ou celular | existe AVD? aparelho autorizado? | usar Compose Preview |
| Internet | consegue baixar o projeto Expo? | Parte B inviável |

**Regra:** se vários itens falharem em várias máquinas, não inicie troubleshooting
individual. Vá para o [Plano B](../plano-b-dinamica/).

## Parte A — Aplicativo nativo (~35 min)

Pasta: [nativo-ola-mobile/](nativo-ola-mobile/)

Os alunos criam o projeto do zero no Android Studio (New Project → Empty
Activity → `PrimeiroAppNativo` → Kotlin). Esta pasta serve como **referência
pronta** do professor: se uma máquina travar, você projeta este projeto, que já
está compilado e com as versões validadas.

### O que mostrar — só três coisas

1. `MainActivity.kt` — ponto de entrada
2. `res/` — recursos do aplicativo
3. `AndroidManifest.xml` — apenas cite que existe, **não aprofunde**

### ⚠️ Sobre o código do slide 16

O slide mostra a `MainActivity` inteira com `Text("Olá, Mobile!")` dentro do
`setContent`. **Aquele trecho não compila se colado por cima do template** —
faltam os imports de `Text` e do Compose.

Avise a turma: *"esse slide é ilustrativo, não copiem"*. A alteração correta é
localizar a função `Greeting` gerada pelo template e mudar só o texto:

```kotlin
@Composable
fun Greeting(name: String, modifier: Modifier = Modifier) {
    Text(
        text = "Olá, $name!",   // era "Hello $name!"
        modifier = modifier
    )
}
```

### Ordem de execução preferida

1. Emulador já configurado
2. Celular físico já autorizado
3. **Compose Preview** — se a execução demorar, use isto e siga a aula

## Parte B — Aplicativo híbrido (~30 min)

Pasta: [expo-ola-mobile/](expo-ola-mobile/) — contém só o `App.js`.

### ⚠️ Correção necessária ao slide 17

O slide manda `npx create-expo-app@latest` **sem template**. Isso gera um projeto
com `expo-router` e pasta `app/` — o aluno abre o VS Code e **não encontra o
`App.js`** que aparece no slide ao lado.

Use sempre:

```bash
npx create-expo-app@latest PrimeiroAppHibrido --template blank
cd PrimeiroAppHibrido
npx expo start
```

Depois substitua o `App.js` gerado pelo desta pasta.

### O que mostrar — só três coisas

1. `App.js` — onde a tela é escrita
2. `package.json` — dependências do projeto
3. `node_modules` — **apenas diga que existe**, não abra

### Para rodar no navegador (sem emulador)

Se o laboratório não tiver emulador nem celular, o Expo roda no navegador:

```bash
npx expo install react-dom react-native-web @expo/metro-runtime
npx expo start --web
```

Isso abre em `http://localhost:8081` e resolve a Parte B sem nenhum Android.

## Comparação final (~15 min)

Construa a tabela **com a turma**, no quadro:

| Pergunta | Nativo Android | React Native / Expo |
|---|---|---|
| Ferramenta principal | Android Studio | VS Code + terminal |
| Linguagem observada | Kotlin | JavaScript |
| Plataforma inicial | Android | multiplataforma |
| Estrutura | projeto Android | projeto Node/React Native |
| Código compartilhável | focado em Android | pode atender mais de uma plataforma |
| **Tempo até a primeira tela** | **minutos (Gradle)** | **segundos** |

A última linha não está no slide, mas é a que os alunos vão **sentir** na pele
durante a aula. Vale nomear o que eles acabaram de viver.

### Pergunta de fechamento

> "Se o resultado visual é parecido, onde está a diferença?"

Direcione para: linguagem, ferramentas, estrutura, integração com a plataforma,
reaproveitamento e manutenção.

> "Hoje vocês não aprenderam Kotlin nem React Native de verdade — e isso foi
> proposital. Vocês tiveram o primeiro contato com os dois caminhos."
