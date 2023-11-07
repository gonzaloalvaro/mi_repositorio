class alumno:
    def __init__(self,nombre, nota):
        self.nombre = nombre
        self.nota = nota
    def __str__(self):
        return f"NOMBRE: {self.nombre},{self.nota}"
    


