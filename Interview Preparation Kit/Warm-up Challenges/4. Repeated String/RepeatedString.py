# Repeated string.


if __name__ == '__main__':
    # Get inputs.
    s_string = str(input())
    n_repeated = int(input())

    # Convert s_string to list_string.
    list_of_string = list(s_string)

    # Calculate n_div_s and n_mod_s.
    n_div_s = n_repeated // len(list_of_string)
    n_mod_s = n_repeated % len(list_of_string)

    # Calculate how many 'a' in given string.
    num_of_a = 0
    for i in list_of_string:
        if i == 'a':
            num_of_a += 1

    # Calculate total a.
    total = 0
    if n_repeated <= len(list_of_string):
        for i in range(n_repeated):
            if list_of_string[i] == 'a':
                total += 1
    else:
        total = num_of_a * n_div_s
        for i in range(n_mod_s):
            if list_of_string[i] == 'a':
                total += 1

    # Print result.
    print(total)
