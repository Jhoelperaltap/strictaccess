from strictaccess import strict_access_control, private, protected, public

@strict_access_control()
class Persona:
    def __init__(self, nombre):
        self.__nombre = nombre

    @private
    def _calcular_edad(self):
        return 25

    @protected
    def _saludar(self):
        print(f"Hola, soy {self.__nombre}")

    @public
    def mostrar_nombre(self):
        print(f"Nombre: {self.__nombre}")

p = Persona("Jhoel")
p.mostrar_nombre()  # OK

# Estas líneas deben lanzar error
# p._saludar()       
# p._calcular_edad()
