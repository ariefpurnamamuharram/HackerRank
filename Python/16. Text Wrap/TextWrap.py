# Text wrap.
import textwrap


def wrap(string, max_width):
    # Chunk string.
    list_chunk = textwrap.wrap(string, max_width)

    # Print result.
    return "\n".join(list_chunk)


if __name__ == '__main__':
    # Get inputs.
    input_string = str(input())
    n_chunk = int(input())

    # Get result.
    result = wrap(input_string, n_chunk)

    # Print result.
    print(result)
