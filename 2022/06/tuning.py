from lib.data import load_input

CHUNK_SIZE_TASK1 = 4
CHUNK_SIZE_TASK2 = 14


def find_marker(big_fat_long_line, window_size):
    """Return index when the first window of unique letters was found."""
    for idx, letter in enumerate(big_fat_long_line):
        window = big_fat_long_line[idx : idx + window_size]
        if len(set(window)) == window_size:
            break

    return idx + window_size


@load_input("06/input.txt")
def main(data):
    big_fat_long_line = data[0]

    sol1 = find_marker(big_fat_long_line, CHUNK_SIZE_TASK1)
    print(f"[ 06 ][ sol1 ] First marker detected on {sol1}")

    sol2 = find_marker(big_fat_long_line, CHUNK_SIZE_TASK2)
    print(f"[ 06 ][ sol2 ] First marker detected on {sol2}")


if __name__ == "__main__":
    main()
