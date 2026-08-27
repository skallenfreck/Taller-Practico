import os

from dotenv import load_dotenv
from google import genai


# Cargar las variables definidas en el archivo .env
load_dotenv()


def main():
    """Inicializa Gemini y realiza una consulta básica."""

    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key:
        raise ValueError(
            "No se encontró la variable GEMINI_API_KEY."
        )

    # Crear el cliente de Gemini utilizando la API Key.
    client = genai.Client(api_key=api_key)

    # Consulta solicitada para el ejercicio.
    prompt = (
        "Explica qué es la Inferencia en Inteligencia Artificial "
        "en menos de 50 palabras."
    )

    # Enviar la petición al modelo.
    response = client.models.generate_content(
        model="gemini-3.1-flash-lite",
        contents=prompt
    )

    # Mostrar la respuesta generada.
    print("\nRespuesta de Gemini:")
    print(response.text)


if __name__ == "__main__":
    main()