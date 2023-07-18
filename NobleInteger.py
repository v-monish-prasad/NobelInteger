def isNobleIntegerIn(array):
    for i in range(len(array)):
        if i == array[i]:
            return 1

    return -1


if __name__ == "__main__":
    A = list(map(int, input().strip('[').strip(']').split(',')))
    A.sort(reverse=True)
    print(isNobleIntegerIn(A))
