# No Idea!


if __name__ == '__main__':
    # Get inputs.
    n, m = input().split(' ')
    nNumbers = input().split(' ')
    setA = set(input().split(' '))
    setB = set(input().split(' '))

    # Print result.
    print(sum((i in setA) - (i in setB) for i in nNumbers))
