from google.adk.agents.llm_agent import Agent #importamos el agente de google.adk

def explicar_concepto (concepto: str) -> dict:  #aca definios explicar concepto y nos dice q concepto sera de tipo str
    conceptos = {
        "api": "una Api permite comunicacion entre sistemas.",
        "algoritmo": "un algoritmo es un conjunto de instrucciones que permiten resolver un problema.",
        "base de datos": "una base de datos es un conjunto de datos organizados y estructurados que permiten su almacenamiento y recuperación.",
    }
    concepto = concepto.lower().strip()  #convertimos el concepto a minusculas
    if concepto in conceptos:  #si el concepto esta en el diccionario
        return {
            "status": "success",
            "explicacion": conceptos[concepto]
        }
    return {
        "status": "not_found",
        "explicacion": "El concepto no se encuentra en la base de datos."
    }

root_agent = Agent(
    model="gemini-flash-latest",
    name="agente_ucv",
    description="Agente académico UCV",
    instruction="""
    Eres un asistente académico.
    Responde en español.
    Usa lenguaje simple.
    """,
    tools=[explicar_concepto],

)  #creamos una instancia del agente