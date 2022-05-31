from cs50 import get_int


def main():
    height = get_int("Height :")
    while True:
        if height >= 1 and height <= 8:
            trace(height)
            exit(0)
        else:
            main()


def trace(height):
    for i in range(1, height + 1):
        for j in range(1, height + 1):
            if j <= height - i:
                print(" ", end="")
            else:
                print("#", end="")

        for j in range(2):
            print(" ", end="")

        for j in range(1, height + 1):
            if j <= i:
                print("#", end="")
            else:
                print("", end="")
        print()


if __name__ == "__main__":
    main()

