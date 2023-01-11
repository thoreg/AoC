"""Useful utility functions around data loading."""


def load_input(path):
    """Load given file path and stuff data into variable."""

    def wrap(func):
        def wrapped_f():
            data = []
            with open(path, "r") as f:
                data = f.read().splitlines()
            func(data)

        return wrapped_f

    return wrap
