# Introduction to sets
# ---
# Calculate distinct plant heights.


def calculate(heights):
    total_heights = sum(set(heights))
    total_distinct_n = len(set(heights))

    return total_heights / total_distinct_n


if __name__ == '__main__':
    input_n = int(input())
    input_heights = [int(x) for x in input().split()]
    print(calculate(input_heights))
