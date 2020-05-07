# Sock merchant.


def sock_merchant(n, socks):
    sock_collections = {}

    for i in socks:
        if i not in sock_collections:
            sock_collections[i] = 1
        else:
            value = sock_collections[i]
            sock_collections[i] = value+1

    arr_socks_stocks = []
    for k in sock_collections:
        value = sock_collections[k]
        arr_socks_stocks.append(value // 2)

    return sum(arr_socks_stocks)


if __name__ == '__main__':
    # Get inputs.
    input_n = int(input())
    input_socks = map(str, input().split())

    # Get result of sock stocks.
    result = sock_merchant(input_n, input_socks)

    # Print result.
    print(result)
