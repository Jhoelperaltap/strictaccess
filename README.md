# strictaccess

![PyPI Version](https://img.shields.io/pypi/v/strictaccess)
![License](https://img.shields.io/pypi/l/strictaccess)
![Python Versions](https://img.shields.io/pypi/pyversions/strictaccess)
![Downloads](https://img.shields.io/pypi/dm/strictaccess)

**strictaccess** es un paquete de Python que permite imponer control estricto de acceso sobre atributos y métodos en clases, similar a lo que ocurre en lenguajes como Java o C++.

Con este paquete puedes controlar el acceso a tus atributos y métodos mediante los decoradores `@private`, `@protected`, `@public`.

## Características

- **Control estricto de acceso**: Asegura que los atributos y métodos sean correctamente accesibles solo desde donde deberían serlo.
- **Decoradores disponibles**: `@private`, `@protected`, `@public`.
- **Modo Debug**: Para facilitar el desarrollo y el monitoreo de los accesos.
- **Excepciones personalizadas**: `PrivateAccessError` y `ProtectedAccessError` para manejar accesos no permitidos.

## Instalación

Puedes instalar **strictaccess** desde PyPI utilizando `pip`:

```bash
pip install strictaccess
