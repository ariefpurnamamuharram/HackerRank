# The Minion Game


if __name__ == '__main__':
    # Get input string.
    s = str(input().upper())

    # String list.
    list_s = list(s)

    # Define vowel letters.
    vowels = 'AEIOU'.upper()

    # Initiate Kevin and Stuart's score.
    kevin_score = 0
    stuart_score = 0

    # Start iteration.
    for i in range(len(list_s)):
        if list_s[i] in vowels:
            kevin_score += (len(list_s) - i)
        else:
            stuart_score += (len(list_s) - i)

    # Print result.
    if kevin_score > stuart_score:
        print("Kevin", kevin_score)
    elif kevin_score < stuart_score:
        print("Stuart", stuart_score)
    else:
        print("Draw")

