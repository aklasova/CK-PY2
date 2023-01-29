class Book:
    """ Базовый класс книги. """

    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    @property
    def name(self):
        return self._name

    @property
    def author(self):
        return self._author

    def __str__(self):
        return f"Книга: {self.name}. Автор: {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        if not isinstance(pages, int):
            raise TypeError('Количество страниц должно быть типа int')
        if pages <= 0:
            raise ValueError('Количество страниц может быть только положительным числом')
        self.pages = pages

    def __str__(self):
        super_str = super().__str__()
        return f"{super_str}. Страницы: {self.pages}"


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        if not isinstance(duration, float):
            raise TypeError('Продолжительность должна быть типа float')
        if duration <= 0:
            raise ValueError('Продолжительность может быть только положительным числом')
        self.duration = duration

    def __str__(self):
        super_str = super().__str__()
        return f"{super_str}. Продолжительность: {self.duration}"


print(PaperBook('Игра престолов', 'Джордж Мартин', 755))
print(AudioBook('Игра престолов', 'Джордж Мартин', 33.48))
