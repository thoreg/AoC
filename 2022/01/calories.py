from dataclasses import dataclass
from operator import attrgetter
from pprint import pprint


@dataclass
class Elve:
    idx: int
    sum: int
    calories: list


def main():
    with open("./01/input.txt", "r") as input:
        data = input.read().splitlines()

    all_elves = []
    idx = 0
    calories = []

    for value in data:
        if not value:
            all_elves.append(Elve(idx, sum(calories), calories))
            calories = []
            idx += 1
            continue

        calories.append(int(value))

    primus_maximus = max(all_elves, key=attrgetter("sum"))
    print(f"[ 1 ][ sol 1 ] : strongest elve carries {primus_maximus.sum} calories")

    sorted_all_elves = sorted(all_elves, key=lambda k: k.sum, reverse=True)

    final_sum = 0
    for e in sorted_all_elves[:3]:
        # pprint(e)
        final_sum += e.sum
    print(f"[ 2 ][ sol 2 ] : sum of the three strongest elves: {final_sum}")


if __name__ == "__main__":
    main()
