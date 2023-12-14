# ai_player.py

import random
from game import Game
from ai import AI


class AIPlayer:
    def __init__(self, side: str, ai: AI):
        self.side = side
        self.ai = ai
        self.old_state = None

    def get_side(self) -> str:
        """Возвращает символ, которым играет игрок"""
        return self.side

    def make_step(self, game: Game):
        """Выбирает следующий шаг из оставшихся доступных ходов"""

        # получаем список доступных ходов
        free = game.get_free()

        # случайным образом решаем, является ли текущий ход
        # зондирующим (случайным) или жадным (максимально выгодным)
        # с вероятностью 10% для зондирующего хода
        if random.randint(0, 100) < 10:
            print("случайны ход")
            step = random.choice(free)
            game.set(step, self.side)
            self.old_state = game.get_state(self.side)
            return

        # "жадный" ход
        rewards = {}
        for step in free:
            # для каждого доступного хода оцениваем состояние игры после него
            new_game = Game(game.get_state(self.side))
            new_game.set(step, self.side)
            rewards[step] = self.ai.get_reward(new_game.get_state(self.side))

        # выясняем, какое вознаграждение оказалось максимальным
        max_reward = max(rewards.values())

        # находим все шаги с максимальным вознаграждением
        steps = [
            step
            for step, reward in rewards.items()
            if max_reward - 0.01 < reward < max_reward + 0.01
        ]

        # корректируем оценку прошлого состояния
        # с учетом ценности нового состояния
        if self.old_state is not None:
            self.ai.correct(self.old_state, max_reward)

        # выбираем ход из ходов с максимальным вознаграждением
        step = random.choice(steps)
        game.set(step, self.side)

        # сохраняем текущее состояние для того,
        # чтобы откорректировать её ценность на следующем ходе
        self.old_state = game.get_state(self.side)

    def lose(self):
        """корректирует ценность предыдущего состояния при проигрыше"""
        if self.old_state is not None:
            self.ai.correct(self.old_state, 0)

    def win(self):
        """корректирует ценность предыдущего состояния при выигрыше"""
        if self.old_state is not None:
            self.ai.correct(self.old_state, 1)

    def draw(self):
        """корректирует ценность предыдущего состояния при ничьей"""
        if self.old_state is not None:
            self.ai.correct(self.old_state, 0.5)
