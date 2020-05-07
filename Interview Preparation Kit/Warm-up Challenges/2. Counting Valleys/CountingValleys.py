# Counting valleys.


def count_valleys(string):
    list_of_string = list(string)

    score = 0
    valleys = 0
    for i in list_of_string:
        if i == 'U':
            score += 1
        if i == 'D':
            score -= 1
        if score == 0 and i == 'U':
            valleys += 1

    return valleys


if __name__ == '__main__':
    # Get inputs.
    input_n = int(input())
    input_string = str(input())

    # Count valleys.
    result = count_valleys(input_string)

    # Print result.
    print(result)
