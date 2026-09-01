# Desenvolvimento Mobile — Curso Técnico em Informática

Material de aula do professor **Emanuel Nascente**.

## Aulas

| Aula | Tema | Material |
|---|---|---|
| **01** | Introdução: Web × Mobile, Nativo × Híbrido | [aula-01/](aula-01/) |

## Exemplos de referência

Aplicações completas usadas como demonstração ou base para aulas futuras.
**Não são material da aula 01** — a aula 01 usa o "Olá, Mobile!", bem mais
simples, para manter o foco no processo e não no código.

| Exemplo | Stack | Pasta |
|---|---|---|
| Lista de Tarefas | React Native + Expo | [exemplos/lista-tarefas-expo/](exemplos/lista-tarefas-expo/) |
| Lista de Tarefas | Kotlin + Jetpack Compose | [exemplos/lista-tarefas-nativo/](exemplos/lista-tarefas-nativo/) |

As duas implementam **a mesma aplicação** nas duas abordagens, com paralelo
quase linha a linha (`useState` ↔ `remember { mutableStateOf }`, `FlatList` ↔
`LazyColumn`). Servem bem para as aulas de estado, listas e eventos.

## Ambiente desta máquina

Levantado em 31/08/2026.

**Instalado:** Node.js 22.23.1, npm 10.9.8, Git 2.47, JDK Zulu 17.0.14,
VS Code, Python 3.10, WSL2 Ubuntu.

**Android SDK** em `C:\dev\android-sdk` (sem Android Studio):

- `platforms/android-35` e `android-36`
- `build-tools/36.0.0`
- `platform-tools` (adb)
- `emulator` 37.1.11 + imagem `android-35;default;x86_64`
- AVD **`aula`** configurado para máquina modesta

**Hardware:** i5-5200U (2 núcleos, 2014), 7,9 GB de RAM. O emulador funciona,
mas é lento — o AVD foi ajustado para 1536 MB de RAM, 720×1280 e GPU em modo
`host`.

## Comandos úteis

```powershell
# Variáveis do Android SDK (uma vez só)
[Environment]::SetEnvironmentVariable('ANDROID_HOME','C:\dev\android-sdk','User')

# Subir o emulador
C:\dev\android-sdk\emulator\emulator.exe -avd aula -no-boot-anim -gpu host

# Liberar a porta 8081 quando o Metro do Expo trava
Get-NetTCPConnection -LocalPort 8081 -State Listen | ForEach-Object { Stop-Process -Id $_.OwningProcess -Force }
```
