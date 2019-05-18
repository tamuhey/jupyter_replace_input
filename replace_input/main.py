from IPython import get_ipython


def replace_input(line, cell):
    """Replace builtins.input to _myinput
    
    _myinput returns one line in cell per call.
    If the cell is exhausted, restore input to builtins.input and raise StopIteration
    """
    ip = get_ipython()
    _input = ip.ns_table["builtin"]["input"]
    itcell = iter(cell.split("\n"))

    def _myinput():
        try:
            return next(itcell)
        except StopIteration:
            global input
            ip.ns_table["builtin"]["input"] = _input
            raise StopIteration

    ip.user_ns["input"] = _myinput
