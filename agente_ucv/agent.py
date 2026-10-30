
from google.adk.agents.llm_agent import Agent
from google.adk.models.google_llm import Gemini
from google.genai import types


def explicar_concepto(concepto: str) -> dict:

    conceptos = {
        "api": "Una API permite la comunicación entre sistemas.",
        "algoritmo": "Un algoritmo es un conjunto de instrucciones que permiten resolver un problema.",
        "base de datos": "Una base de datos es un conjunto de datos organizados y estructurados que permiten su almacenamiento y recuperación."
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

    
    tools=[explicar_concepto]
)
