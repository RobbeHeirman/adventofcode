import hashlib


def hash_with_tail(start: str, num: int):
    st = f"{start}{num}"
    return hashlib.md5(st.encode('utf-8')).hexdigest()


def part1(inp: str, zeroes=5):
    counter = 0
    check_str = "0" * zeroes
    while True:
        if hash_with_tail(inp, counter)[:5] == check_str:
            return counter
        counter += 1


def main():
    inp = 'ckczppom'
    test_inpt = 'abcdef'
    print(f"Anwser to part1 is: {part1(inp)}")
    print(f"Anwser to part2 is: {part1(inp, zeroes=6)}")
    print(f"Anwser to test is: {part1(test_inpt)}")


if __name__ == "__main__":
    main()
