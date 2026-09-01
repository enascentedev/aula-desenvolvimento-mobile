package com.aula.tarefas

import android.os.Bundle
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.compose.foundation.background
import androidx.compose.foundation.border
import androidx.compose.foundation.clickable
import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.layout.size
import androidx.compose.foundation.layout.systemBarsPadding
import androidx.compose.foundation.lazy.LazyColumn
import androidx.compose.foundation.lazy.items
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.foundation.text.KeyboardActions
import androidx.compose.foundation.text.KeyboardOptions
import androidx.compose.material3.Button
import androidx.compose.material3.ButtonDefaults
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.OutlinedTextField
import androidx.compose.material3.OutlinedTextFieldDefaults
import androidx.compose.material3.Surface
import androidx.compose.material3.Text
import androidx.compose.material3.darkColorScheme
import androidx.compose.runtime.Composable
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.remember
import androidx.compose.runtime.setValue
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.text.input.ImeAction
import androidx.compose.ui.text.style.TextDecoration
import androidx.compose.ui.tooling.preview.Preview
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp

// Lista de Tarefas - versao Android nativo (Kotlin + Jetpack Compose)
// A MESMA aplicacao esta em React Native na pasta 01-react-native-expo.
//
// Repare que Compose e React Native seguem a mesma ideia: a interface e uma
// funcao do estado. Quando o estado muda, a tela e redesenhada sozinha.
//   React Native:  useState(...)          ->  Compose: remember { mutableStateOf(...) }
//   React Native:  FlatList               ->  Compose: LazyColumn
//   React Native:  StyleSheet.create      ->  Compose: Modifier encadeado

private val Fundo = Color(0xFF0F1115)
private val Cartao = Color(0xFF1B1F27)
private val Destaque = Color(0xFF4C8DFF)
private val TextoClaro = Color(0xFFE8EAED)
private val TextoApagado = Color(0xFF9AA0A6)
private val TextoRiscado = Color(0xFF5F6672)

data class Tarefa(
    val id: Long,
    val titulo: String,
    val feita: Boolean = false
)

class MainActivity : ComponentActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContent {
            MaterialTheme(colorScheme = darkColorScheme()) {
                Surface(modifier = Modifier.fillMaxSize(), color = Fundo) {
                    TelaTarefas()
                }
            }
        }
    }
}

@Composable
fun TelaTarefas() {
    // Equivalente ao useState do React. O 'remember' preserva o valor entre
    // redesenhos; o 'mutableStateOf' avisa o Compose quando o valor muda.
    var texto by remember { mutableStateOf("") }
    var tarefas by remember {
        mutableStateOf(
            listOf(
                Tarefa(1, "Instalar o JDK e o Android SDK", feita = true),
                Tarefa(2, "Compilar meu primeiro APK", feita = false)
            )
        )
    }

    fun adicionar() {
        val titulo = texto.trim()
        if (titulo.isEmpty()) return

        tarefas = tarefas + Tarefa(id = System.currentTimeMillis(), titulo = titulo)
        texto = ""
    }

    fun alternar(id: Long) {
        tarefas = tarefas.map { if (it.id == id) it.copy(feita = !it.feita) else it }
    }

    fun remover(id: Long) {
        tarefas = tarefas.filterNot { it.id == id }
    }

    val pendentes = tarefas.count { !it.feita }

    Column(
        modifier = Modifier
            .fillMaxSize()
            .systemBarsPadding()
            .padding(horizontal = 20.dp)
    ) {
        Text(
            text = "Minhas Tarefas",
            color = Color.White,
            fontSize = 28.sp,
            fontWeight = FontWeight.Bold,
            modifier = Modifier.padding(top = 20.dp)
        )

        Text(
            text = if (pendentes == 0) "Tudo em dia!"
                   else "$pendentes pendente${if (pendentes > 1) "s" else ""}",
            color = TextoApagado,
            fontSize = 14.sp,
            modifier = Modifier.padding(top = 4.dp, bottom = 16.dp)
        )

        Row(
            modifier = Modifier.fillMaxWidth(),
            horizontalArrangement = Arrangement.spacedBy(10.dp),
            verticalAlignment = Alignment.CenterVertically
        ) {
            OutlinedTextField(
                value = texto,
                onValueChange = { texto = it },
                placeholder = { Text("O que precisa ser feito?", color = TextoApagado) },
                singleLine = true,
                shape = RoundedCornerShape(12.dp),
                colors = OutlinedTextFieldDefaults.colors(
                    focusedContainerColor = Cartao,
                    unfocusedContainerColor = Cartao,
                    focusedTextColor = Color.White,
                    unfocusedTextColor = Color.White,
                    focusedBorderColor = Destaque,
                    unfocusedBorderColor = Color.Transparent
                ),
                keyboardOptions = KeyboardOptions(imeAction = ImeAction.Done),
                keyboardActions = KeyboardActions(onDone = { adicionar() }),
                modifier = Modifier.weight(1f)
            )

            Button(
                onClick = { adicionar() },
                shape = RoundedCornerShape(12.dp),
                colors = ButtonDefaults.buttonColors(containerColor = Destaque),
                contentPadding = androidx.compose.foundation.layout.PaddingValues(0.dp),
                modifier = Modifier.size(width = 48.dp, height = 56.dp)
            ) {
                Text("+", fontSize = 24.sp, color = Color.White)
            }
        }

        if (tarefas.isEmpty()) {
            Text(
                text = "Nenhuma tarefa ainda. Adicione a primeira!",
                color = TextoRiscado,
                fontSize = 15.sp,
                modifier = Modifier
                    .fillMaxWidth()
                    .padding(top = 40.dp)
            )
        } else {
            LazyColumn(
                verticalArrangement = Arrangement.spacedBy(10.dp),
                modifier = Modifier.padding(top = 16.dp)
            ) {
                items(items = tarefas, key = { it.id }) { tarefa ->
                    ItemTarefa(
                        tarefa = tarefa,
                        aoClicar = { alternar(tarefa.id) },
                        aoRemover = { remover(tarefa.id) }
                    )
                }
            }
        }
    }
}

@Composable
fun ItemTarefa(tarefa: Tarefa, aoClicar: () -> Unit, aoRemover: () -> Unit) {
    Row(
        verticalAlignment = Alignment.CenterVertically,
        horizontalArrangement = Arrangement.spacedBy(12.dp),
        modifier = Modifier
            .fillMaxWidth()
            .background(Cartao, RoundedCornerShape(12.dp))
            .clickable { aoClicar() }
            .padding(14.dp)
    ) {
        // Caixa de marcacao desenhada na mao, para nao depender de icones extras.
        Box(
            contentAlignment = Alignment.Center,
            modifier = Modifier
                .size(24.dp)
                .background(
                    color = if (tarefa.feita) Destaque else Color.Transparent,
                    shape = RoundedCornerShape(6.dp)
                )
                .border(2.dp, Destaque, RoundedCornerShape(6.dp))
        ) {
            if (tarefa.feita) {
                Text("✓", color = Color.White, fontSize = 14.sp, fontWeight = FontWeight.Bold)
            }
        }

        Text(
            text = tarefa.titulo,
            color = if (tarefa.feita) TextoRiscado else TextoClaro,
            fontSize = 16.sp,
            textDecoration = if (tarefa.feita) TextDecoration.LineThrough else null,
            modifier = Modifier.weight(1f)
        )

        Text(
            text = "✕",
            color = TextoRiscado,
            fontSize = 16.sp,
            modifier = Modifier
                .clickable { aoRemover() }
                .padding(horizontal = 4.dp)
        )
    }
}

@Preview(showBackground = true, backgroundColor = 0xFF0F1115)
@Composable
fun PreviewTelaTarefas() {
    MaterialTheme(colorScheme = darkColorScheme()) {
        Surface(color = Fundo) {
            TelaTarefas()
        }
    }
}
