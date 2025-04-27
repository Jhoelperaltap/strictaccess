from strictaccess import strict_access_control

@strict_access_control(debug=True)
class Prueba:
    def __init__(self):
        self.__secret = 123
        self._protected = 'hola'
        self.public = 'ok'

p = Prueba()
print(p.public)         # OK
print(p._protected)     # Warning
print(p.__secret)       # Warning
