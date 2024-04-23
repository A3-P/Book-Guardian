
def validar_nome_usuario(nome_usuario):
    if len(nome_usuario) <= 100:
        return True
    else:
        return False

nome_usuario = input("Digite o nome de usuário: ")
if validar_nome_usuario(nome_usuario):
    print("Nome de usuário válido!")