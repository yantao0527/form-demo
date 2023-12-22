import os
import logging

logging.basicConfig(
    format='%(asctime)s,%(msecs)03d %(levelname)-8s [%(filename)s:%(lineno)d in ' \
           '%(funcName)s] %(message)s',
    datefmt='%H:%M:%S',
    level=logging.INFO
)

logger = logging.getLogger(__name__)

# dotenv
from dotenv import load_dotenv

load_dotenv()

env_list = [
    "OPENAI_API_KEY",

    "SMTP_SERVER",
    "SMTP_USERNAME",
    "SMTP_PASSWORD",
]
for key in env_list:
    if not key in os.environ:
        print(f"\nCheck whether the variable {key} is defined in the file .env\n")
        exit(-1)

def startup():
    logger.info("app started up")