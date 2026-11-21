import sys

if __name__ == "__main__":
    if (len(sys.argv) != 2):
        sys.stderr.write("usage: pac-man config.json\n")
        sys.exit(1)

    sys.exit(0)
