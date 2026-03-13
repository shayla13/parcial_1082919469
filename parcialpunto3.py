"""Analizador de texto.

Pide un texto al usuario (no vacío) y calcula varias estadísticas usando
funciones separadas. Muestra los resultados de forma clara y organizada.
"""

import re
from typing import List, Tuple


def contar_caracteres(texto: str) -> int:
    """Devuelve el total de caracteres del texto (incluye espacios)."""
    return len(texto)


def _extraer_palabras(texto: str) -> List[str]:
    """Extrae palabras del texto (letras, incluye acentos y ñ)."""
    # Consideramos secuencias de letras como palabras
    return re.findall(r"[A-Za-zÀ-ÖØ-öø-ÿ]+", texto, flags=re.UNICODE)


def contar_palabras(texto: str) -> int:
    """Devuelve el total de palabras en el texto."""
    palabras = _extraer_palabras(texto)
    return len(palabras)


def contar_oraciones(texto: str) -> int:
    """Cuenta oraciones separadas por '.', '!' o '?'.

    Se ignoran segmentos vacíos resultantes de la división.
    """
    partes = re.split(r'[.!?]+', texto)
    # Contar partes no vacías tras eliminar espacios
    return sum(1 for p in partes if p.strip())


def palabra_mas_larga(texto: str) -> str:
    """Devuelve la palabra más larga; devuelve cadena vacía si no hay palabras."""
    palabras = _extraer_palabras(texto)
    if not palabras:
        return ""
    return max(palabras, key=len)


def palabra_mas_corta(texto: str) -> str:
    """Devuelve la palabra más corta; devuelve cadena vacía si no hay palabras."""
    palabras = _extraer_palabras(texto)
    if not palabras:
        return ""
    return min(palabras, key=len)


def contar_vocales(texto: str) -> int:
    """Cuenta vocales (incluye mayúsculas y vocales acentuadas y 'ü')."""
    vocales = set('aeiouAEIOUáéíóúÁÉÍÓÚüÜ')
    return sum(1 for c in texto if c in vocales)


def contar_consonantes(texto: str) -> int:
    """Cuenta consonantes (letras que no son vocales)."""
    vocales = set('aeiouAEIOUáéíóúÁÉÍÓÚüÜ')
    return sum(1 for c in texto if c.isalpha() and c not in vocales)


def analizar_texto(texto: str) -> Tuple[int, int, int, str, str, int, int]:
    """Usa las funciones auxiliares y devuelve todas las estadísticas.

    Retorna una tupla con:
      (caracteres, palabras, oraciones, palabra_mas_larga, palabra_mas_corta, vocales, consonantes)
    """
    caracteres = contar_caracteres(texto)
    palabras = contar_palabras(texto)
    oraciones = contar_oraciones(texto)
    mas_larga = palabra_mas_larga(texto)
    mas_corta = palabra_mas_corta(texto)
    vocales = contar_vocales(texto)
    consonantes = contar_consonantes(texto)
    return caracteres, palabras, oraciones, mas_larga, mas_corta, vocales, consonantes


def main() -> None:
    """Bucle principal: pide texto no vacío y muestra las estadísticas."""
    while True:
        texto = input("Ingrese un texto para analizar: ").strip()
        if texto:
            break
        print("El texto no puede estar vacío. Intente de nuevo.")

    (caracteres, palabras, oraciones,
     mas_larga, mas_corta, vocales, consonantes) = analizar_texto(texto)

    print("\nEstadísticas del texto:\n")
    print(f"- Total de caracteres: {caracteres}")
    print(f"- Total de palabras: {palabras}")
    print(f"- Total de oraciones: {oraciones}")
    print(f"- Palabra más larga: {mas_larga}")
    print(f"- Palabra más corta: {mas_corta}")
    print(f"- Número de vocales: {vocales}")
    print(f"- Número de consonantes: {consonantes}")


if __name__ == '__main__':
    main()
