# 1. If-Else


def is_weird(n):
    if n % 2 == 0:
        if n in range(2, 5):
            return "Not Weird"
        elif n in range(6, 21):
            return "Weird"
        else:
            return "Not Weird"
    else:
        return "Weird"


if __name__ == '__main__':
    a = int(input())
    print(is_weird(a))
