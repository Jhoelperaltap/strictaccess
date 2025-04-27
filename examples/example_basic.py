from strictaccess import strict_access_control

@strict_access_control()
class Punto:
    def __init__(self, x, y):
        self.__x = x
        self._y = y
        self.z = 0

    def get_x(self):
        return self.__x

p = Punto(1, 2)

print(p.z)        # OK
print(p.get_x())  # OK

# Estas líneas deben lanzar error
# print(p._y)      
# print(p.__x)     
