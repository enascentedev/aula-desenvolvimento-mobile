# Análise: apresentação × roteiro

Revisão dos 20 slides de `Aula_01_Desenvolvimento_Mobile.pptx` contra o roteiro,
feita em 31/08/2026, com verificação prática dos comandos numa máquina real.

## Resumo

A apresentação está boa e o roteiro é sólido — ele **já corrige de própria conta**
os dois problemas técnicos reais dos slides. O que segue são ajustes pontuais e
um risco que o roteiro subestima.

---

## 🔴 Divergências entre slide e realidade

### Slide 17 — comando do Expo incompleto

**No slide:**
```bash
npx create-expo-app@latest
```

**Problema confirmado na prática:** sem `--template blank`, o Expo gera um projeto
com `expo-router` e pasta `app/`. O aluno abre o VS Code procurando o `App.js`
que está impresso no próprio slide, ao lado, e **não encontra**.

**Correção (já prevista no roteiro):**
```bash
npx create-expo-app@latest PrimeiroAppHibrido --template blank
```

Verificado: com `--template blank`, o projeto gerado tem `App.js` na raiz,
exatamente como o slide mostra.

### Slide 16 — o Kotlin do slide não compila

**No slide:**
```kotlin
class MainActivity : ComponentActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContent {
            Text("Olá, Mobile!")
        }
    }
}
```

**Problema:** faltam os imports de `Text`, `setContent` e do Compose. Um aluno
que colar isso por cima do template gerado recebe erro de compilação.

**O roteiro já acerta** ao mandar alterar apenas o texto dentro de `Greeting`.
A tensão é que o slide projetado na parede sugere outra coisa.

**Ação em aula:** diga explicitamente *"esse slide é ilustrativo, não copiem"*.

---

## 🟡 Risco subestimado: o tempo do Gradle

O gatilho de Plano B no roteiro é sobre **instalação** — "não use a primeira aula
para instalar Android Studio em 25 máquinas". Correto, mas há um segundo gargalo.

**Medição real nesta máquina, com SDK já instalado:**

```
BUILD SUCCESSFUL in 15m 1s
37 actionable tasks: 37 executed
```

Quinze minutos. Não para instalar nada — só para o Gradle baixar ~1,1 GB de
dependências AndroidX e compilar um projeto Compose vazio pela primeira vez.

Em 25 máquinas simultâneas, disputando a mesma banda, os 35 minutos da Parte A
podem se tornar insuficientes.

**Sugestão:** acrescentar ao health check a verificação do cache do Gradle:

```powershell
dir $env:USERPROFILE\.gradle\caches
```

Vazio na maioria das máquinas → Plano B.

---

## 🟢 Divergências menores

| Item | PPTX | Roteiro | Observação |
|---|---|---|---|
| Tempo de apresentação dos alunos | 25 min (25 × 1 min) | ~30 min | O roteiro é mais realista; alunos passam do minuto |
| Checklist (slide 15) | lista Android Studio como requisito | idem | Tecnicamente dispensável (dá para compilar por CLI), mas para 25 máquinas o Studio é mais prático |

---

## ✅ Pontos fortes que valem preservar

1. **Slide 6 ("um site aberto no celular é um app mobile?")** é uma excelente
   abertura — separa dispositivo de arquitetura sem virar pegadinha.

2. **A seção 8 do roteiro** ("pontos conceituais que o professor deve proteger")
   é o melhor pedaço do documento. Os 8 itens evitam exatamente os vícios que
   alunos de técnico levam para a vida ("nativo é sempre mais rápido").

3. **O Plano B não é plano de contingência disfarçado.** Ele pratica a decisão
   técnica, que é a mensagem central da aula. Em alguns aspectos cumpre o
   objetivo do encontro melhor que o laboratório.

4. **A mudança de requisito na dinâmica** é o melhor recurso pedagógico do
   roteiro inteiro. Mostra que decisão técnica não é permanente.

---

## Sugestão de ajuste no slide 18

A tabela comparativa do slide 18 lista ferramenta, linguagem, estrutura. Falta a
linha que os alunos vão **sentir** durante a aula:

| Pergunta | Nativo Android | React Native / Expo |
|---|---|---|
| **Tempo até a primeira tela** | **minutos (Gradle)** | **segundos** |

Nomear essa diferença logo depois que eles a viveram é mais eficaz que qualquer
explicação teórica sobre ciclo de build.

---

## Verificações feitas

| O quê | Resultado |
|---|---|
| `npx create-expo-app --template blank` | ✅ gera `App.js` na raiz |
| Build Compose do zero | ✅ compila, 15m 1s |
| APK em emulador | ✅ instala e roda |
| Expo no navegador (`--web`) | ✅ funciona sem nenhum Android |
