class Personaje:
    def __init__(self, nombre, edad, nivel, puntos_salud):
        self.nombre = nombre
        self.edad = edad
        self.nivel = nivel
        self.puntos_salud = puntos_salud

    def subir_nivel(self):
        self.nivel += 1
        print(f"{self.nombre} ha subido al nivel {self.nivel}.")

    def recibir_daño(self, daño):
        self.puntos_salud -= daño
        if self.puntos_salud > 0:
            print(f"{self.nombre} ha recibido {daño} puntos de daño. Puntos de salud restantes: {self.puntos_salud}.")
        else:
            print(f"{self.nombre} ha recibido {daño} puntos de daño y ha sido derrotado.")

    def __str__(self):
        return f"Personaje: {self.nombre}, Edad: {self.edad}, Nivel: {self.nivel}, Puntos de Salud: {self.puntos_salud}"


# Crear un personaje principal
personaje_principal = Personaje(nombre="Aragorn", edad=87, nivel=5, puntos_salud=100)

# Mostrar información del personaje
print(personaje_principal)

# Subir de nivel
personaje_principal.subir_nivel()

# Recibir daño
personaje_principal.recibir_daño(30)

# Mostrar información actualizada del personaje
print(personaje_principal)
