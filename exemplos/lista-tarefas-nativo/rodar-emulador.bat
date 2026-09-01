@echo off
REM Sobe o emulador, compila a aplicacao e instala.
REM Uso: dar duplo clique, ou rodar no terminal a partir desta pasta.

set ANDROID_HOME=C:\dev\android-sdk
set JAVA_HOME=C:\Java\jdk-17.0.14
set PATH=%PATH%;%ANDROID_HOME%\platform-tools;%ANDROID_HOME%\emulator

echo.
echo [1/4] Iniciando o emulador (deixe esta janela aberta)...
start "Emulador Android" "%ANDROID_HOME%\emulator\emulator.exe" -avd aula -no-boot-anim -gpu host

echo [2/4] Aguardando o Android terminar de iniciar...
adb wait-for-device
:aguarda
for /f "tokens=*" %%i in ('adb shell getprop sys.boot_completed 2^>nul') do set BOOT=%%i
if not "%BOOT%"=="1" (
    timeout /t 3 /nobreak >nul
    goto aguarda
)

echo [3/4] Compilando o APK...
call gradlew.bat assembleDebug
if errorlevel 1 (
    echo.
    echo ERRO na compilacao. Veja as mensagens acima.
    pause
    exit /b 1
)

echo [4/4] Instalando e abrindo...
adb install -r app\build\outputs\apk\debug\app-debug.apk
adb shell monkey -p com.aula.tarefas -c android.intent.category.LAUNCHER 1 >nul 2>&1

echo.
echo Pronto. A aplicacao esta rodando no emulador.
pause
