# ai.py

import json
import os

from game import Game
from typing import Dict

reward_file = "rewards.json"


class AI:
    table = {}

    def __init__(self):
        self.table: Dict[str, float] = self.load()

    def get_reward(self, state: str) -> float:
        """Расчет оценки состояния игры"""

        game = Game(state)

        # если победитель - мы, то оценка состояния игры "1"
        # если победиль - соперник, то оценка состояния игры "0"
        if game.is_win("x"):
            return 1.0
        elif game.is_win("o"):
            return 0.0

        # смотрим ценность по таблице
        # если в таблице нет, то считаем начальной ценностью "0.5"
        if state in self.table:
            return self.table[state]

        return 0.5

    def correct(self, state: str, new_reward: float) -> None:
        """Корректирующая функция"""

        old_reward = self.get_reward(state)
        self.table[state] = old_reward + 0.1 * (new_reward - old_reward)
        print(f"correct {state} => {self.table[state]}")

    def load(self) -> Dict[str, float]:
        """Загружает таблицу ценностей из файла. Если файл отсутсвует, создает новый"""

        # проверяем существует ли файл
        if not os.path.exists(reward_file):
            return {}

        with open(reward_file, "r") as file:
            table = json.load(file)
            return table

    def save(self) -> None:
        """Сохраняет таблицу ценностей в файл на диск"""

        with open(reward_file, "w") as file:
            json.dump(self.table, file, ensure_ascii=False, indent="\t")
