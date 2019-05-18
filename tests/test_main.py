import pytest
from IPython.testing.globalipapp import get_ipython

from replace_input import replace_input


def test_myinput():
    ip = get_ipython()

    test_cell = "foo\nbar"

    assert not ip.register_magic_function(replace_input, magic_kind="cell")
    assert not ip.run_cell_magic("replace_input", None, test_cell)

    for line in test_cell.split("\n"):
        c = ip.run_cell("input()")
        print(c.result)
        assert c.success
        assert c.result == line
    c = ip.run_cell("input()")
    assert not c.success
    assert isinstance(c.error_in_exec, StopIteration)
