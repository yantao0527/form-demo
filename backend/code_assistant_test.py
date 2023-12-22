from app.startup import startup

from app.langchain.assistants.code_assistant import CodeInterpreterAssistant

startup()
assistant = CodeInterpreterAssistant()
output = assistant.ask__question("What's 10 - 4 raised to the 2.7")
print()
for threadMessage in output:
    print(threadMessage)
    for messageContentText in threadMessage.content:
        print()
        print(messageContentText.text.value)