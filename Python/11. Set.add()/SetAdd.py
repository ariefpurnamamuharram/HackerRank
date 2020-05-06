# Set.add()


if __name__ == '__main__':
    # Get n numbers of input
    n = int(input())

    # Get stamps collection.
    stamps = set([])
    for i in range(n):
        stamps.add(input())

    # Print numbers of stamp collection.
    print(len(stamps))
