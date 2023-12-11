from math import prod


def test_get_number_of_possible_wins() -> None:
    """Get the number of possible wins.

    Time:      7  15   30
    Distance:  9  40  200

    """
    assert get_number_of_possible_wins(7, 9) == 4
    assert get_number_of_possible_wins(15, 40) == 8
    assert get_number_of_possible_wins(30, 200) == 9


def get_number_of_possible_wins(time: int, distance: int) -> int:
    """Time hold = speed -> * time left = distance."""

    print(f"\ntime: {time} distance: {distance}")
    result = 0
    for t in range(1, time + 1):
        time_left = time - t
        speed = t
        current_distance = speed * time_left
        # print(f"speed: {t} time left: {time_left} distance: {current_distance}")
        if current_distance > distance:
            result += 1

    print(f"result: {result}")
    return result


def main():
    """..."""
    with open("./06/input.txt", "r") as input:
        data = input.read().splitlines()
    times = data[0].split()[1:]
    distances = data[1].split()[1:]

    result = []
    for time, distance in zip(times, distances):
        result.append(get_number_of_possible_wins(int(time), int(distance)))
    print(f"sol1: {prod(result)}")

    result = get_number_of_possible_wins(53897698, 313109012141201)
    print(f"sol2: {result}")


if __name__ == "__main__":
    main()
