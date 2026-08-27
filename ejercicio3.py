import os

from dotenv import load_dotenv
from google import genai
from google.genai import types


# Cargar las variables de entorno.
load_dotenv()


def crear_chat(client):
    """
    Crea una conversación de soporte para una tienda de tecnología.
    """

    # Define el comportamiento general del asistente.
    system_instruction = (
        "Actúa como un vendedor amable y profesional de una tienda "
        "de tecnología. Responde de forma clara, cordial y útil. "
        "Cuando el usuario pregunte por un producto, proporciona "
        "sus especificaciones de forma organizada. "
        "No inventes especificaciones que no estén disponibles. "
        "Si no tienes información suficiente, indícalo claramente."
    )

    # Historial utilizado como ejemplos Few-Shot.
    history = [
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(
                    text=(
                        "¿Qué características tiene el portátil "
                        "TechBook Pro 14?"
                    )
                )
            ],
        ),
        types.Content(
            role="model",
            parts=[
                types.Part.from_text(
                    text=(
                        "El TechBook Pro 14 cuenta con pantalla de 14 "
                        "pulgadas, procesador Intel Core i7, 16 GB de RAM "
                        "y almacenamiento SSD de 512 GB. Es una opción "
                        "adecuada para trabajo y estudio."
                    )
                )
            ],
        ),
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(
                    text=(
                        "¿Qué especificaciones tiene el teléfono "
                        "SmartTech X1?"
                    )
                )
            ],
        ),
        types.Content(
            role="model",
            parts=[
                types.Part.from_text(
                    text=(
                        "El SmartTech X1 dispone de pantalla de 6,5 "
                        "pulgadas, 8 GB de RAM, 256 GB de almacenamiento "
                        "y conectividad 5G. Es un equipo orientado a "
                        "usuarios que buscan buen rendimiento."
                    )
                )
            ],
        ),
    ]

    # Crear la conversación utilizando el historial inicial.
    chat = client.chats.create(
        model="gemini-3.1-flash-lite",
        config=types.GenerateContentConfig(
            system_instruction=system_instruction
        ),
        history=history,
    )

    return chat


def main():
    """Inicia el sistema interactivo de soporte."""

    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key:
        raise ValueError(
            "No se encontró la variable GEMINI_API_KEY."
        )

    # Inicializar el cliente.
    client = genai.Client(api_key=api_key)

    # Crear el chat con su rol e historial Few-Shot.
    chat = crear_chat(client)

    print("======================================")
    print("   SOPORTE - TIENDA DE TECNOLOGÍA")
    print("======================================")
    print("Escribe 'finalizar' para terminar.\n")

    while True:
        pregunta = input("Cliente: ").strip()

        # Comprobar si el usuario desea finalizar.
        if pregunta.lower() == "finalizar":
            print("\nVendedor: Gracias por contactarnos. ¡Hasta pronto!")
            break

        # Evitar enviar mensajes vacíos.
        if not pregunta:
            print("Vendedor: Por favor, escribe una pregunta.")
            continue

        # Enviar el mensaje manteniendo el historial del chat.
        response = chat.send_message(pregunta)

        print(f"\nVendedor: {response.text}\n")


if __name__ == "__main__":
    main()