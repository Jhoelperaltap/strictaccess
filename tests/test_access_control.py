import pytest
from strictaccess import (
    strict_access_control,
    private,
    protected,
    PrivateAccessError,
    ProtectedAccessError,
)


@strict_access_control(debug=False)
class TestClass:
    def __init__(self):
        self._prot = 1
        self.__priv = 2

    @private
    def _my_private(self):
        return "secret"

    @private
    def __really_private(self):
        return "very secret"

    @protected
    def _my_protected(self):
        return "semi-secret"

    def public_method(self):
        return "public"


def test_public_access():
    obj = TestClass()
    assert obj.public_method() == "public"


def test_private_violation():
    obj = TestClass()
    with pytest.raises(PrivateAccessError):
        obj._my_private()


def test_name_mangled_private_violation():
    obj = TestClass()
    # Name-mangled __really_private aparece como:
    # _TestClass__really_private
    with pytest.raises(PrivateAccessError):
        getattr(obj, "_TestClass__really_private")()


def test_protected_violation():
    obj = TestClass()
    with pytest.raises(ProtectedAccessError):
        obj._my_protected()
