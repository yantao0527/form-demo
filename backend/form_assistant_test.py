from startup import startup
from form_assistant import FormAssistant

startup()
assistant = FormAssistant()
#output = assistant.ask__question("who are you?")
#output = assistant.ask__question("Send an email to \"Frank Yan <frankyan.work@gmail.com>\" to inform him of a meeting at the company at nine o'clock tomorrow morning")
output = assistant.ask__question("Olga want to spend $1000 to lay concrete walkway in south of housing")
print(output)
print()
print(output["output"])
