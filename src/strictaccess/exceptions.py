class AccessControlError(Exception):
    """Base class for access control exceptions."""
    pass

class PrivateAccessError(AccessControlError):
    """Raised when trying to access a private attribute or method."""
    pass

class ProtectedAccessError(AccessControlError):
    """Raised when trying to access a protected attribute or method."""
    pass
