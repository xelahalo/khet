class Point:
    def __init__(self, i, j):

        # hacky hack, I'm lazy
        if i < 0 or j < 0:
            raise Exception()
        
        self._i = i
        self._j = j
    
    @property
    def i(self):
        return self._i

    @property
    def j(self):
        return self._j

    