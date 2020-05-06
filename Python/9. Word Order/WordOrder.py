# Word order


if __name__ == '__main__':
    # Get n input numbers.
    n = int(input())

    # Get words.
    words = []
    for i in range(n):
        words.append(str(input()))

    # Create dictionary.
    sets = {}
    for j in words:
        if j not in sets:
            sets[j] = 1
        else:
            value = sets[j]
            sets[j] = value+1

    # Parse list.
    result = []
    for k in sets:
        result.append(str(sets[k]))

    # Print result.
    print(len(sets))
    print(' '.join(result))

