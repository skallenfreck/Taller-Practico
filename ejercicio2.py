import os

from dotenv import load_dotenv
from google import genai


# Cargar las variables de entorno desde el archivo .env.
load_dotenv()


def procesar_articulo(texto, tarea):
    """
    Procesa un artículo según la tarea seleccionada.

    Parámetros:
        texto (str): Artículo que se desea procesar.
        tarea (str): Puede ser 'resumir' o 'profesionalizar'.

    Retorna:
        str: Resultado generado por Gemini.
    """

    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key:
        raise ValueError(
            "No se encontró la variable GEMINI_API_KEY."
        )

    # Inicializar el cliente de Gemini.
    client = genai.Client(api_key=api_key)

    # Definir el rol que debe asumir la IA.
    system_instruction = (
        "Actúa como un Editor Editorial de prestigio. "
        "Trabaja con precisión, claridad, coherencia y lenguaje "
        "profesional. Conserva las ideas principales del texto "
        "y no inventes información."
    )

    # Normalizar la opción ingresada por el usuario.
    tarea = tarea.lower().strip()

    if tarea == "resumir":
        prompt = (
            "Elabora un resumen ejecutivo del siguiente artículo. "
            "Identifica las ideas principales y los aspectos más "
            "importantes de forma clara y concisa.\n\n"
            f"ARTÍCULO:\n{texto}"
        )

    elif tarea == "profesionalizar":
        prompt = (
            "Edita el siguiente artículo para que tenga un tono "
            "formal, técnico y profesional. Mejora la redacción, "
            "claridad y coherencia sin cambiar su significado.\n\n"
            f"ARTÍCULO:\n{texto}"
        )

    else:
        raise ValueError(
            "La tarea seleccionada no es válida."
        )

    # Enviar la solicitud al modelo utilizando la system_instruction.
    response = client.models.generate_content(
        model="gemini-3.1-flash-lite",
        contents=prompt,
        config={
            "system_instruction": system_instruction
        }
    )

    return response.text


def main():
    """Permite al usuario seleccionar la tarea desde la consola."""

    print("=" * 50)
    print("       PROCESADOR DE TEXTOS INTELIGENTE")
    print("=" * 50)

    # Solicitar el artículo al usuario.
    print("\nIngrese el artículo que desea procesar.")
    print("Cuando termine, presione ENTER dos veces.\n")

    lineas = []

    while True:
        linea = input()

        if linea == "":
            break

        lineas.append(linea)

    texto = "\n".join(lineas)

    # Validar que se haya ingresado contenido.
    if not texto.strip():
        print("\nError: debe ingresar un artículo.")
        return

    # Mostrar las opciones disponibles.
    print("\nSeleccione la tarea que desea realizar:")
    print("1. Resumir")
    print("2. Profesionalizar")

    opcion = input("\nOpción: ").strip()

    # Convertir la opción numérica al nombre de la tarea.
    if opcion == "1":
        tarea = "resumir"
    elif opcion == "2":
        tarea = "profesionalizar"
    else:
        print("\nError: opción no válida.")
        return

    print("\nProcesando el artículo con Gemini...")
    
    try:
        resultado = procesar_articulo(texto, tarea)

        print("\n" + "=" * 50)
        print("RESULTADO")
        print("=" * 50)
        print(resultado)

    except Exception as error:
        print(f"\nOcurrió un error: {error}")


if __name__ == "__main__":
    main()