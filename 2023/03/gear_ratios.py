from dataclasses import dataclass, field
from pprint import pprint

# DEBUG = False
DEBUG = True


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


def test_get_gear_ratio():
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
    assert get_gear_ratio(data) == 467835


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

    def neighbour_match2(self, idx) -> tuple[bool, int | None]:
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

        star_idx = None
        neighbour_match = False
        ch_idx_map = {
            0: idx - self.line_length - 1,
            1: idx - self.line_length,
            2: idx - self.line_length + 1,
            3: idx - 1,
            4: idx + 1,
            5: idx + self.line_length - 1,
            6: idx + self.line_length,
            7: idx + self.line_length + 1,
        }

        # if idx > 90:
        #     import ipdb; ipdb.set_trace()
        for ch_idx, ch in enumerate([a, b, c, p, n, x, y, z]):
            if not v.isdigit():
                break
            if ch != "*":
                continue
            neighbour_match = True
            star_idx = ch_idx_map[ch_idx]

        if DEBUG:
            print(
                f"[{idx:03}] neighbour_match: {neighbour_match} : "
                f"star_idx: {star_idx}"
            )

        return neighbour_match, star_idx

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


def get_gear_ratio(data):
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
    numbers_with_stars = []

    for list_of_digits in all_numbers:
        relevant = False
        last_star_idx = None
        for digit in list_of_digits:
            is_match, star_index = field.neighbour_match2(digit[0])
            # if is_match and star_index is None:
            #     import ipdb; ipdb.set_trace()

            if is_match and star_index:
                relevant = True
                last_star_idx = star_index

        if relevant:
            digits_as_number = int("".join([d[1] for d in list_of_digits]))
            numbers_with_stars.append((digits_as_number, last_star_idx))

    print("\nnumbers_with_stars:")
    pprint(numbers_with_stars)

    numbers_per_star_idx = {}
    for num_w_stars in numbers_with_stars:
        star_idx = num_w_stars[1]
        if star_idx not in numbers_per_star_idx:
            numbers_per_star_idx[star_idx] = []
        numbers_per_star_idx[star_idx].append(num_w_stars[0])

    print("numbers_per_star_idx: ")
    pprint(numbers_per_star_idx)
    result = []
    for k, v in numbers_per_star_idx.items():
        if len(v) == 2:
            result.append(v[0] * v[1])

    pprint(result)
    __print_field(data)

    return sum(result)


def main():
    """..."""
    with open("./03/input.txt", "r") as input:
        data = input.read().splitlines()
    #
    # Solution - Task 1
    #
    # sum_of_part_numbers = get_part_numbers(data)
    # print(f"sum_of_part_numbers: {sum_of_part_numbers}")

    gear_ratio = get_gear_ratio(data)
    print(f"gear_ratio: {gear_ratio}")


if __name__ == "__main__":
    main()
