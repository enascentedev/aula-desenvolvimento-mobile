// Build script raiz. Declara os plugins e suas versoes, sem aplica-los aqui
// (o modulo :app e quem aplica).
//
// Versoes escolhidas para casar com o SDK ja instalado em C:\dev\android-sdk
// (platforms android-36, build-tools 36.0.0):
//   - AGP 8.13.0  -> suporta ate API 36.1
//   - Kotlin 2.2.0 -> o plugin do Compose acompanha a versao do Kotlin
//
// Atencao: Compose 1.12+ (BOM 2026.08.00) exige compileSdk 37 e AGP 9.
// Por isso este projeto usa a BOM 2026.03.01, da linha compativel com AGP 8.

plugins {
    id("com.android.application") version "8.13.0" apply false
    id("org.jetbrains.kotlin.android") version "2.2.0" apply false
    id("org.jetbrains.kotlin.plugin.compose") version "2.2.0" apply false
}
