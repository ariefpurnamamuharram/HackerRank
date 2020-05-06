# Symetric difference.


if __name__ == '__main__':
    # Get inputs.
    m = int(input())
    mIntegers = set(input().split())
    n = int(input())
    nIntegers = set(input().split())

    # Get mIntegers union with nIntegers.
    mUn = mIntegers.union(nIntegers)

    # Get mIntegers intersection with nIntegers.
    mIn = mIntegers.intersection(nIntegers)

    # Get list of differences of mUn with mIn.
    diff = list(mUn.difference(mIn))

    # Convert diff to listDiff.
    listDiff = list(map(int, diff))

    # Print the result.
    for i in sorted(listDiff):
        print(i)
