import inspect
from .exceptions import PrivateAccessError, ProtectedAccessError

class AccessControlMixin:
    _debug_mode = False  # Default no debug

    def __getattribute__(self, name):
        value = super().__getattribute__(name)

        if name.startswith('__') and not name.endswith('__'):
            self._handle_violation('private', name)
        elif name.startswith('_') and not name.startswith('__'):
            caller = inspect.stack()[1].frame.f_locals.get('self', None)
            if caller is not self:
                self._handle_violation('protected', name)

        # Check access level for methods
        if callable(value):
            access_level = getattr(value, '_access_level', None)
            if access_level == 'private':
                self._handle_violation('private', name)
            elif access_level == 'protected':
                caller = inspect.stack()[1].frame.f_locals.get('self', None)
                if caller is not self:
                    self._handle_violation('protected', name)

        return value

    def _handle_violation(self, level, name):
        if self._debug_mode:
            print(f"[DEBUG] Access {level.upper()} violation: {name}")
        else:
            if level == 'private':
                raise PrivateAccessError(f"Access to private member '{name}' is forbidden.")
            elif level == 'protected':
                raise ProtectedAccessError(f"Access to protected member '{name}' is forbidden.")
