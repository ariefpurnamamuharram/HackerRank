# 5. Find the Runner-Up Score!


if __name__ == '__main__':
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]

    input_set = set(input_numbers)
    sort_set = sorted(input_set)

    print(sort_set[len(sort_set)-2])
