import re


def validar_senha(senha):
    if len(senha) < 6:
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
