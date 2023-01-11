import re
from copy import deepcopy
from pprint import pprint

LINES_2_SKIP = 10

pattern = re.compile("move ([0-9\(\)]+) from ([0-9\(\)]+) to ([0-9\(\)]+)")


def process(stacks, step, crate_mover_version=9000):
    """Process as single instruction/step.

    step looks like 'move 4 from 9 to 1'

    CrateMover 9000 -> Moves one single box at a time (order of boxes changes)
    CrateMover 9001 -> Moves multiple boxes at a time (order of boxes stays the same)

    """
    match = re.search(pattern, step)
    if not match:
        print("\nERROR - no match - return\n")

    number_of_boxes = int(match.group(1))
    src_stack = int(match.group(2))
    target_stack = int(match.group(3))

    if crate_mover_version == 9000:
        for _idx in range(number_of_boxes):
            box = stacks[src_stack].pop()
            stacks[target_stack].append(box)
    elif crate_mover_version == 9001:
        boxes = stacks[src_stack][-number_of_boxes:]
        stacks[target_stack].extend(boxes)
        del stacks[src_stack][-number_of_boxes:]


def main():

    STACKS = {
        1: ["F", "H", "B", "V", "R", "Q", "D", "P"],
        2: ["L", "D", "Z", "Q", "W", "V"],
        3: ["H", "L", "Z", "Q", "G", "R", "P", "C"],
        4: ["R", "D", "H", "F", "J", "V", "B"],
        5: ["Z", "W", "L", "C"],
        6: ["J", "R", "P", "N", "T", "G", "V", "M"],
        7: ["J", "R", "L", "V", "M", "B", "S"],
        8: ["D", "P", "J"],
        9: ["D", "C", "N", "W", "V"],
    }

    with open("./05/input.txt", "r") as f:
        data = f.read().splitlines()
    data = data[LINES_2_SKIP:]

    stacks_sol1 = deepcopy(STACKS)
    for step in data:
        process(stacks_sol1, step)
    boxes = "".join([v[-1] for v in stacks_sol1.values()])
    print(f"[ 05 ][ sol1 ] Last boxes on the stack {boxes}")

    stacks_sol2 = deepcopy(STACKS)
    for step in data:
        process(stacks_sol2, step, 9001)
    boxes = "".join([v[-1] for v in stacks_sol2.values()])
    print(f"[ 05 ][ sol2 ] Last boxes on the stack {boxes}")


if __name__ == "__main__":
    main()
