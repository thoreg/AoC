"""
The newly-improved calibration document consists of lines of text;
each line originally contained a specific calibration value that the Elves
now need to recover. On each line, the calibration value can be found by
combining
    the first digit and the last digit (in that order) to form
    a single two-digit number.

For example:

1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet

In this example, the calibration values of these four lines are 12, 38, 15,
and 77. Adding these together produces 142.

Consider your entire calibration document.

What is the sum of all of the calibration values?

one, two, three, four, five, six, seven, eight, and nine also count as valid "digits".

"""
import regex


def get_line(data: str) -> int:
    """Return matches for (written) digits from a line like described."""

    # Task 1
    # matches = re.findall(r'(\d)', data)

    matches = regex.findall(
        r"(\d|one|two|three|four|five|six|seven|eight|nine)", data, overlapped=True
    )

    digits_map = {
        "1": 1,
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
    }
    return int(f"{digits_map[matches[0]]}{digits_map[matches[-1]]}")


def test_get_line():
    assert get_line("two1nine") == 29
    assert get_line("eightwothree") == 83
    assert get_line("abcone2threexyz") == 13
    assert get_line("xtwone3four") == 24
    assert get_line("4nineeightseven2") == 42
    assert get_line("zoneight234") == 14
    assert get_line("7pqrstsixteen") == 76
    assert get_line("7fjkfdlmhqxtwoxcpssngss") == 72
    assert get_line("ttmtqrh3four4oneightrkv") == 38


def main():
    with open("./01/input.txt", "r") as input:
        data = input.read().splitlines()

    result = []
    for line in data:
        line_result = get_line(line)
        print(f"{line_result} :: {line}")
        result.append(line_result)

    print(sum(result))


if __name__ == "__main__":
    main()
