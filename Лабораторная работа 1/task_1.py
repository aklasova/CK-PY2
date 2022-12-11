import doctest

class Notebook:
    def __init__(self, subject: str, pages: int, clean_pages: int):
        """
            Создание и подготовка к работе объекта "Тетрадь"

        :param subject: учебный предмет
        :param pages: количество страниц
        :param clean_pages: количество чистых страниц

        """
        if not isinstance(subject, str):
            raise TypeError('Название учебного предмета должно быть типа str')
        self.subject = subject
        if not isinstance(pages, int):
            raise TypeError('Количество страниц должно быть типа int')
        if pages <= 0:
            raise ValueError('Количество страниц может быть только положительным числом')
        self.pages = pages
        if not isinstance(clean_pages, int):
            raise TypeError('Количество страниц должно быть типа int')
        if clean_pages < 0:
            raise ValueError('Количество страниц не может быть отрицательным числом')
        self.clean_pages = clean_pages

    def buy_new_notebook(self) -> bool:
        """
        Функция, которая проверяет, нужно ли покупать новую тетрадь

        :return: Количество чистых страниц

        """
        ...

    def other_subject(self) -> bool:
        """
        Функция, которая проверяет, можно ли использовать тетрадь для других предметов
        Например, тетрадь по биологии в клетку, значит ее можно использовать для математики, но нельзя для русского языка

        :return: Учебный предмет

        """
        ...


if __name__ == "__main__":
    notebook = Notebook('Биология', 48, 0)
    notebook.buy_new_notebook()
    notebook = Notebook('Биология', 48, 48)
    notebook.other_subject()
    doctest.testmod()

class Bottle:
    def __init__(self, material: str, volume: int, liquid_volume: int):
        """
        Создание и подготовка к работе объекта "Бутылка"

        :param material: Материал бутылки
        :param volume: Объем бутылки
        :param liquid_volume: Объем жидкости

        """
        if not isinstance(material, str):
            raise TypeError('Название материала бутылки тип str')
        self.material = material
        if not isinstance(volume, int):
            raise TypeError('Объем бутылки тип int')
        if volume <= 0:
            raise ValueError('Объем бутылки может быть только положительным числом')
        self.volume = volume
        if not isinstance(liquid_volume, int):
            raise TypeError('Объем жидкости тип int')
        if liquid_volume <= 0:
            raise ValueError('Объем жидкости может быть только положительным числом')
        self.liquid_volume = liquid_volume

    def recycling(self) -> bool:
        """
        Функция, которая проверяет, сделана ли бутылка из перерабатываемого материала

        :return: Материал бутылки

        """
        ...

    def pour_out(self) -> None:
        """
        Вылить жидкость из бутылки, например, в стакан

        :return: объем вылитой жидкости

        """
        ...

if __name__ == "__main__":
    bottle = Bottle('Пластик', 500, 250)
    bottle.recycling()
    bottle = Bottle('Пластик', 500, 250)
    bottle.pour_out()
    doctest.testmod()

class MusicColumn:
    def __init__(self, max_volume: int, now_volume: int, max_battery: int, now_battery: int):
        """
        Создание и подготовка к работе объекта "Музыкальная колонка"

        :param max_volume: Максимальная громкость (индикатор)
        :param now_volume: Показатель громкости сейчас (индикатор)
        :param max_battery: Максимальный заряд аккумулятора
        :param now_battery: Заряд аккумулятора сейчас

        """

        if not isinstance(max_volume, int):
            raise TypeError('Максимальная громкость тип int')
        if max_volume <= 0:
            raise ValueError('Максимальная громкость может быть только положительным числом')
        self.max_volume = max_volume
        if not isinstance(now_volume, int):
            raise TypeError('Показатель громкости сейчас тип int')
        if now_volume < 0:
            raise ValueError('Показатель громкости не может быть отрицательным числом')
        self.now_volume = now_volume
        if not isinstance(max_battery, int):
            raise TypeError('Максимальный заряд аккумулятора тип int')
        if max_battery <= 0:
            raise ValueError('Максимальный заряд аккумулятора может быть только положительным числом')
        self.max_battery = max_battery
        if not isinstance(now_battery, int):
            raise TypeError('Заряд аккумулятора сейчас тип int')
        if now_battery < 0:
            raise ValueError('Заряд аккумулятора сейчас не может быть отрицательным числом')
        self.now_battery = now_battery

    def charge(self) -> bool:
        """
        Функция, которая проверяет, нужно ли зарядить музыкальную колонку

        :return: Заряд аккумулятора сейчас

        """
        ...

    def without_sound(self) -> None:
        """
        Функция выключения звука на музыкальной колонке

        :return: Показатель громкости сейчас (снижение его до нуля)

        """
        ...

if __name__ == "__main__":
    music_column = MusicColumn(20, 10, 2500, 2000)
    music_column.charge()
    music_column = MusicColumn(20, 10, 2500, 2000)
    music_column.without_sound()
    doctest.testmod()

