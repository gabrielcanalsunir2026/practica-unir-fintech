"""
License: Apache
Organization: UNIR
"""

import os
import sys

DEFAULT_FILENAME = "words.txt"
DEFAULT_DUPLICATES = False


def sort_list(items, ascending=True):
    if not isinstance(items, list):
        raise RuntimeError(f"No puede ordenar {type(items)}")

    return sorted(items, reverse=(not ascending))


def remove_duplicates_from_list(items):
    return list(set(items))


def get_word_stats(word_list):
    """
    Calcula estadísticas básicas de la lista de palabras.
    """
    if not word_list:
        return {
            "total_words": 0,
            "unique_words": 0,
            "average_length": 0.0,
            "longest_word": "",
            "shortest_word": ""
        }
    
    total_words = len(word_list)
    unique_words = len(set(word_list))
    lengths = [len(word) for word in word_list]
    avg_length = sum(lengths) / total_words
    longest_word = max(word_list, key=len)
    shortest_word = min(word_list, key=len)
    
    return {
        "total_words": total_words,
        "unique_words": unique_words,
        "average_length": round(avg_length, 2),
        "longest_word": longest_word,
        "shortest_word": shortest_word
    }


if __name__ == "__main__":
    filename = DEFAULT_FILENAME
    remove_duplicates = DEFAULT_DUPLICATES
    if len(sys.argv) == 3:
        filename = sys.argv[1]
        remove_duplicates = sys.argv[2].lower() == "yes"
    else:
        print("Se debe indicar el fichero como primer argumento")
        print("El segundo argumento indica si se quieren eliminar duplicados")
        sys.exit(1)

    print(f"Se leerán las palabras del fichero {filename}")
    file_path = os.path.join(".", filename)
    if os.path.isfile(file_path):
        word_list = []
        with open(file_path, "r") as file:
            for line in file:
                word_list.append(line.strip())
    else:
        print(f"El fichero {filename} no existe")
        word_list = ["ravenclaw", "gryffindor", "slytherin", "hufflepuff"]

    if remove_duplicates:
        word_list = remove_duplicates_from_list(word_list)

    sorted_words = sort_list(word_list)
    print(sorted_words)

    # Nueva feature: Estadísticas de palabras
    stats = get_word_stats(word_list)
    print("\nEstadísticas de palabras:")
    print(f"Total de palabras: {stats['total_words']}")
    print(f"Palabras únicas: {stats['unique_words']}")
    print(f"Longitud promedio: {stats['average_length']}")
    print(f"Palabra más larga: {stats['longest_word']}")
    print(f"Palabra más corta: {stats['shortest_word']}")

