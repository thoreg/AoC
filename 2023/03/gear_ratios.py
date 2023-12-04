from dataclasses import dataclass, field
from pprint import pprint

DEBUG = False


def test_get_part_numbers():
    """Basic algorithm."""
    data = (
        "467..114..",
        "...*......",
        "..35..633.",
        "......#...",
        "617*......",
        ".....+.58.",
        "..592.....",
        "......755.",
        "...$.*....",
        ".664.598..",
    )
    assert get_part_numbers(data) == 4361


def test_neighbour_match():
    """..."""
    data = (
        "467..114..",
        "...*......",
        "..35..633.",
        "......#...",
        "617*......",
        ".....+.58.",
        "..592.....",
        "......755.",
        "...$.*....",
        ".664.598..",
    )
    f = Field()
    idx = 0
    for line in data:
        if not f.line_length:
            f.line_length = len(line)

        for c in line:
            f.all[idx] = c
            idx += 1

    __print_field(data)
    assert f.neighbour_match(0) is False
    assert f.neighbour_match(1) is False
    assert f.neighbour_match(2) is True
    assert f.neighbour_match(99) is False
    assert f.neighbour_match(98) is False
    assert f.neighbour_match(45) is False
    assert f.neighbour_match(63) is False
    assert f.neighbour_match(50) is False
    assert f.neighbour_match(55) is False


def __print_field(data):
    line_number = 1
    print("\n")
    for line in data:
        print(f"{line} {len(line)} {line_number:03}")
        line_number += 1
    print("\n")


@dataclass
class Field:
    """The whole playground."""

    legit_numbers: list[str] = field(default_factory=list)
    all: dict = field(default_factory=dict)
    line_length: int = 0

    def neighbour_match2(self, idx) -> bool:
        """Print a single field (in the middle) and its neighbours.

        Each single field has the following neighbors:

        a b c - on top
        previous - value - next
        x y z - on the bottom

        +-----+-----+-----+
        | {a} | {b} | {c} |
        +-----+-----+-----+
        | {p} | {v} | {n} |
        +-----+-----+-----+
        | {x} | {y} | {z} |
        +-----+-----+-----+

        """
        a = self.all.get(idx - self.line_length - 1, " ")
        b = self.all.get(idx - self.line_length, " ")
        c = self.all.get(idx - self.line_length + 1, " ")
        p = self.all.get(idx - 1, " ")
        v = self.all.get(idx)
        n = self.all.get(idx + 1, " ")
        x = self.all.get(idx + self.line_length - 1, " ")
        y = self.all.get(idx + self.line_length, " ")
        z = self.all.get(idx + self.line_length + 1, " ")

        if DEBUG:
            print(
                f"""
            +---+---+---+
            | {a} | {b} | {c} |
            +---+---+---+
            | {p} | {v} | {n} |
            +---+---+---+
            | {x} | {y} | {z} |
            +---+---+---+
            """
            )

        neighbour_match = False
        for ch in [a, b, c, p, n, x, y, z]:
            if not v.isdigit():
                break
            if ch.isdigit() or ch == "." or ch == " ":
                continue
            neighbour_match = True

        if DEBUG:
            print(f"[{idx:03}] neighbour_match: {neighbour_match}")

        return neighbour_match

    def neighbour_match(self, idx) -> bool:
        """Print a single field (in the middle) and its neighbours.

        Each single field has the following neighbors:

        a b c - on top
        previous - value - next
        x y z - on the bottom

        +-----+-----+-----+
        | {a} | {b} | {c} |
        +-----+-----+-----+
        | {p} | {v} | {n} |
        +-----+-----+-----+
        | {x} | {y} | {z} |
        +-----+-----+-----+

        """
        a = self.all.get(idx - self.line_length - 1, " ")
        b = self.all.get(idx - self.line_length, " ")
        c = self.all.get(idx - self.line_length + 1, " ")
        p = self.all.get(idx - 1, " ")
        v = self.all.get(idx)
        n = self.all.get(idx + 1, " ")
        x = self.all.get(idx + self.line_length - 1, " ")
        y = self.all.get(idx + self.line_length, " ")
        z = self.all.get(idx + self.line_length + 1, " ")

        if DEBUG:
            print(
                f"""
            +---+---+---+
            | {a} | {b} | {c} |
            +---+---+---+
            | {p} | {v} | {n} |
            +---+---+---+
            | {x} | {y} | {z} |
            +---+---+---+
            """
            )

        neighbour_match = False
        for ch in [a, b, c, p, n, x, y, z]:
            if not v.isdigit():
                break
            if ch.isdigit() or ch == "." or ch == " ":
                continue
            neighbour_match = True

        if DEBUG:
            print(f"[{idx:03}] neighbour_match: {neighbour_match}")

        return neighbour_match


def get_part_numbers(data) -> int:
    """...

    find complete numbers
    get all neighbour fields (idxs) of each number
    check if special character is in these neighbour fields
    if yes -> add to result list
    sumup result list

    """
    __print_field(data)

    idx = 0
    field = Field()

    # Collect given single fields
    for line in data:
        if not field.line_length:
            field.line_length = len(line)

        for c in line:
            field.all[idx] = c
            idx += 1

    # Collect numbers
    all_numbers = []
    list_of_digits = []
    for k, v in field.all.items():
        if v.isdigit():
            list_of_digits.append((k, v))
        else:
            all_numbers.append(list_of_digits)
            list_of_digits = []

    all_numbers = [e for e in all_numbers if e != []]

    pprint(all_numbers)
    relevant_numbers = []
    for list_of_digits in all_numbers:
        relevant = False
        for digit in list_of_digits:
            is_match = field.neighbour_match(digit[0])
            if is_match:
                relevant = True

        if relevant:
            digits_as_number = int("".join([d[1] for d in list_of_digits]))
            relevant_numbers.append(digits_as_number)

    print("\nrelevant_numbers:")
    pprint(relevant_numbers)

    return sum(relevant_numbers)


def main():
    """..."""
    with open("./03/input.txt", "r") as input:
        data = input.read().splitlines()

    sum_of_part_numbers = get_part_numbers(data)
    print(f"sum_of_part_numbers: {sum_of_part_numbers}")


if __name__ == "__main__":
    main()
