import time

print("Iniciando programa especial...")
time.sleep(1)

print("\nAnalizando sentimientos...")
time.sleep(2)

print("\nResultado encontrado:\n")
time.sleep(1)

mensaje = """
Desde que llegaste a mi vida,
todo tiene más color 💫

La verdad no se cuanto me quieras,
pero yo si que te quiero un monton ❤️

Eres la persona mas bella de mi vida
dejame estar a tu lado mucho tiempo 💕
"""

for letra in mensaje:
    print(letra, end="", flush=True)
    time.sleep(0.05)

print("\n\nPrograma finalizado...")
print("Pero lo que siento por ti apenas comienza 😉")
