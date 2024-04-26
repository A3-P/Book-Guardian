import re


def validar_email(email):
    regex = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return re.match(regex, email) is not None


email = "exemplo@email.com"
input("digite seul email: ")
if validar_email(email):
    print("Email válido")
else:
    print("Email inválido")
