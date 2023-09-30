import random
import string
import json

from palabras import palabras
from words import words
from ahorcado_diagramas import vidas_diccionario_visual
from hangman_diagrams import lives_dictionary_visual


def obtener_palabra_válida(palabras):
    palabra = random.choice(palabras)

    while '-' in palabra or ' ' in palabra:
        palabra = random.choice(palabras)

    return palabra.upper()

def get_valid_word(words):
    word = random.choice(words)

    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word.upper()

name_file_json = "traducciones.json"


def traducir(word):
    # Verificar si el archivo JSON existe
    try:
        with open(name_file_json, "r", encoding="utf-8") as file:
            traducciones = json.load(file)
    except FileNotFoundError:
        print(f"No se encontró el archivo JSON: {name_file_json}")
        traducciones = {}

    # Verificar si la palabra está en el archivo de traducciones
    if word in traducciones:
        return traducciones[word]
    else:
        return "Traducción no encontrada"



def ahorcado_IE():
    while True:
        Esp_Ing = input('Escoge una letra: "I" para versión en Ingles o "E" para versión en Español: ')
        print()

        if Esp_Ing == "E" or Esp_Ing == "e":
            print("======================================================")
            print(" ¡Hola amigo(a) bienvenido(a) al juego del Ahorcado! ")
            print("======================================================")
            print()
            palabra = obtener_palabra_válida(palabras)
            letras_por_adivinar = set(palabra)
            abecedario = set(string.ascii_uppercase)
            letras_adivinadas = set()
            vidas = 7

            while len(letras_por_adivinar) > 0 and vidas > 0:
                print(f"Te quedan {vidas} vidas y has usado estas letras: {' '.join(letras_adivinadas)}")
                print()

                palabra_lista = [letra if letra in letras_adivinadas else '-' for letra in palabra]
                print(vidas_diccionario_visual[vidas])
                print(f"Palabra: {' '.join(palabra_lista)}")

                letra_usuario = input('Escoge una letra: ').upper()

                if letra_usuario.isalpha():  
                    if letra_usuario in abecedario - letras_adivinadas:
                        letras_adivinadas.add(letra_usuario)
                        if letra_usuario in letras_por_adivinar:
                            letras_por_adivinar.remove(letra_usuario)
                            print('')
                        else:
                            vidas = vidas - 1
                            print(f"\nTu letra, {letra_usuario} no está en la palabra.")
                    elif letra_usuario in letras_adivinadas:
                        print("\nYa escogiste esa letra. Por favor escoge una letra nueva.")
                    else:
                        print("\nEsta letra no es válida.")
                else:
                    print("\nLetra no válida. Por favor, ingresa una letra del alfabeto.")
 
            if vidas == 0:
                print(vidas_diccionario_visual[vidas])
                print(f"¡Ahorcado! Perdiste. Lo lamento mucho. La palabra era: {palabra}")
            else:
                print(f'¡Excelente! ¡Adivinaste la palabra: {palabra}!')
            break

        elif Esp_Ing == "I" or Esp_Ing == "i":
            print("=========================================")
            print(" ¡Hello, welcome to the Hangman game! ")
            print("=========================================")
            print()

            word = get_valid_word(words)
            word_to_guess = set(word)
            alphabet = set(string.ascii_uppercase)
            guessed_letters = set()

            lives = 7

            while len(word_to_guess) > 0 and lives > 0:
                print(f"You have {lives} lives left and have used these letters: {' '.join(guessed_letters)}")

                word_list = []
                for letter in word:
                    if letter in guessed_letters:
                        word_list.append(letter)
                    else:
                        word_list.append('-')

                print(lives_dictionary_visual[lives])
                print(f"Word: {' '.join(word_list)}")

                letter_user = input('Choose a letter: ').upper()

                if letter_user.isalpha(): 
                    if letter_user in alphabet - guessed_letters:
                        guessed_letters.add(letter_user)
                        if letter_user in word_to_guess:
                            word_to_guess.remove(letter_user)
                            print('')
                        else:
                            lives = lives - 1
                            print(f"\nYour letter, {letter_user} is not in the word.")
                    elif letter_user in guessed_letters:
                        print("\nYou've already chosen that letter. Please choose a new letter.")
                    else:
                        print("\nThis letter is not valid.")
                else:
                    print("\nInvalid input. Please enter a letter of the alphabet.")
                
                              
            traduccion = traducir(word)
            if lives == 0:
                print(lives_dictionary_visual[lives])
                print(f"¡Hangman! You lost. I'm so sorry. The word was: {word}")
                print(f"¡La traducción de la palabra {word} es: {traduccion}!")
                 
            else:
                print(f"¡Excellent! You guessed the word {word}!")
                print(f"¡La traducción de la palabra {word} es: {traduccion}!")

            
            break

        else:
            print('¡Debes ingresar la letra correcta!')

if __name__ == '__main__':
    ahorcado_IE()