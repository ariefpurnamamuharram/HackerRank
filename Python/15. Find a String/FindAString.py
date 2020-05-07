# Find a string.


def count(string, substring):
    score = 0
    for i in range(len(string) - len(substring) + 1):
        if string[i] == substring[0]:
            flag = 1
            for j in range(len(substring)):
                if string[i+j] != substring[j]:
                    flag = 0
                    break
            if flag == 1:
                score += 1
    return score


if __name__ == '__main__':
    # Get input.
    string = input()
    substring = input()

    # Get result.
    result = count(string, substring)

    # Print result.
    print(result)
