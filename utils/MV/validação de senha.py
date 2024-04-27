import re


def validar_senha(senha):
    if len(senha) < 8:
        return False
    if not re.search("[A-Z]", senha):
        return False
    if not re.search("[a-z]", senha):
        return False
    if not re.search("[0-9]", senha):
        return False
    if not re.search("[!@#$%^&*()_+=-]", senha):
        return False
    return True


senha = input("Digite sua senha: ")

if validar_senha(senha):
    print("Senha válida!")
else:
    print(
        "Senha inválida! A senha deve conter no mínimo 8 caracteres, incluindo letras maiúsculas, minúsculas, números e caracteres especiais."
    )
    print()
