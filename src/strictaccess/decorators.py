from .core import AccessControlMixin


def strict_access_control(debug=False):
    def decorator(cls):
        class Wrapped(AccessControlMixin, cls):
            pass

        Wrapped._debug_mode = debug
        Wrapped.__name__ = cls.__name__
        Wrapped.__doc__ = cls.__doc__
        return Wrapped

    return decorator
