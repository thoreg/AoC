POINTS = {
    # the opponent plays rock
    ("A", "X"): 4,  # 1 rock 3 draw
    ("A", "Y"): 8,  # 2 paper 6 won
    ("A", "Z"): 3,  # 3 scissor 0 lost
    # the opponent plays paper
    ("B", "X"): 1,  # 1 rock 0 lost
    ("B", "Y"): 5,  # 2 paper 3 draw
    ("B", "Z"): 9,  # 3 scissor 6 won
    # the opponent plays scissor
    ("C", "X"): 7,  # 1 rock 6 won
    ("C", "Y"): 2,  # 2 paper 0 lost
    ("C", "Z"): 6,  # 3 scissor 3 draw
}

RESULT_MAP_TASK_2 = {
    "A": {  # the opponent plays rock
        "X": 3,  # 3 scissor 0 lost
        "Y": 4,  # 1 rock 3 draw
        "Z": 8,  # 2 paper 6 won
    },
    "B": {  # the opponent plays paper
        "X": 1,  # 1 rock 0 lost
        "Y": 5,  # 2 paper 3 draw
        "Z": 9,  # 2 paper 6 won
    },
    "C": {  # the opponent plays scissor
        "X": 2,  # 2 paper 0 lost
        "Y": 6,  # 3 scissor 3 draw
        "Z": 7,  # 1 rock 6 won
    },
}


def main():
    with open("./02/input.txt", "r") as f:
        data = f.read().splitlines()

    sum = 0
    sum2 = 0

    for result in data:
        # solution 1
        player, response = result.split()
        # print(f"{player} {response} => {POINTS[(player, response)]}")
        sum += POINTS[(player, response)]

        # solution 2
        player, expected_result = result.split()
        sum2 += RESULT_MAP_TASK_2[player][expected_result]

    print(f"[ 2 ][ sol 1 ] : sum: {sum}")
    print(f"[ 2 ][ sol 2 ] : sum2: {sum2}")


if __name__ == "__main__":
    main()
