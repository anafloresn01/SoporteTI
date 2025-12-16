print("Cuál es tu primer nombre")
nombre = input()
print("Cuál es tu primer nombre")
apellido = input ()
print("Cuál es tu primer nombre")

print("Hoy vamos a contar una historia.")
nombre = input("Escribe un nombre: ")
npuesto = input("Escribe el nombre de un puesto: ")
adj1 = input("Escribe un adjetivo para describir a un compañero: ")
adj2 = input("Escribe un adjetivo para describir al maestro: ")
comida = input("Escribe una comida: ")
snack = input("Escribe otra comida: ")
sentimiento = input("Escribe un sentimiento: ")

historia = (
    f"{nombre} ha comenzado hoy su primer curso de Generation. "
    f"Se está formando como {npuesto}. "
    f"Su compañero les pareció muy {adj1}, pero su profesor era, cuando menos, {adj2}. "
    f"Para comer comen {comida} y {snack} mientras repasan sus notas. "
    f"Sienten {sentimiento} pero están decididos a completar el curso."
)

print("---- La historia queda así ---")
print(historia)



#---------------------------------------------------

print("Hoy vamos a contar una historia sobre un explorador. \n")
nexplorador = input("Escribe un nombre para el explorador: ")
npais = input("Escribe el pais al que visitará: ")
tiempo = input("Escribe una catidad de años : ")
sonido = input("Escribe un sonido: ")
objAntiguo = input("Escribe un objeto antiguo: ")
cPolvo= input("Escribe un color para el polvo: ")
personajeAn = input("Escribe un personaje antiguo: ")
adjetivo= input("Escribe un adjetivo de carácter: ")
sensa1= input("Escribe una sensación: ")
sensa2= input("Escribe otra sensación: ")
criatura = input ("Escribe el nombre de una criatura: ")
tesoro= input ("Escribe un tesoro a encontrar: ")

historia2 = (
    f"{nexplorador} viajó hasta el lejano {npais} para investigar un castillo que había sido abandonado durante más de {tiempo} años. "
    f"Al entrar por el enorme portón, escuchó un {sonido} que resonó por todo el pasillo principal. "
    f"En el centro de la sala, encontró un {objAntiguo} cubierto por una capa gruesa de {cPolvo}. "
    f"Según los registros, ese objeto pertenecía al legendario {personajeAn}, conocido por su carácter {adjetivo} y sus decisiones impredecibles. "
    f"Mientras avanzaba por los corredores, {nexplorador} sentía una combinación de {sensa1} y {sensa2}, pero sabía que no podía detenerse."
    f"Todo cambió cuando descubrió una puerta oculta detrás de un tapiz con un dibujo de {criatura}. "
    f"Dentro de esa habitación secreta, encontró un mapa que revelaba la ubicación de un {tesoro} que llevaba siglos perdido. "
)

print("---- La historia queda así ---")
print(historia2)