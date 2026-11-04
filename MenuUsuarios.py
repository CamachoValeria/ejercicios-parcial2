name=""
lastName="
age=0
birthday=""
email=""
password=""
confirmPass=""
opcion=0

print("Bienvenido al sistema de usuarios")
print("----------MENU DE OPCIOMES----------")
print("1.Registrar usuario")
print("2.Ver informacion de usuario")
print("3.Borrar informacion del usuario")
print("4.Modificar informacion del usuario")
print("5.salir")
print("------------------------------------")
opcion=int(input("Seleccione una opcion"))

match opcion:#Aqui inicia el match, que es una validacion de caso

    case 1:
    name=input("Ingresa tu nombre:")
lastName=input("ingresa tu apellido:")
age=int(input("Ingresa tu edad:"))
birthday=input("Ingresa tu fecha de nacimiento:")
email=input("Ingresa tu correo electronico:")
password=input("Ingresa tu contrasena:")
confirmPass=input("Confirma tu contrasena:")

case 2:
print=("Nombre:", name,)