
from startup import startup
from utilities.email.send import send_email

if __name__ == '__main__':
    startup()

    send_email("frankyan.work@gmail.com", "Hello!", "Hello world plain text!")
    