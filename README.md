# JuegoAhorcadoIE
Este es un código de Python que implementa el juego del ahorcado con dos opciones de idioma: inglés (I) y español (E). 
Se importan las librerías random y string para generar palabras aleatorias y trabajar con cadenas.
Se importa el módulo json para manejar archivos JSON.
Se importan cuatro módulos personalizados: palabras, words, ahorcado_diagramas, y hangman_diagrams. Estos módulos parecen contener datos y diagramas relacionados con el juego.

**Definición de Funciones:**


obtener_palabra_válida(palabras): Esta función elige aleatoriamente una palabra del conjunto palabras y se asegura de que no contenga guiones o espacios. Luego, devuelve la palabra en mayúsculas.
get_valid_word(words): Similar a la función anterior, pero trabaja con el conjunto words.
traducir(word): Busca la traducción de la palabra word en un archivo JSON llamado traducciones.json. Si la palabra está en el archivo, devuelve la traducción; de lo contrario, devuelve "Traducción no encontrada".

**Función Principal: ahorcado_IE():**

Se utiliza un bucle while True para permitir al usuario jugar más de una vez.
El usuario elige la versión del juego, ya sea en inglés (I) o español (E).
Si se selecciona la versión en español, se inicia el juego en español. Si se selecciona la versión en inglés, se inicia el juego en inglés.
En ambos casos, se inicializan variables y estructuras de datos para el juego, como las letras por adivinar, el abecedario, las letras adivinadas y las vidas.
Se ejecutan bucles para permitir al usuario adivinar letras y se proporciona retroalimentación en función de las letras adivinadas y las vidas restantes.
Al final del juego, se muestra si el usuario ganó o perdió y se muestra la palabra correcta junto con su posible traducción si se encuentra en el archivo JSON.



