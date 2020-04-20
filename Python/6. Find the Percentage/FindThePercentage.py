# Find the percentage


if __name__ == '__main__':
    # Get input size number.
    input_n = int(input())

    # Get students data.
    students = {}
    for i in range(input_n):
        student = [str(x) for x in input().split()]
        student_name = student[0]
        student_score = student[1:]
        students[student_name] = student_score

    # Get input student name.
    input_name = str(input())

    # Get student score.
    get_student_score = [float(x) for x in students[input_name]]

    # Calculate student score.
    result = sum(get_student_score) / len(get_student_score)

    # Print result.
    print("{:.2f}".format(result))
