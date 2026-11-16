class MascotaVirtual:
    def __init__(self, nombre):
        self.nombre = nombre
        self.hambre = 50      # De 0 a 100
        self.felicidad = 50   # De 0 a 100
        self.energia = 50     # De 0 a 100

    def alimentar(self):
        self.hambre -= 15
        if self.hambre < 0:
            self.hambre = 0
        print(f"¡Has alimentado a {self.nombre}! Hambre actual: {self.hambre}")

    def jugar(self):
        self.felicidad += 15
        self.energia -= 10
        print(f"¡Has jugado con {self.nombre}! Felicidad: {self.felicidad}")

    def ver_estado(self):
        print(f"\n--- Estado de {self.nombre} ---")
        print(f"Hambre: {self.hambre}")
        print(f"Felicidad: {self.felicidad}")
        print(f"Energía: {self.energia}")

# Ejemplo de uso
mi_mascota = MascotaVirtual("Pixel")
mi_mascota.ver_estado()
mi_mascota.alimentar()