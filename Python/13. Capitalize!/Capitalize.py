# Capitalize!


def solve(s):
    list_string = [str(i).capitalize() for i in s.split(' ')]
    return ' '.join(list_string)

if __name__ == '__main__':
    # Get input.
    inputString = input()

    # Capitalize!
    result = solve(inputString)

    # Print result.
    print(result)
