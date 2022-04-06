

from classroom.asignatura import Asignatura


class Grupo:

    grado = "Grado 12" 

    def __init__(self, grupo="grupo predeterminado", asignaturas=None, estudiantes=None):

        self._grupo = grupo
        self._asignaturas = asignaturas
        self.listadoAlumnos = estudiantes
        if (asignaturas is None): 
            asignaturas = []
        if (estudiantes is None): 
            estudiantes = []

    def listadoAsignaturas(self, **kwargs):
        for x in kwargs.values():
            self._asignaturas.append(Asignatura(x))

    def agregarAlumno(self,*args):
           if self.listadoAlumnos is None:
            self.listadoAlumnos = []
            
            for a in args:
                self.listadoAlumnos.append(a)

    def __str__(self):
            return "Grupo de estudiantes: " + self._grupo

    @ classmethod
    def asignarNombre(cls, nombre="Grado 6"):
        cls.grado = nombre