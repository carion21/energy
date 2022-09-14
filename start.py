
from os import system as runcom

command = "uvicorn main:app --reload --host 0.0.0.0"
runcom(command)