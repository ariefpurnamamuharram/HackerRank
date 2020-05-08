# Jumping on the clouds.


if __name__ == '__main__':
    # Get inputs
    n = int(input())
    clouds = [str(x) for x in input().split()]

    # Convert clouds to string.
    str_clouds = ''.join(clouds)

    # Split clouds.
    cumulus_clouds = str_clouds.split('1')

    # Calculate.
    score = []
    for i in range(len(cumulus_clouds)):
        score.append(len(cumulus_clouds[i]) // 2)
    score.append(len(cumulus_clouds) - 1)

    # Print the result.
    print(sum(score))

