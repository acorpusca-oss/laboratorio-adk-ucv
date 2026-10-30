
from google.adk.agents.llm_agent import Agent
from google.adk.models.google_llm import Gemini
from google.genai import types

def calcular_promedio(notas: list[float]) -> dict:
    if not isinstance(notas, list):
        return {
            "status": "error",
            "message": "El parámetro 'notas' debe ser una lista de números."
        }
    if len(notas) == 0:
        return {
            "status": "error",
            "message": "La lista de notas no puede estar vacía."
        }
    for nota in notas:
        if isinstance(nota, bool) or not isinstance(nota, (int, float)):
            return {
                "status": "error",
                "message": "todas las notas deben ser numeros"
            }
        if nota < 0 or nota > 20:
            return {
                "status": "error",
                "message": "todas las notas deben estar entre 0 y 20"
            }
    
    promedio = sum(notas) / len(notas) if notas else 0
    return {
        "status": "success",
        "promedio": promedio
    }

def explicar_concepto(concepto: str) -> dict:

    conceptos = {
        "api": "Una API permite la comunicación entre sistemas.",
        "algoritmo": "Un algoritmo es un conjunto de instrucciones que permiten resolver un problema.",
        "base de datos": "Una base de datos es un conjunto de datos organizados y estructurados que permiten su almacenamiento y recuperación.",
        "chatbot": "Un chatbot es un programa de computadora diseñado para simular una conversación con usuarios humanos, especialmente a través de Internet.",
        "inteligencia artificial": "La inteligencia artificial es un campo de la informática que se centra en la creación de sistemas capaces de realizar tareas que normalmente requieren inteligencia humana, como el aprendizaje, el razonamiento y la toma de decisiones.",
        "machine learning": "El machine learning es una rama de la inteligencia artificial que se centra en el desarrollo de algoritmos y modelos que permiten a las computadoras aprender y mejorar automáticamente a partir de la experiencia sin ser explícitamente programadas.",
        "redes neuronales": "Las redes neuronales son un conjunto de algoritmos inspirados en el funcionamiento del cerebro humano, diseñados para reconocer patrones y realizar tareas de clasificación y predicción.",
        "big data": "El big data se refiere al manejo y análisis de grandes volúmenes de datos que no pueden ser procesados por métodos tradicionales debido a su tamaño, velocidad y variedad.",
        "cloud computing": "El cloud computing es un modelo de computación que permite acceder a recursos informáticos (como servidores, almacenamiento y aplicaciones) a través de Internet, sin necesidad de tenerlos físicamente en el lugar donde se utilizan."
    }

    concepto = concepto.lower().strip()

    if concepto in conceptos:
        return {
            "status": "success",
            "explicacion": conceptos[concepto]
        }

    return {
        "status": "not_found",
        "explicacion": "El concepto no se encuentra en la base de datos."
    }


root_agent = Agent(
    model=Gemini(
        model="gemini-3.5-flash-lite",
        retry_options=types.HttpRetryOptions(
            initial_delay=1,
            attempts=3
        )
    ),
    name="agente_ucv",
    description="Agente académico UCV",
    instruction="""
    
Eres un asistente académico de la UCV.
Responde siempre en español y utiliza lenguaje sencillo.

REGLAS OBLIGATORIAS:

1. Cuando el usuario pregunte por un concepto,
   debes consultar la herramienta explicar_concepto.

2. Si la herramienta devuelve status success,
   debes responder exactamente con el contenido
   del campo explicacion.

3. No debes ampliar, modificar, resumir ni
   complementar la explicación obtenida.

4. No debes utilizar tus conocimientos generales
   para reemplazar la información de la herramienta.

5. Si la herramienta devuelve status not_found,
   debes informar que el concepto no está registrado.
""",

    
    tools=[explicar_concepto, calcular_promedio]
)
