from replace_input.main import replace_input


def load_ipython_extension(ipython):
    ipython.register_magic_function(replace_input, "cell")
