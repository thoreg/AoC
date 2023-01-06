"""

Priorities:
    Lowercase item types a through z have priorities 1 through 26.
    Uppercase item types A through Z have priorities 27 through 52.

"""
from collections import Counter

OFFSET_LOWER_CASE = 96
OFFSET_UPPER_CASE = 38


def _get_priority(letter):
    """Return value for priority according to the rules above."""
    if letter.islower():
        return ord(letter) - OFFSET_LOWER_CASE

    return ord(letter) - OFFSET_UPPER_CASE


def get_issue_letter(line):
    """Return the letter which went wrong plus its priority value."""

    half = int(len(line) / 2)

    first_half = line[:half]
    second_half = line[half:]
    issue_letter = ""

    for letter in first_half:
        if letter in second_half:
            issue_letter = letter
            break

    priority = _get_priority(issue_letter)

    # print(f"{first_half} : {second_half} -> {issue_letter} {priority}")

    return issue_letter, priority


def chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i : i + n]


def get_issue_letter2(line1, line2, line3):
    """Return letter (plus prio) which is in every of the lines."""
    c1 = Counter(line1)
    c2 = Counter(line2)
    c3 = Counter(line3)

    for letter in c1:
        if letter in c2:
            if letter in c3:
                return letter, _get_priority(letter)


if __name__ == "__main__":
    print("starting ...")
    with open("./03/input.txt", "r") as f:
        data = f.read().splitlines()

    sum = 0
    for line in data:
        letter, priority = get_issue_letter(line)
        sum += priority

    print(f"[ 03 ][ sol1 ] sum of priorities: {sum}")

    sum = 0
    for line1, line2, line3 in chunks(data, 3):
        letter, priority = get_issue_letter2(line1, line2, line3)
        sum += priority

    print(f"[ 03 ][ sol2 ] sum of priorities: {sum}")
