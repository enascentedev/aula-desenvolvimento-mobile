import { StyleSheet, Text, View } from 'react-native';

// Aula 01 - Laboratorio, Parte B: aplicativo HIBRIDO / MULTIPLATAFORMA.
//
// O objetivo de hoje NAO e entender cada linha. E reconhecer que:
//   1. a linguagem e JavaScript;
//   2. a tela e montada com componentes (View, Text);
//   3. nao existe Android Studio neste caminho - so VS Code e terminal.
//
// O mesmo "Ola, Mobile!" esta escrito em Kotlin na pasta nativo-ola-mobile.

export default function App() {
  return (
    <View style={styles.container}>
      <Text style={styles.texto}>Olá, Mobile!</Text>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    alignItems: 'center',
    justifyContent: 'center',
  },
  texto: {
    fontSize: 28,
  },
});
