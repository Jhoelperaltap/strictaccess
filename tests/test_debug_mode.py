from strictaccess import strict_access_control, private


@strict_access_control(debug=True)
class DebugClass:
    @private
    def _x(self):
        return 42


def test_debug_print(capfd):
    obj = DebugClass()
    # Siguientes llamadas siguen devolviendo el valor, pero imprimen debug
    assert obj._x() == 42
    captured = capfd.readouterr()
    assert "[DEBUG] Access PRIVATE violation" in captured.out
