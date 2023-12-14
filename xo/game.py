# game.py

from typing import List


class Game:
    def __init__(self, field=None):
        if field:
            self.field = field
        else:
            self.start()

    def start(self):
        """Начинает игру с пустого поля"""

        self.field = " " * 9

    def print_field(self):
        """Выводит текущее стостояние поля"""

        for i in range(len(self.field)):
            cell = self.field[i]
            print("[" + (cell if cell != " " else str(i + 1)) + "]", end="")
            if i % 3 == 2:
                print()

    def set(self, position: int, side: str):
        """Устанавливает символ на переданную позицию"""

        self.field = self.field[: position - 1] + side + self.field[position:]

    def get_free(self) -> List[int]:
        """Возвращает список доступных ходов"""

        return [i + 1 for i in range(len(self.field)) if self.field[i] == " "]

    def is_draw(self) -> bool:
        """Проверяет игру на ничью"""

        return not self.get_free()

    def is_win(self, side: str) -> bool:
        """Проверяет игру на победу."""

        for i in range(3):
            is_win = all(self.field[i * 3 + j] == side for j in range(3))
            if is_win:
                return True

            is_win = all(self.field[j * 3 + i] == side for j in range(3))
            if is_win:
                return True

        is_win = all(self.field[i * 3 + i] == side for i in range(3))
        if is_win:
            return True

        is_win = all(self.field[i * 3 + 2 - i] == side for i in range(3))
        return is_win

    def get_state(self, side: str) -> str:
        """Возвращает состояние поля после хода"""

        if side == "x":
            return self.field

        new_field = ""
        for cell in self.field:
            if cell == "x":
                new_field += "o"
            elif cell == "o":
                new_field += "x"
            else:
                new_field += cell

        return new_field
