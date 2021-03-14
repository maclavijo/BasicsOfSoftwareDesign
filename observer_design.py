
class MovieList:
    def __init__(self):
        self.movielist = []
        self._observersList = []

    def addMovie(self,movie):
        self.movielist.append(movie)
        self._notify()

    def _notify(self):
        for observer in self._observersList:
            observer.update(self)

    def get_state(self):
        return self.movielist

    def addMovie(self,observer):
        self._observersList.append(observer)

class Drama(MovieList):
    pass

class Comedy(MovieList):
    pass

class Action(MovieList):
    pass

