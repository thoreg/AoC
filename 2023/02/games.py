import math
import re
from dataclasses import dataclass

MAX_RED = 12
MAX_GREEN = 13
MAX_BLUE = 14


@dataclass
class Game:
    _id: int
    red: int
    green: int
    blue: int


def main():
    """..."""
    with open("./02/input.txt", "r") as input:
        data = input.read().splitlines()

    possible_games = []
    list_of_all_maxies = []
    # for game_description in data[:3]:
    for game_description in data:
        game_id = int(game_description.split(":")[0].replace("Game ", ""))
        games = game_description.split(":")[1]
        print(game_description)

        #
        # part 1 - sum up ids of possible games
        #
        game_is_possible = True
        for snapshot in games.split(";"):
            print(f"  {snapshot}")
            red = re.findall(r"(\d+) red", snapshot)
            if red:
                if int(red[0]) > MAX_RED:
                    game_is_possible = False

            green = re.findall(r"(\d+) green", snapshot)
            if green:
                if int(green[0]) > MAX_GREEN:
                    game_is_possible = False

            blue = re.findall(r"(\d+) blue", snapshot)
            if blue:
                if int(blue[0]) > MAX_BLUE:
                    game_is_possible = False

        print(f"Game {game_id} is possible {game_is_possible}\n")

        if game_is_possible:
            possible_games.append(game_id)

        #
        # part 2 - sum up product of max of each color
        #
        maxies = {
            "red": 0,
            "green": 0,
            "blue": 0,
        }
        for snapshot in games.split(";"):
            print(f"  {snapshot}")
            red = re.findall(r"(\d+) red", snapshot)
            if red:
                maxies["red"] = max(int(red[0]), maxies["red"])

            green = re.findall(r"(\d+) green", snapshot)
            if green:
                maxies["green"] = max(int(green[0]), maxies["green"])

            blue = re.findall(r"(\d+) blue", snapshot)
            if blue:
                maxies["blue"] = max(int(blue[0]), maxies["blue"])

        print(f"maxies: {maxies}")
        product = math.prod(maxies.values())
        print(f"product: {product}")
        list_of_all_maxies.append(product)

    print(f"sum of all ids of possible games: {sum(possible_games)}")
    print(f"sum of all products of all maxies: {sum(list_of_all_maxies)}")


if __name__ == "__main__":
    main()
