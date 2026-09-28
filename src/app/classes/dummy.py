class Dummy:
    def __init__(self):
        self.real = None
        self.update = True
        self.new_var = True

    def __repr__(self):
        return f"Dummy(real={self.real!r}, update={self.update!r}, new_var={self.new_var!r})"
