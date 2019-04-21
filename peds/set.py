
class Set:

    def __init__(self, s=set()):
        if isinstance(s, set):
            pass
        elif isinstance(s, Set):
            pass
        else:
            raise TypeError
