package com.aula.olamobile

import android.os.Bundle
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.Surface
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.tooling.preview.Preview
import androidx.compose.ui.unit.sp

// Aula 01 - Laboratorio, Parte A: aplicativo NATIVO.
//
// O objetivo de hoje NAO e entender cada linha. E reconhecer que:
//   1. a linguagem e Kotlin;
//   2. a interface e declarada com Jetpack Compose;
//   3. o projeto tem uma estrutura propria de Android (Gradle, res, Manifest).
//
// O mesmo "Ola, Mobile!" esta escrito em React Native na pasta expo-ola-mobile.

class MainActivity : ComponentActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContent {
            MaterialTheme {
                Surface(modifier = Modifier.fillMaxSize()) {
                    Saudacao()
                }
            }
        }
    }
}

@Composable
fun Saudacao() {
    Box(
        modifier = Modifier.fillMaxSize(),
        contentAlignment = Alignment.Center
    ) {
        Text(
            text = "Olá, Mobile!",
            fontSize = 28.sp
        )
    }
}

@Preview(showBackground = true)
@Composable
fun PreviewSaudacao() {
    MaterialTheme {
        Saudacao()
    }
}
