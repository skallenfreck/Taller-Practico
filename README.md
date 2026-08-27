# Taller-Practico

# Paso 1. Crear un entorno virtual

Abrir la terminal dentro de la carpeta del proyecto y ejecutar:

python -m venv venv


Activar el entorno virtual:

venv\Scripts\activate

---

# Paso 2. Instalar las librerías necesarias

Con el entorno virtual activado, instalar las dependencias:

pip install google-genai python-dotenv

También se puede verificar que quedaron instaladas con:

pip list

Deberán aparecer, entre otras:

google-genai
python-dotenv

# Paso 3. Configurar la API Key

Dentro de la carpeta del proyecto crear un archivo llamado:

.env

En su interior escribir la API Key:

GEMINI_API_KEY=TU_API_KEY_AQUI

# Ejercicio 1 – Conexión y petición básica

## Cómo ejecutarlo

Desde la terminal, ubicarse en la carpeta del proyecto y ejecutar:

python ejercicio1.py

## ¿Qué hace este ejercicio?

1. Carga la API Key desde el archivo `.env`.
2. Inicializa el cliente de Gemini.
3. Envía una consulta al modelo.
4. Solicita una explicación sobre **Inferencia en Inteligencia Artificial** en menos de 50 palabras.
5. Muestra la respuesta generada por Gemini.

<img width="1600" height="858" alt="image" src="https://github.com/user-attachments/assets/6b553c63-0f12-45f5-8844-50d24c1bf6dc" />


# Ejercicio 2 – Procesador de textos inteligente

## Cómo ejecutarlo

python ejercicio2.py

## ¿Qué hace este ejercicio?

1. Carga la API Key.
2. Inicializa Gemini.
3. Define una **System Instruction**, donde la IA actúa como un **Editor Editorial de prestigio**.
4. Analiza el texto recibido.
5. Ejecuta la tarea seleccionada.
6. Devuelve el texto procesado.

<img width="1600" height="853" alt="image" src="https://github.com/user-attachments/assets/e7ef44b4-f515-4f7f-83e8-0464d060221d" />
<img width="1600" height="853" alt="image" src="https://github.com/user-attachments/assets/401aff3a-4e3c-4916-be48-b39f22b2954c" />
<img width="1600" height="857" alt="image" src="https://github.com/user-attachments/assets/4b07167d-a557-4d29-8aeb-88dca1f6591f" />



# Ejercicio 3 – Chat de soporte con historial (Few-Shot)

## Cómo ejecutarlo

python ejercicio3.py

Al iniciar aparecerá un mensaje similar a:

======================================
   SOPORTE - TIENDA DE TECNOLOGÍA
======================================

Escribe 'finalizar' para terminar.

Ahora el usuario puede realizar preguntas como:

Cliente: ¿Qué portátil tienen para estudiar?

Cliente: ¿Cuánta memoria RAM tiene?

Cliente: ¿Tiene almacenamiento SSD?

Cliente: finalizar

## ¿Qué hace este ejercicio?

El programa realiza las siguientes acciones:

1. Carga la API Key.
2. Inicializa el cliente de Gemini.
3. Define el rol de la IA como **vendedor amable y profesional**.
4. Carga un historial con ejemplos de conversación (Few-Shot).
5. Inicia un chat interactivo.
6. Mantiene el contexto entre preguntas.
7. Finaliza únicamente cuando el usuario escribe **finalizar**.

<img width="1600" height="861" alt="image" src="https://github.com/user-attachments/assets/8ee79ec4-8606-491e-9a15-793cf574d8f7" />
<img width="1600" height="851" alt="image" src="https://github.com/user-attachments/assets/84c8f3fe-a6e3-48c8-ac89-3e1783403015" />


