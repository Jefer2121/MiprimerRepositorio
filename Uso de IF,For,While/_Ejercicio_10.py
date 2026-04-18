user_db = "admin"
pass_db = "1234"

usuario = input("Usuario: ")
clave = input("Contraseña: ")

if usuario == user_db and clave == pass_db:
    print("Acceso permitido")
else:
    print("Acceso denegado")