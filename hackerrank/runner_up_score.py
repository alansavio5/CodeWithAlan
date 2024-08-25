if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arr = list(set(arr))
    first = max(arr)
    arr.sort()
    print(arr[arr.index(first)-1])