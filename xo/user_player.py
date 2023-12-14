# user_player.py

from abc import ABC, abstractmethod
from game import Game


class PlayerInterface(ABC):
    """Абстрактный класс, используемый для определения интерфейса пользователя"""

    @abstractmethod
    def get_side(self) -> str:
        pass

    @abstractmethod
    def make_step(self, game: Game) -> None:
        pass

    @abstractmethod
    def lose(self) -> None:
        pass

    @abstractmethod
    def win(self) -> None:
        pass

    @abstractmethod
    def draw(self) -> None:
        pass


class UserPlayer(PlayerInterface):
    def __init__(self, side: str):
        self.side = side

    def get_side(self) -> str:
        """Возвращает символ, которым играет игрок"""

        return self.side

    def make_step(self, game: Game) -> None:
        """Делает следующий шаг из оставшихся доступных ходов"""

        game.print_field()
        free = game.get_free()

        while True:
            user_input = input()
            if user_input in map(str, free):
                break

        game.set(int(user_input), self.side)

    def lose(self) -> None:
        print("вы проиграли")

    def win(self) -> None:
        print("вы выиграли")

    def draw(self) -> None:
        print("ничья")
