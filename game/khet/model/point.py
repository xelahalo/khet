class Point:
    def __init__(self, i, j):
        self._i = i
        self._j = j
    
    @property
    def i(self):
        return self._i

    @property
    def j(self):
        return self._j

    