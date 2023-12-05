from dataclasses import dataclass


def test_get_points() -> None:
    """Points per line are returned properly."""
    assert get_points("Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53") == 8
    assert get_points("Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19") == 2
    assert get_points("Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1") == 2
    assert get_points("Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83") == 1
    assert get_points("Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36") == 0
    assert get_points("Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11") == 0


def test_get_number_of_cards() -> None:
    data = (
        "Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53",
        "Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19",
        "Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1",
        "Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83",
        "Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36",
        "Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11",
    )
    assert get_number_of_cards(data) == 30


def get_points(line) -> int:
    """Return points of the line. Each match from the left side doubles the points."""

    line = line.split(":")[1]

    win_numbers, numbers = line.split("|")

    points = 0
    win_numbers = win_numbers.split()
    numbers = numbers.split()
    for win_number in win_numbers:
        if win_number in numbers:
            if not points:
                points = 1
            else:
                points += points

    return points


def get_number_of_wins(line) -> int:
    """Return the number of matches from the left to the right side."""

    line = line.split(":")[1]

    win_numbers, numbers = line.split("|")

    wins = 0
    win_numbers = win_numbers.split()
    numbers = numbers.split()
    for win_number in win_numbers:
        if win_number in numbers:
            wins += 1

    return wins


@dataclass
class Card:
    instances: int
    wins: int


def get_number_of_cards(data) -> int:
    all = {}
    for num, line in enumerate(data, start=1):
        all[num] = Card(
            instances=1,
            wins=get_number_of_wins(line),
        )

    for key in all:
        origin_card = all[key]
        for offset in range(1, origin_card.wins + 1):
            card = all[key + offset]
            card.instances += 1 * origin_card.instances

    result = 0
    for card in all.values():
        result += card.instances

    return result


def main():
    """..."""
    with open("./04/input.txt", "r") as input:
        data = input.read().splitlines()
    #
    # Solution - Task 1
    #
    points = 0
    for line in data:
        points += get_points(line)
    print(f"points: {points}")
    #
    # Solution - Task 2
    #
    number_of_cards = get_number_of_cards(data)
    print(f"number_of_cards: {number_of_cards}")


if __name__ == "__main__":
    main()
