# main.py

from user_player import UserPlayer
from ai_player import AIPlayer
from ai import AI
from game import Game
from typing import Union


def main():
    print(
        "Выберите сторону:\nX) x\nO) o\nЛюбой другой символ или ничего, для игры AI против AI"
    )
    side = input()

    ai = AI()
    game_count = 1

    player_x: Union[UserPlayer, AIPlayer]
    player_o: Union[UserPlayer, AIPlayer]

    if side.lower() == "x":
        player_x = UserPlayer("x")
        player_o = AIPlayer("o", ai)
    elif side.lower() == "o":
        player_x = AIPlayer("x", ai)
        player_o = UserPlayer("o")
    else:
        player_x = AIPlayer("x", ai)
        player_o = AIPlayer("o", ai)
        print("Введите количество партий")
        game_count = max(1, int(input()))

    game = Game()

    for i in range(game_count):
        print(f"Новая игра #{i + 1}")
        game.start()

        while True:
            if game.is_draw():
                player_x.draw()
                player_o.draw()
                break

            player_x.make_step(game)
            if game.is_win(player_x.get_side()):
                player_x.win()
                player_o.lose()
                break

            if game.is_draw():
                player_x.draw()
                player_o.draw()
                break

            player_o.make_step(game)
            if game.is_win(player_o.get_side()):
                player_o.win()
                player_x.lose()
                break

        game.print_field()

    ai.save()


# 5242

if __name__ == "__main__":
    main()
