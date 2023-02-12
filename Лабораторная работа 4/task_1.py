import doctest


class ComputerGame:
    """ Базовый класс компьютерной игры"""

    def __init__(self, developer: str, category: str, size: float):
        """ Cоздание и подготовка к работе объекта 'Компьютерная игра'
        :param developer: Разработчик
        :param category: Категория
        :param size: Размер(занимаемая память)
        """
        self._developer = developer
        self._category = category
        self._size = size

    @property
    def developer(self):
        return self._developer

    @developer.setter
    def developer(self, new_developer: str) -> None:
        if not isinstance(new_developer, str):
            raise TypeError('Разработчик должен быть типа str')
        self._developer = new_developer

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, new_category: str) -> None:
        if not isinstance(new_category, str):
            raise TypeError('Категория должна быть типа str')
        self._category = new_category

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, new_size: float) -> None:
        if not isinstance(new_size, float):
            raise TypeError('Размер(занимаемая память) должно быть типа int')
        if new_size <= 0:
            raise ValueError('Размер(занимаемая память) должна быть больше нуля')
        self._size = new_size

    def __str__(self):
        return f"Разработчик: {self.developer}. Категория: {self.category}. Размер(Занимаемая память): {self.size}"

    def __repr__(self):
        return f"{self.__class__.__name__}(developer={self.developer!r}, category={self.category!r}, " \
               f"size={self.size!r})"

    def size_game(self) -> bool:
        """
        Метод показывает размер игры относительно 100 Гб
        :return: Весит ли игра больше 100 Гб
        """
        if self.size > 100:
            return True
        else:
            return False

    def company(self):
        """
        Метод выводит компанию разработчика

        :return: Название компании разработчика
        """
        print(self.developer)


class AssassinsCreed(ComputerGame):
    def __init__(self, developer: str, category: str, size: float, weapon: str, damage: int):
        """

        :param developer: Разработчик
        :param category: Категория
        :param size: Размер(занимаемая память)
        :param weapon: Применяемое оружие
        :param damage: Наносимый урон
        """
        super().__init__(developer, category, size)
        self._weapon = weapon
        self._damage = damage

    @property
    def weapon(self):
        return self._weapon

    @weapon.setter
    def weapon(self, new_weapon: str) -> None:
        if not isinstance(new_weapon, str):
            raise TypeError('Применяемое оружие должно быть типа str')
        self._weapon = new_weapon

    @property
    def damage(self):
        return self._damage

    @damage.setter
    def damage(self, new_damage: int) -> None:
        if not isinstance(new_damage, int):
            raise TypeError('Наносимый урон должен быть типа int')
        if new_damage <= 0:
            raise ValueError('Наносимый урон может быть только положительным числом')
        self._damage = new_damage

    def __str__(self):
        super_str = super().__str__()
        return f"{super_str}. Применяемое оружие: {self.weapon}. Наносимый урон: {self.damage}"

    def __repr__(self):
        super_repr = super().__repr__()
        return f'{super_repr}(weapon={self.weapon!r}, damage={self.damage!r})'

    def size_game(self):
        super_size = super().size_game()
        return f'{super_size}'

    def company(self):
        super().company()
        return f'Montpellier'


class NeedForSpeed(ComputerGame):
    def __init__(self, developer: str, category: str, size: float, car: str, speed: int):
        """

        :param developer: Разработчик
        :param category: Категория
        :param size: Размер(занимаемая память)
        :param car: Автомобиль
        :param speed: Скорость
        """
        super().__init__(developer, category, size)
        self._car = car
        self._speed = speed

    @property
    def car(self):
        return self._car

    @car.setter
    def car(self, new_car: str) -> None:
        if not isinstance(new_car, str):
            raise TypeError('Автомобиль должен быть типа str')
        self._car = new_car

    @property
    def speed(self):
        return self._speed

    @speed.setter
    def speed(self, new_speed: int) -> None:
        if not isinstance(new_speed, int):
            raise TypeError('Наносимый урон должен быть типа int')
        if new_speed < 0:
            raise ValueError('Скорость не может быть отрицательным числом')
        self._speed = new_speed

    def __str__(self):
        super_str = super().__str__()
        return f"{super_str}. Автомобиль: {self.car}. Скорость: {self.speed}"

    def __repr__(self):
        super_repr = super().__repr__()
        return f'{super_repr}(car={self.car!r}, speed={self.speed!r})'

    def size_game(self):
        super_size = super().size_game()
        return f'{super_size}'

    def company(self):
        super().company()
        return f'Gothenburg'


if __name__ == "__main__":
    computer_game = ComputerGame('Rockstar Games', 'Экшн и приключения', 123.4)
    print(computer_game.size)
    print(computer_game.size_game())
    nfs = NeedForSpeed('Electronic Arts', 'Гонки', 31.22, 'Infiniti', 230)
    print(nfs.size_game())
    print(nfs.company())
    print(nfs.car)
    as_cr = AssassinsCreed('Ubisoft', 'Экшн и приключения', 75.9, 'Топор', 350)
    print(as_cr.size_game())
    print(as_cr.company())
    print(as_cr.damage)
    doctest.testmod()
    pass
