import React, { useState } from 'react';
import {
  SafeAreaView,
  View,
  Text,
  TextInput,
  FlatList,
  Pressable,
  StyleSheet,
  StatusBar,
  Platform,
} from 'react-native';

// Lista de Tarefas - versao React Native + Expo
// A MESMA aplicacao esta implementada em Kotlin nativo na pasta 02-android-nativo,
// para os alunos compararem as duas abordagens lado a lado.

export default function App() {
  // useState guarda o estado da tela. Quando muda, o React redesenha a interface.
  const [texto, setTexto] = useState('');
  const [tarefas, setTarefas] = useState([
    { id: '1', titulo: 'Abrir o Snack no navegador', feita: true },
    { id: '2', titulo: 'Escrever meu primeiro componente', feita: false },
  ]);

  function adicionar() {
    const titulo = texto.trim();
    if (titulo.length === 0) return; // ignora entrada vazia

    setTarefas((atual) => [
      ...atual,
      { id: String(Date.now()), titulo, feita: false },
    ]);
    setTexto('');
  }

  function alternar(id) {
    setTarefas((atual) =>
      atual.map((t) => (t.id === id ? { ...t, feita: !t.feita } : t))
    );
  }

  function remover(id) {
    setTarefas((atual) => atual.filter((t) => t.id !== id));
  }

  const pendentes = tarefas.filter((t) => !t.feita).length;

  return (
    <SafeAreaView style={styles.tela}>
      <StatusBar barStyle="light-content" />

      <View style={styles.cabecalho}>
        <Text style={styles.titulo}>Minhas Tarefas</Text>
        <Text style={styles.subtitulo}>
          {pendentes === 0
            ? 'Tudo em dia!'
            : `${pendentes} pendente${pendentes > 1 ? 's' : ''}`}
        </Text>
      </View>

      <View style={styles.linhaEntrada}>
        <TextInput
          style={styles.input}
          placeholder="O que precisa ser feito?"
          placeholderTextColor="#9aa0a6"
          value={texto}
          onChangeText={setTexto}
          onSubmitEditing={adicionar}
          returnKeyType="done"
        />
        <Pressable
          style={({ pressed }) => [styles.botao, pressed && styles.botaoPressionado]}
          onPress={adicionar}
        >
          <Text style={styles.botaoTexto}>+</Text>
        </Pressable>
      </View>

      <FlatList
        data={tarefas}
        keyExtractor={(item) => item.id}
        contentContainerStyle={styles.lista}
        ListEmptyComponent={
          <Text style={styles.vazio}>Nenhuma tarefa ainda. Adicione a primeira!</Text>
        }
        renderItem={({ item }) => (
          <Pressable style={styles.item} onPress={() => alternar(item.id)}>
            <View style={[styles.caixa, item.feita && styles.caixaMarcada]}>
              {item.feita && <Text style={styles.check}>✓</Text>}
            </View>

            <Text style={[styles.itemTexto, item.feita && styles.itemTextoFeito]}>
              {item.titulo}
            </Text>

            <Pressable onPress={() => remover(item.id)} hitSlop={12}>
              <Text style={styles.remover}>✕</Text>
            </Pressable>
          </Pressable>
        )}
      />
    </SafeAreaView>
  );
}

const styles = StyleSheet.create({
  tela: {
    flex: 1,
    backgroundColor: '#0f1115',
    paddingTop: Platform.OS === 'android' ? 28 : 0,
  },
  cabecalho: {
    paddingHorizontal: 20,
    paddingTop: 20,
    paddingBottom: 12,
  },
  titulo: {
    fontSize: 28,
    fontWeight: '700',
    color: '#ffffff',
  },
  subtitulo: {
    fontSize: 14,
    color: '#9aa0a6',
    marginTop: 4,
  },
  linhaEntrada: {
    flexDirection: 'row',
    paddingHorizontal: 20,
    gap: 10,
    marginBottom: 16,
  },
  input: {
    flex: 1,
    backgroundColor: '#1b1f27',
    borderRadius: 12,
    paddingHorizontal: 16,
    paddingVertical: 12,
    fontSize: 16,
    color: '#ffffff',
  },
  botao: {
    width: 48,
    borderRadius: 12,
    backgroundColor: '#4c8dff',
    alignItems: 'center',
    justifyContent: 'center',
  },
  botaoPressionado: {
    opacity: 0.7,
  },
  botaoTexto: {
    color: '#ffffff',
    fontSize: 26,
    lineHeight: 30,
    fontWeight: '600',
  },
  lista: {
    paddingHorizontal: 20,
    paddingBottom: 40,
  },
  item: {
    flexDirection: 'row',
    alignItems: 'center',
    backgroundColor: '#1b1f27',
    borderRadius: 12,
    padding: 14,
    marginBottom: 10,
    gap: 12,
  },
  caixa: {
    width: 24,
    height: 24,
    borderRadius: 6,
    borderWidth: 2,
    borderColor: '#4c8dff',
    alignItems: 'center',
    justifyContent: 'center',
  },
  caixaMarcada: {
    backgroundColor: '#4c8dff',
  },
  check: {
    color: '#ffffff',
    fontSize: 14,
    fontWeight: '700',
  },
  itemTexto: {
    flex: 1,
    fontSize: 16,
    color: '#e8eaed',
  },
  itemTextoFeito: {
    textDecorationLine: 'line-through',
    color: '#5f6672',
  },
  remover: {
    color: '#5f6672',
    fontSize: 16,
    paddingHorizontal: 4,
  },
  vazio: {
    textAlign: 'center',
    color: '#5f6672',
    marginTop: 40,
    fontSize: 15,
  },
});
