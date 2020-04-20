# Merge the tools.


if __name__ == '__main__':
    # Get input string and number of members for each group.
    input_string = str(input())
    input_k = int(input())

    # Calculate string length.
    string_length = len(input_string)

    # Convert input string to list.
    string_list = list(input_string)

    # Calculate total group.
    total_group = int(string_length / input_k)

    # Grouping.
    string_groups = []
    for i in range(total_group):
        tmp_group = []
        k = i * input_k
        while k < ((i + 1) * input_k):
            tmp_group.append(string_list[k])
            k += 1
        string_groups.append(tmp_group)

    # Clean from duplicates and print the result.
    for i in range(len(string_groups)):
        new_string = []
        for j in range(len(string_groups[i])):
            if string_groups[i][j] not in new_string:
                new_string.append(string_groups[i][j])
        print(''.join(new_string))

