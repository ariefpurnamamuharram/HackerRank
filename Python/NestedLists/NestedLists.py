# Nested lists.


if __name__ == '__main__':
    input_n = int(input())
    students = []

    # Get inputs.
    for i in range(input_n):
        name = str(input())
        score = float(input())
        students.append([name, score])

    # Sort data.
    students.sort(key=lambda x: x[1])

    # Get second lowest score.
    second_lowest_score = 0
    for i in range(len(students)):
        if students[i+1][1] != students[0][1]:
            second_lowest_score = students[i+1][1]
            break

    # Get all students with the same second lowest score.
    result = []
    for i in range(len(students)):
        if students[i][1] == second_lowest_score:
            result.append(students[i])

    # Sort result.
    result.sort(key=lambda x: x[0])

    # Print all result.
    for i in range(len(result)):
        print(result[i][0])

