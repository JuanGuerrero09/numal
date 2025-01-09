import sys


def main():
    print("Hello from numal!")
    if sys.version_info[0] < 3:
        raise Exception("Must be using Python 3")
    print(sys.version_info)


if __name__ == "__main__":
    main()
