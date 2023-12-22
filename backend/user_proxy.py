from form_assistant import FormAssistant

async def call_agent(input: str):
    assistant = FormAssistant()
    output = assistant.ask__question(input)
    return output["output"]