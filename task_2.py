#1. Создай класс Movies:

class Movies:

#2. проинициализируй в нём пустой список self.movies через конструктор;

    def __init__(self):
       self.movies = []

#3. добавь метод add_movie(). Он будет принимать параметр movie и добавлять его в конец списка self.movies.

    def add_movie(self, movie):
        self.movies.append(movie)


#4. Создай два дочерних класса — Comedy и Drama. Они наследуют метод add_movie(). Метод этих классов должен принимать параметр movie и добавлять его в конец списка self.movies. Затем возвращать записи вида Комедии: '[]' и Драмы: '[]' соответственно.

class Comedy(Movies):
    def add_movie(self, movie):
        super().add_movie(movie)
        return f"Комедии: '{self.movies}'"
    
class Drama(Movies):
    def add_movie(self, movie):
        super().add_movie(movie)
        return f"Драмы: '{self.movies}'"
    
#5. Вызови метод add_movie() для объекта Comedy(). Входной параметр — 'Большой куш'. Выведи на экран результат.
comedy = Comedy()
print(comedy.add_movie('Большой куш'))

#6. Вызови метод add_movie() для объекта Drama(). Входной параметр — 'Оружейный барон'. Выведи на экран результат.
drama = Drama()
print(drama.add_movie('Оружейный барон'))