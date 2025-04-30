# strictaccess

![PyPI Version](https://img.shields.io/pypi/v/strictaccess)
![Build Status](https://github.com/jhoelperaltap/strictaccess/actions/workflows/ci.yml/badge.svg)
![Coverage](https://img.shields.io/codecov/c/github/jhoelperaltap/strictaccess)
![License](https://img.shields.io/pypi/l/strictaccess)

# strictaccess

**strictaccess** es un paquete de Python que impone control estricto de acceso a atributos y métodos en clases, similar a lo que ofrecen lenguajes como Java o C++.

## Características principales

- Control de acceso privado (`@private`) y protegido (`@protected`).
- Decorador de clase `@strict_access_control` para aplicar la lógica automáticamente.
- Modo `debug` para visualizar violaciones sin detener la ejecución.
- Excepciones personalizadas: `PrivateAccessError`, `ProtectedAccessError`.

## Instalación

```bash
pip install strictaccess

## Uso básico

```python
from strictaccess import strict_access_control, private, PrivateAccessError

@strict_access_control(debug=False)
class Cuenta:
    def __init__(self, saldo):
        self._saldo = saldo

    @private
    def _ajustar(self, delta):
        self._saldo += delta

    def ver_saldo(self):
        return self._saldo

cuenta = Cuenta(100)
print(cuenta.ver_saldo())  # 100

try:
    cuenta._ajustar(50)
except PrivateAccessError as e:
    print(e)  # Access to private member '_ajustar' is forbidden.

from strictaccess import strict_access_control, private

@strict_access_control(debug=True)
class MiClase:
    def __init__(self):
        self._valor = 42

    @private
    def _metodo_privado(self):
        return "secreto"

obj = MiClase()
print(obj._valor)  # [DEBUG] Access PROTECTED violation: _valor
print(obj._metodo_privado())  # [DEBUG] Access PRIVATE violation: _metodo_privado

Modo Debug vs. Excepciones

debug=False (por defecto): lanza PrivateAccessError o ProtectedAccessError.

debug=True: imprime en consola pero continúa la ejecución.

Marca un método como protegido. Sólo puede llamarse desde dentro de la misma instancia.


@protected
def _metodo_protegido(self):
    ...

Decorador de clase

strict_access_control(debug: bool = False)

Envuelve tu clase para añadir la lógica de control de acceso.

debug: si es True, las violaciones se imprimen en lugar de lanzar.

@strict_access_control(debug=True)
class MiClase: ...

Excepciones

PrivateAccessError: se lanza en accesos a métodos/atributos privados.

ProtectedAccessError: se lanza en accesos a métodos/atributos protegidos.

Estructura de módulos

access_tags.py: decoradores @private, @protected, @public.

core.py: implementación de AccessControlMixin y lógica de inspección.

decorators.py: @strict_access_control para clases.

exceptions.py: definiciones de excepción.

