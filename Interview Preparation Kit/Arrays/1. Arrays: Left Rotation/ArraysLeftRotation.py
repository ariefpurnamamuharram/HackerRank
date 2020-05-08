# Array left rotation.
# ---------------------
# A solution by Arief Purnama Muharram


if __name__ == '__main__':
    # Get inputs.
    n, d = map(int, input().split())
    a = [str(x) for x in input().split()]

    # Do array shift.
    for i in range(d):
        a.append(a[i])
    for j in range(d):
        del a[0]

    # Print result.
    print(' '.join(a))
