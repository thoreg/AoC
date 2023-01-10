if __name__ == "__main__":
    print("starting ...")
    with open("./04/input.txt", "r") as f:
        data = f.read().splitlines()

    count_includes = 0
    for line in data:
        range1, range2 = line.split(",")
        min1, max1 = range1.split("-")
        min2, max2 = range2.split("-")
        min1, max1 = int(min1), int(max1)
        min2, max2 = int(min2), int(max2)

        if min1 <= min2 and max2 <= max1:
            # print(f"{min1} <= {min2} <= {max2} <= {max1}")
            count_includes += 1
        elif min2 <= min1 and max1 <= max2:
            # print(f"{min2} <= {min1} <= {max1} <= {max2}")
            count_includes += 1

    print(f"[ 04 ][ sol1 ] sum of cleanup range includes {count_includes}")

    def do_overlap(start1, end1, start2, end2):
        """Return True if the both ranges overlap at all.

        Examples:
            2-4, 6-8 and 2-3, 4-5 don't overlap
            5-7,7-9, 2-8,3-7, 6-6,4-6, and 2-6,4-8 do overlap

        """
        list1 = list(range(start1, end1 + 1))
        list2 = list(range(start2, end2 + 1))
        return set(list1) & set(list2)

    count_overlaps = 0
    for line in data:
        range1, range2 = line.split(",")
        min1, max1 = range1.split("-")
        min2, max2 = range2.split("-")

        if do_overlap(int(min1), int(max1), int(min2), int(max2)):
            count_overlaps += 1

    print(f"[ 04 ][ sol2 ] sum of cleanup range overlaps {count_overlaps}")
